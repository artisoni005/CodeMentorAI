import os
import time
from dotenv import load_dotenv
from google import genai
from groq import Groq

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

gemini_client = genai.Client(api_key=gemini_api_key)
groq_client = Groq(api_key=groq_api_key)


def generate_response(prompt):

    # Try Gemini first
    for attempt in range(4):

        try:
            response = gemini_client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            error_message = str(e)

            # Gemini quota exhausted
            if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
                print("Gemini quota exhausted. Switching to Groq...")
                break

            # Gemini temporarily unavailable
            if "503" in error_message or "UNAVAILABLE" in error_message:

                if attempt < 3:
                    wait_time = 5 * (attempt + 1)

                    print(
                        f"Gemini temporarily unavailable. "
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)
                    continue

            # Other Gemini error
            raise e

    # Groq fallback
    try:

        print("Using Groq fallback...")

        response = groq_client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:

        raise Exception(
            f"Both Gemini and Groq failed.\n"
            f"Groq error: {str(e)}"
        )