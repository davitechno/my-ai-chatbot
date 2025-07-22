import google.generativeai as genai

API_KEY = "AIzaSyAFlMlbw7tIvZ9cLwtjfM7_vzD4am-Mlew"

genai.configure(api_key = API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")   

query = "who build kartar combines"

responce = model.generate_content(query)

print(responce.text)