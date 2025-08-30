import os
import openai
import anthropic
import google.generativeai as genai

class LLMClient:
    def __init__(self, provider, api_key):
        self.provider = provider.lower()
        self.api_key = api_key

        if self.provider == "openai":
            openai.api_key = api_key
        elif self.provider == "anthropic":
            self.client = anthropic.Anthropic(api_key=api_key)
        elif self.provider == "gemini":
            genai.configure(api_key=api_key)

    def generate(self, prompt):
        if self.provider == "openai":
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return response["choices"][0]["message"]["content"]

        elif self.provider == "anthropic":
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=800,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text

        elif self.provider == "gemini":
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            return response.text

        else:
            raise ValueError("Unsupported provider")
