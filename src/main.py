import time
from config import (
    SHEET_ID,
    SHEET_RANGE,
    CREDENTIALS_FILE,
    LLM_PROVIDER,
    LLM_CONFIG,
    SELECTED_MODEL,
    MAX_POST_LENGTH,
    PROMPT_TEMPLATE
)
from sheets_handler import GoogleSheetsHandler
from llm_handler import get_llm_handler

def main():
    # Initialize handlers
    sheets_handler = GoogleSheetsHandler(CREDENTIALS_FILE, SHEET_ID)
    llm_handler = get_llm_handler(LLM_PROVIDER, LLM_CONFIG)
    
    print(f"Starting LinkedIn post generation process using {LLM_PROVIDER} - {SELECTED_MODEL}...")
    
    while True:
        try:
            # Read topics from Google Sheet
            topics = sheets_handler.read_topics(SHEET_RANGE)
            
            if not topics:
                print("No new topics to process. Waiting for 5 minutes...")
                time.sleep(300)  # Wait 5 minutes before checking again
                continue
            
            print(f"Found {len(topics)} topics to process.")
            
            # Process each topic
            for topic in topics:
                print(f"\nProcessing topic: {topic['topic']}")
                
                # Get model configuration
                model_config = LLM_CONFIG[LLM_PROVIDER]["available_models"][SELECTED_MODEL]
                
                try:
                    # Generate post using selected LLM
                    generated_post = llm_handler.generate_text(
                        prompt=PROMPT_TEMPLATE.format(topic=topic['topic']),
                        max_tokens=model_config["max_tokens"],
                        temperature=model_config["temperature"]
                    )
                    
                    if generated_post:
                        # Update the sheet with the generated post
                        sheets_handler.update_post(
                            topic['row_index'],
                            generated_post
                        )
                        print("Post generated and saved successfully!")
                    else:
                        print("Failed to generate post. Skipping...")
                        
                except Exception as e:
                    print(f"Error generating post: {str(e)}")
                    print("Skipping to next topic...")
                    continue
                
                # Wait a bit between requests to avoid rate limits
                time.sleep(2)
            
            print("\nAll topics processed. Waiting for new topics...")
            time.sleep(300)  # Wait 5 minutes before checking for new topics
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Retrying in 5 minutes...")
            time.sleep(300)

if __name__ == "__main__":
    main()
