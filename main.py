from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import json

app = FastAPI()

class ItemBody(BaseModel):
    text:str
    offset:int
    mode:""

@app.get('/test')
def for_checking():
    return {"msg":"hi from text"}

@app.get('/test/')
def add_user(name:str):
    with open('names.txt','a') as f:
        f.write(name)

@app.post('/caesar')
def handel_caesar_cipher(body:ItemBody):
    if body.mode == 'encrypt':
        return {'encrypted_text':body.text}
    else:
        return {'decrypted':body.text}

@app.get('fence/encrypt')
def encrypted_by_fence(text:str):
    return {'encrypted_text':text}

@app.post('fence/decrypt')
def decrypted_by_fence(body:ItemBody):
    return {'decrypted': body.text}


if __name__ == '__main__':
    uvicorn.run(app,host='localhost',port=8000 )