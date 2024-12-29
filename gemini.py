import google.generativeai as genai
from datetime import datetime
import os
from dotenv import load_dotenv
import json

def helper(text):
    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    current_date = datetime.now().strftime("%Y-%m-%d")
    role = "You are a model which gives response in the format {'name':'name of the task','due':'due date and time of the task in ISO 8601 date format'}."
    query = text + "today date is " + current_date
    prompt = f"{role} {query}"
    response = model.generate_content(prompt)
    print(response.text)
    return json.loads(response.text.replace("`","").replace("json","").replace("'",'"'))
