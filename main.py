from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis
import hashlib

app = FastAPI()

# Verbinden met Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

class URLRequest(BaseModel):
    url: str

@app.post("/shorten")
def shorten_url(request: URLRequest):
    """Genereer een korte URL en sla op in Redis"""
    short_hash = hashlib.md5(request.url.encode()).hexdigest()[:6]
    
    # Opslaan in Redis met een vervaldatum (bijv. 7 dagen)
    redis_client.setex(short_hash, 604800, request.url)
    
    return {"short_url": f"http://localhost:8000/{short_hash}"}

@app.get("/{short_hash}")
def redirect_to_url(short_hash: str):
    """Korte URL omzetten naar originele link"""
    original_url = redis_client.get(short_hash)
    
    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return {"original_url": original_url}
