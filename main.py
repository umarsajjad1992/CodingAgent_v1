import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if len(sys.argv) < 2:
        print("I need a prompt as an argument. Usage: uv run main.py \"<prompt>\"")
        sys.exit(1)
    prompt = sys.argv[1]
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite", 
        contents=messages
    )

    print(response.text)
    #Since response can be empty, we need to check if the usage_metadata is not None before accessing its attributes
    if response is None or response.usage_metadata is None:
        print("No usage metadata available.")
        return
    print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response Tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()