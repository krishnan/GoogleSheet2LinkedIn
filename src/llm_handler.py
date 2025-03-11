from typing import Optional, Dict, Any
import openai
from anthropic import Anthropic
import google.generativeai as genai
import cohere
from abc import ABC, abstractmethod

class LLMHandler(ABC):
    @abstractmethod
    def generate_text(self, prompt: str, max_tokens: int, temperature: float) -> str:
        pass

class OpenAIHandler(LLMHandler):
    def __init__(self, api_key: str):
        self.client = openai.OpenAI(api_key=api_key)
        
    def generate_text(self, prompt: str, max_tokens: int, temperature: float) -> str:
        try:
            response = self.client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": "You are a professional content creator specializing in creating engaging LinkedIn posts."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")

class AnthropicHandler(LLMHandler):
    def __init__(self, api_key: str):
        self.client = Anthropic(api_key=api_key)
        
    def generate_text(self, prompt: str, max_tokens: int, temperature: float) -> str:
        try:
            response = self.client.messages.create(
                model=model_name,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            return response.content[0].text.strip()
        except Exception as e:
            raise Exception(f"Anthropic API error: {str(e)}")

class GoogleAIHandler(LLMHandler):
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
    def generate_text(self, prompt: str, max_tokens: int, temperature: float) -> str:
        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=max_tokens,
                    temperature=temperature
                )
            )
            return response.text.strip()
        except Exception as e:
            raise Exception(f"Google AI API error: {str(e)}")

class CohereHandler(LLMHandler):
    def __init__(self, api_key: str):
        self.client = cohere.Client(api_key)
        
    def generate_text(self, prompt: str, max_tokens: int, temperature: float) -> str:
        try:
            response = self.client.generate(
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.generations[0].text.strip()
        except Exception as e:
            raise Exception(f"Cohere API error: {str(e)}")

def get_llm_handler(provider: str, config: Dict[str, Any]) -> LLMHandler:
    """Factory function to create the appropriate LLM handler."""
    handlers = {
        "openai": OpenAIHandler,
        "anthropic": AnthropicHandler,
        "google": GoogleAIHandler,
        "cohere": CohereHandler
    }
    
    if provider not in handlers:
        raise ValueError(f"Unsupported LLM provider: {provider}")
        
    handler_class = handlers[provider]
    return handler_class(config[provider]["api_key"]) 