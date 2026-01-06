import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# DeepSeek client (OpenAI-compatible)
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

app = FastAPI()

@app.post("/")
async def quote_generate():
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": "You are a motivational speaker."
                },
                {
                    "role": "user",
                    "content": "Give a most powerful motivational quote."
                }
            ],
            max_tokens=40,
            temperature=0.7
        )

        return {
            "quote": response.choices[0].message.content.strip()
        }

    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
