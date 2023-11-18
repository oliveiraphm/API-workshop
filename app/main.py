from fastapi import FastAPI 
from typing import List, Dict, Any
from schemas import Produto

app = FastAPI()




id_atual = 3

def lista(self):
    return self.produtos

def inserir(self, item: Dict[str, any]) -> Dict[str, any]:
    self.id_atual += 1
    item["id"] = self.id_atual
    return self.produtos.append(item)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/produtos")
def listar_produtos():
    """
    View que que retorna o dicionário de produtos
    """
    return produtos