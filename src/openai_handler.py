from openai import OpenAI
from typing import Optional

class OpenAIHandler:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def generate_post(self, topic: str, prompt_template: str, max_length: int) -> str:
        """Generate a LinkedIn post using OpenAI's GPT-4 model."""
        prompt = prompt_template.format(topic=topic)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",  # You can also use "gpt-4-turbo-preview" for the latest model
                messages=[
                    {"role": "system", "content": "You are a professional content creator specializing in creating engaging LinkedIn posts that are technically accurate and insightful."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_length,
                temperature=0.7,
                top_p=1.0,
                frequency_penalty=0.3,
                presence_penalty=0.3
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"Error generating post: {str(e)}")
            return None
