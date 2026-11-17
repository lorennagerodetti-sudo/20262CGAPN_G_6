#Carregar o pandas e o streamlit
import pandas as pd
import streamlit as st

#Função para classificar porte
def classifica_porte(total):
    if total <= 200:
        return "Pequena"
    elif total <= 400:
        return "Média"
    else:
        return "Grande"

#Leitura de Dados
censo = pd.read_csv("escolas_sp_regioes_2024_geo.csv")

st.title("Painel de Escolas de Regiões de SP")
st.caption("Adaptado do Censo Escolar 2024 (INEP)")

#Filtrar dados do arquivo
regiao = st.selectbox("Escolha a região", ["Todas", "Região Metropolitana de SP", "Baixada Santista", "Litoral Norte", "Vale do Ribeira"])
if regiao != "Todas":
    censo = censo[censo["regiao"]==regiao]
    
censo["porte"] = censo ["matriculas"].apply(classifica_porte)
porte = st.selectbox("Escolha o porte", ["Todas", "Pequena", "Média", "Grande"])
if porte != "Todas":
    censo = censo[censo["porte"]==porte]
    
dependencia = st.selectbox("Escolha a dependência",["Todas", "Municipal", "Estadual", "Federal", "Privada"])
if dependencia != "Todas":
    censo = censo [censo["dependencia"]==dependencia]
     
#MOntagem das contagens e soma
col1, col2 = st.columns (2)
col1.metric("Qtde de Escolas", len(censo))
col2.metric("Total de Matrículas", censo["matriculas"].sum())

#Gráfico da contagem de escolas por infra

st.subheader ("Escolas por porte")
st.bar_chart(censo["porte"].value_counts())

st.subheader ("Escolas por dependência")
st.bar_chart(censo["dependencia"].value_counts())

st.subheader ("Escolas por abastecimento de água")
st.bar_chart(censo["agua"].value_counts())

st.subheader("Escolas por coleta de lixo")
st.bar_chart(censo["lixo"].value_counts())

## Plotar as escolas no Mapa
st.subheader("Mapa das escolas")
st.map(censo[["latitude", "longitude"]])

#Exibir Lista de Escolas
st.subheader("Lista das escolas")
st.dataframe(censo[["regiao","municipio","escola","dependencia","matriculas", "porte"]])