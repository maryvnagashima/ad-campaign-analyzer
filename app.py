import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Ad Campaign Analyzer", layout="wide")

st.title("📈 Ad Campaign Analyzer")
st.markdown("Faça upload do seu arquivo CSV de campanha (Google Ads, Meta, TikTok). O app analisará os dados e apresentará insights acionáveis.")

uploaded_file = st.file_uploader("📤 Upload do arquivo CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("👀 Pré-visualização dos dados")
    st.dataframe(df.head())

    expected_cols = ["Canal", "País", "Impressões", "Cliques", "Custo", "Conversões", "Receita"]

    if all(col in df.columns for col in expected_cols):
        df["CPC"] = (df["Custo"] / df["Cliques"]).round(2)
        df["CPA"] = (df["Custo"] / df["Conversões"]).round(2)
        df["ROAS"] = (df["Receita"] / df["Custo"]).round(2)

        st.markdown("---")
        st.subheader("📊 Métricas Calculadas por Canal e País")
        st.dataframe(df[["Canal", "País", "CPC", "CPA", "ROAS"]])

        st.markdown("---")
        st.subheader("📍 ROAS Médio por Canal")
        roas_canal = df.groupby("Canal")["ROAS"].mean().sort_values(ascending=False)
        st.bar_chart(roas_canal)

        st.subheader("📍 CPA Médio por País")
        cpa_pais = df.groupby("País")["CPA"].mean().sort_values()
        st.bar_chart(cpa_pais)

        st.markdown("---")
        st.subheader("🧠 Sugestões Estratégicas")

        melhor_roas = roas_canal.idxmax()
        st.success(f"📌 Canal com melhor ROAS médio: **{melhor_roas}**")

        if df["CPA"].mean() > 10:
            st.warning("🔍 CPA médio está acima de 10. Avalie estratégias de segmentação ou oferta.")
        if df["ROAS"].mean() < 3:
            st.error("⚠️ ROAS médio abaixo do ideal. Revise posicionamento ou mix de canais.")
        else:
            st.info("✅ Sua média de ROAS está saudável!")

        st.markdown("---")
        st.caption("Versão de demonstração – Marina V. Nagashima | Powered by Streamlit")

    else:
        st.error(f"O CSV precisa conter as colunas: {', '.join(expected_cols)}")
else:
    st.info("Envie um arquivo CSV com dados de campanha para iniciar a análise.")
