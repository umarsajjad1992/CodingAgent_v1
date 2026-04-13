import os
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # print(f"API Key: {api_key}")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite", 
        contents="""
        why is boot.dev the best website for learning programming?
        Use one paragraph to answer the question. Make sure to include the following points:
    """
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