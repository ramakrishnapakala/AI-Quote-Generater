import os
from fastapi import FastAPI,HTTPException
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
# openai
client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))
app = FastAPI()
@app.post("/")
async def quote_generate():
     try:
          response = client.chat.completions.create(
               model="gpt-4o-mini",
               messages=[
                    {
                         "role":"system",
                         "content":"Your the motivatinal speaker"
                    },{
                         "role":"user",
                         "content":"Give a most powerfull motivational quote"
                    }
               ],
               max_tokens=40,
               temperature=0.7
          )
          return {"quote":response.choices[0].message.content.strip()}
     except Exception as err:
          HTTPException(status_code=500,detail=str(err))