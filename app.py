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

# =========================
# INSERIR
# =========================
if menu == "Inserir":
    nome = st.text_input("Nome")
    email = st.text_input("Email")

    if st.button("Salvar"):
        collection.insert_one({
            "nome": nome,
            "email": email
        })
        st.success("Salvo!")

# =========================
# VISUALIZAR
# =========================
elif menu == "Visualizar":
    
    # Consulta os documentos no MongoDB e transforma em DataFrame
    # Boa prática: o uso do Pandas facilita a manipulação, organização
    # e análise dos dados
    df = pd.DataFrame(list(collection.find({}, {"_id": 0})))

    if not df.empty:
        st.subheader("📋 Dados cadastrados")
        st.dataframe(df)

        # 📊 MÉTRICA
        st.subheader("📊 Estatísticas")
        st.metric("Total de registros", len(df))

    else:
        st.info("Nenhum dado cadastrado ainda.")

# =========================
# EDITAR / EXCLUIR
# =========================
elif menu == "Editar/Excluir":
    
    df = pd.DataFrame(list(collection.find()))

    if not df.empty:
        selecionado = st.selectbox("Selecione", df["nome"])

        if st.button("Excluir"):
            collection.delete_one({"nome": selecionado})
            st.warning("Excluído!")
    else:
        st.info("Nenhum dado para editar ou excluir.")