import streamlit as st
from pymongo import MongoClient
import pandas as pd

# conexão com MongoDB
client = MongoClient("mongodb://mongodb:27017/")
db = client["eshop"]
collection = db["clientes"]

st.title("📊 E-Shop Brasil")

menu = st.sidebar.selectbox("Menu", [
    "Inserir",
    "Visualizar",
    "Editar/Excluir"
])

# INSERIR
if menu == "Inserir":
    nome = st.text_input("Nome")
    email = st.text_input("Email")

    if st.button("Salvar"):
        collection.insert_one({
            "nome": nome,
            "email": email
        })
        st.success("Salvo!")

# VISUALIZAR
elif menu == "Visualizar":
    dados = list(collection.find({}, {"_id": 0}))
    df = pd.DataFrame(dados)
    st.dataframe(df)

# EDITAR / EXCLUIR
elif menu == "Editar/Excluir":
    dados = list(collection.find())
    
    if dados:
        nomes = [d["nome"] for d in dados]
        selecionado = st.selectbox("Selecione", nomes)

        if st.button("Excluir"):
            collection.delete_one({"nome": selecionado})
            st.warning("Excluído!")