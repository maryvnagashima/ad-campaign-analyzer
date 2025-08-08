import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ad Intelligence Dashboard", layout="wide")

st.title("📊 Ad Intelligence Dashboard")
st.markdown("Navegue pelas seções no menu lateral para visualizar diferentes análises de performance.")

# Menu lateral
menu = st.sidebar.radio("🔎 Selecione a análise:", [
    "Resumo Geral",
    "CAC por Criativo",
    "Desempenho de Criativos",
    "Canal & País",
    "Recomendações da IA"
])

if menu == "Resumo Geral":
    st.subheader("📈 Visão Geral de Performance")
    st.info("KPIs principais como ROAS, CPA e CAC médio aparecerão aqui.")

elif menu == "CAC por Criativo":
    st.subheader("🎯 CAC por Criativo")
    st.warning("Área dedicada a comparar desempenho por criativo com base em custo e conversões.")

elif menu == "Desempenho de Criativos":
    st.subheader("🎥 Análise de Criativos")
    st.warning("Explore os melhores criativos com base em CTR, engajamento e retorno.")

elif menu == "Canal & País":
    st.subheader("🌍 Análise por Canal e País")
    st.warning("Veja comparações de performance por canal (Google, Meta, TikTok) e por país.")

elif menu == "Recomendações da IA":
    st.subheader("🤖 Sugestões Estratégicas Automatizadas")
    st.success("Aqui entrarão insights automáticos gerados com base nos dados enviados.")
