#uvicorn main:app --reload
#http://127.0.0.1:8000

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional



app = FastAPI()
   
    

#-----------------------------------------
@app.get("/")
def index():
    return {"mensaje": "Hola Python"}

@app.get("/libros/{id}")
def mostrar_libros(id: int):
    return{"data": id}

@app.get("/calculadora/{op_1}/{op_2}")
def calcular(op_1: float, op_2: float):
    return {'resultado': op_1 * op_2} 
#-----------------------------------------

#https://api-11.onrender.com/docs#/