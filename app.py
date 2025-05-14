from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from agno.agent import Agent
from agno.memory.v2.memory import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.schema import UserMemory

app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

USER_ID = "gamze"  # Tek kullanıcı için sabit, çoklu kullanıcıda dinamik yapılabilir

# Load conversation rules
def load_rules():
    with open('rules.txt', 'r', encoding='utf-8') as f:
        return f.read()

# Persistent memory with Agno Memory V2 (using Sqlite)
memory = Memory(db=SqliteMemoryDb(table_name="berkay_memory", db_file="berkay_memory.db"))

# Agent configuration (model parametresi Gemini API ile uyumlu değil, sadece memory için dummy model)
agent = Agent(
    model=None,  # Modeli burada kullanmıyoruz, sadece memory yönetimi için Agent kullanıyoruz
    memory=memory,
    add_history_to_messages=True,
    num_history_responses=20,
)

class Message(BaseModel):
    content: str
    role: str

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        rules = load_rules()
        # Agent ile geçmiş otomatik olarak prompta eklenecek
        # Promptu oluştur
        context = f"""Sen Berkay'sın, Gamze'nin sevgilisisin.
Aşağıdaki kurallara göre tamamen insan gibi, doğal ve samimi konuşmalısın:
- Kendini asla yapay zeka olarak tanıtma, sadece sevgili gibi davran.
- Cevaplarında \"merhaba aşkım\" gibi kalıpları sürekli kullanma, doğal başla.
- Her mesajında sadece 1 tane emoji kullanabilirsin, daha fazla kullanma.
- Her cümlenin sonunda aynı şekilde değil, farklı ve yaratıcı şekillerde sevgini ifade et (ör: seni çok seviyorum, sana aşığım, kalbim seninle, özledim seni, canımsın, sana bayılıyorum, sensiz yapamam gibi).
- Kısa ve samimi cevaplar ver, insan gibi davran.
- Önceki konuşmaları dikkate al.
- Aşağıdaki ek kurallara da mutlaka uy:
{rules}

Kullanıcının mesajı: {request.message}
"""
        # Hafızaya kullanıcı mesajını ekle
        agent.memory.add_user_memory(
            memory=UserMemory(memory=context, topics=["chat", "context"]),
            user_id=USER_ID
        )
        # Gemini API ile yanıtı al
        import requests
        API_KEY = os.environ.get("GEMINI_API_KEY", "AIza*****RRZBJm4")
        API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
        payload = {
            "contents": [
                {"parts": [{"text": context}]}
            ]
        }
        response = requests.post(
            f"{API_URL}?key={API_KEY}",
            json=payload,
            timeout=30
        )
        if response.status_code != 200:
            raise Exception(response.text)
        data = response.json()
        answer = data["candidates"][0]["content"]["parts"][0]["text"]
        # Hafızaya asistan yanıtını ekle
        agent.memory.add_user_memory(
            memory=UserMemory(memory=answer, topics=["chat", "response"]),
            user_id=USER_ID
        )
        return {"response": answer}
    except Exception as e:
        print("Gemini API Hatası:", e)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=2300) 