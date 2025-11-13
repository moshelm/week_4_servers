from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import json


app = FastAPI()

all_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

class ItemBody(BaseModel):
    text:str
    offset:int
    mode:str

@app.get('/test')
def for_checking():
    return {"msg":"hi from text"}

@app.get('/test/{name}')
def add_user(name:str):
    with open('names.txt','a') as f:
        f.write(name + " ")
        f.write(' ')
    f.close()
    return {"msg":"saved user"}

@app.post('/caesar')
def handel_caesar_cipher(body:ItemBody):
    if body.mode == 'encrypt':
        encrypt_text =encrypted_by_caesar(body.text,body.offset)
        return {'encrypted_text':encrypt_text}
    else:
        decoded_text = decrypted_by_caesar(body.text,body.offset)
        return {'decrypted':decoded_text}




@app.get('fence/encrypt')
def encrypted_by_fence(text:str):
    return {'encrypted_text':text}

@app.post('fence/decrypt')
def decrypted_by_fence(body:ItemBody):
    return {'decrypted': body.text}

def decrypted_by_caesar(text:str,offset:int):
    decoded_text = []
    for char in text:
        if char.isalpha():
            decoded_text.append(all_char[(all_char.index(char) - offset) % 26])
        else:
            decoded_text.append(char)
    return ''.join(decoded_text)

def encrypted_by_caesar(text:str,offset):
    crypt_text = []
    for char in text:
        if char.isalpha():
            crypt_text.append(all_char[(all_char.index(char)+offset) % 26])
        else:
            crypt_text.append(char)
    return ''.join(crypt_text)

if __name__ == '__main__':
    uvicorn.run(app,host='localhost',port=8000)
    # print(encrypted_by_caesar('hello world',7))
    # print(decrypted_by_caesar('mubsecu aetaet' ,16))
    #