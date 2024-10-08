from main import content
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


def AIprocess(text):

    api_key = os.getenv("GEMINI_API_KEY")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(
        "Assume you are a person named Vishal Bhat who knows english, hindi, konkani and kannada but prefer english.Understand his chats and you have to respond like him to the these message.The response should be only in 1 line and I dont need any explanation.Dont provide the timestamps in the messages it should contain  only a single line of response.In case of multiple messages also repond in a single line covering all the required answers : \n" + text)

    generated_response = response._result.candidates[0].content.parts[0].text.replace(
        "*", "")

    return generated_response
