from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


app = FastAPI()

all_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class ItemBodyCaesar(BaseModel):
    text:str
    offset:int
    mode:str

class ItemBodyFence(BaseModel):
    text:str

@app.get('/test')
def checking_point():
    return {"msg":"hi from text"}

@app.get('/test/{name}')
def add_user(name:str):
    with open('names.txt','a') as f:
        f.write(name + " ")
        f.write(' ')
    return {"msg":"saved user"}

@app.post('/caesar')
def caesar_cipher_management(body:ItemBodyCaesar):
    if body.mode == 'encrypt':
        encrypted_text =caesar_cipher_encryption(body.text,body.offset)
        return {'encrypted_text':encrypted_text}
    else:
        decoded_text = caesar_cipher_decryption(body.text, body.offset)
        return {'decrypted':decoded_text}

@app.get('/fence/encrypt')
def encrypted_fence_cipher(text:str):
    return {'encrypted_text':fence_cipher_encryption(text)}

def fence_cipher_encryption(text:str):
    text_no_space = text.replace(' ', '')
    encrypted_text = text_no_space[::2] + text_no_space[1::2]
    return encrypted_text

@app.post('/fence/decrypt')
def decrypted_fence_cipher(body:ItemBodyFence):
    return {'decrypted': fence_cipher_decryption(body.text)}

def fence_cipher_decryption(text:str):
    # The boundary between even and odd
    limit = len(text)//2 + len(text) % 2
    # Division by type
    even_text = text[:limit]
    odd_text = text[limit:]

    decoded_text = []

    for index in range(len(even_text)):
        decoded_text.append(even_text[index])
        # test ot of range, finish odd_text
        if len(odd_text) > index:
            decoded_text.append(odd_text[index])
    return ''.join(decoded_text)

def caesar_cipher_decryption(text:str, offset:int):
    decoded_text = []
    for char in text:
        if char.isalpha():
            # find the original char in all chars by calculate index - offset and module 26
            decoded_text.append(all_chars[(all_chars.index(char) - offset) % 26])
        else:
            # if char is space
            decoded_text.append(char)
    return ''.join(decoded_text)

def caesar_cipher_encryption(text:str,offset):
    crypt_text = []
    for char in text:
        if char.isalpha():
            # find the original char in all chars by calculate index + offset and module 26
            crypt_text.append(all_chars[(all_chars.index(char) + offset) % 26])
        else:
            # if char is space
            crypt_text.append(char)
    return ''.join(crypt_text)

if __name__ == '__main__':
    uvicorn.run(app,host='localhost',port=8000)
