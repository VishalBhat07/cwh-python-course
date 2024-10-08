import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def AIprocess(c):

    api_key = os.getenv("GEMINI_API_KEY")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(c + "The response should not be too long.")

    generated_response = response._result.candidates[0].content.parts[0].text

    return generated_response
