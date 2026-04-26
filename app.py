import streamlit as st
from pymongo import MongoClient
import pandas as pd

# =========================
# CONEXÃO COM O MONGODB
# =========================
# Conexão com banco local (fora do Docker)
client = MongoClient("mongodb://localhost:27017/")
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
            # Inserção de dados no MongoDB
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
        # Exibe a quantidade total de registros cadastrados
        st.subheader("📊 Estatísticas")
        st.metric("Total de registros", len(df))

    else:
        st.info("Nenhum dado cadastrado ainda.")

# =========================
# EDITAR / EXCLUIR
# =========================
elif menu == "Editar/Excluir":
    st.subheader("✏️ Editar ou Excluir Cliente")

    # Busca todos os dados do banco
    dados = list(collection.find())

    if dados:
        # Cria uma lista com nome + parte do ID para evitar duplicidade
        opcoes = {f"{d['nome']} ({str(d['_id'])[:5]})": d for d in dados}

        selecionado = st.selectbox("Selecione um cliente", list(opcoes.keys()))

        cliente = opcoes[selecionado]

        # Campos para edição dos dados
        novo_nome = st.text_input("Novo nome", cliente["nome"])
        novo_email = st.text_input("Novo email", cliente["email"])

        col1, col2 = st.columns(2)

        # =========================
        # EDITAR
        # =========================
        with col1:
            if st.button("Atualizar"):
                # Atualiza os dados no MongoDB
                collection.update_one(
                    {"_id": cliente["_id"]},
                    {"$set": {
                        "nome": novo_nome,
                        "email": novo_email
                    }}
                )
                st.success("Cliente atualizado com sucesso!")

        # =========================
        # EXCLUIR
        # =========================
        with col2:
            if st.button("Excluir"):
                # Remove o registro do banco
                collection.delete_one({"_id": cliente["_id"]})
                st.warning("Cliente excluído!")

    else:
        st.info("Nenhum dado para editar ou excluir.")