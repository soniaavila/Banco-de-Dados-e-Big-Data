import streamlit as st
from pymongo import MongoClient
import pandas as pd

# =========================
# CONEXÃO COM O MONGODB
# =========================
client = MongoClient("mongodb://mongodb:27017/")
db = client["eshop"]
collection = db["clientes"]

# =========================
# INTERFACE PRINCIPAL
# =========================
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
    st.subheader("➕ Inserir Cliente")

    nome = st.text_input("Nome")
    email = st.text_input("Email")

    if st.button("Salvar"):
        if nome and email:
            collection.insert_one({
                "nome": nome,
                "email": email
            })
            st.success("Salvo com sucesso!")
        else:
            st.warning("Preencha todos os campos!")

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
    st.subheader("✏️ Editar ou Excluir Cliente")

    dados = list(collection.find())

    if dados:
        # Seleciona o cliente direto do objeto
        cliente = st.selectbox(
            "Selecione um cliente",
            options=dados,
            format_func=lambda x: x["nome"]
        )

        # Campos aparecem sempre
        novo_nome = st.text_input("Novo nome", cliente["nome"])
        novo_email = st.text_input("Novo email", cliente["email"])

        col1, col2 = st.columns(2)

        # EDITAR
        with col1:
            if st.button("Atualizar"):
                collection.update_one(
                    {"_id": cliente["_id"]},
                    {"$set": {
                        "nome": novo_nome,
                        "email": novo_email
                    }}
                )
                st.success("Atualizado com sucesso!")

        # EXCLUIR
        with col2:
            if st.button("Excluir"):
                collection.delete_one({"_id": cliente["_id"]})
                st.warning("Excluído!")

    else:
        st.info("Nenhum dado para editar ou excluir.")