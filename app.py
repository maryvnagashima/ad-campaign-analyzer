# app.py
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import os

# ===================================
# 🎨 CARREGAR CSS EXTERNO
# ===================================
def load_css():
    """Carrega o arquivo style.css"""
    css_path = "style.css"
    if os.path.exists(css_path):
        with open(css_path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Arquivo style.css não encontrado. O estilo não será aplicado.")

# Carregar o CSS
load_css()

# ===================================
# 📈 FUNÇÕES DE GRÁFICOS
# ===================================
def create_neon_line_chart(data, title="Performance Trend"):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data['x'], y=data['y'], mode='lines', name='Main Trend',
        line=dict(color='#00FFFF', width=3, shape='spline'),
        fill='tonexty', fillcolor='rgba(0, 255, 255, 0.1)'
    ))
    fig.add_trace(go.Scatter(
        x=data['x'], y=[0]*len(data['x']), mode='lines', line=dict(color='rgba(0,0,0,0)'),
        fill='tonexty', fillcolor='rgba(0, 255, 255, 0.05)', showlegend=False
    ))
    fig.update_layout(
        title={'text': title, 'font': {'size': 16, 'color': '#00FFFF'}, 'x': 0.02},
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        font={'color': '#ffffff'}, 
        xaxis={'gridcolor': 'rgba(255,255,255,0.1)', 'zerolinecolor': 'rgba(255,255,255,0.1)', 'color': '#ffffff'},
        yaxis={'gridcolor': 'rgba(255,255,255,0.1)', 'zerolinecolor': 'rgba(255,255,255,0.1)', 'color': '#ffffff'},
        height=250, margin=dict(l=20, r=20, t=40, b=20), showlegend=False
    )
    return fig

def create_metric_card(value, label, change=None, change_type="positive"):
    change_color = "#00FF80" if change_type == "positive" else "#FF4444"
    change_icon = "▲" if change_type == "positive" else "▼"
    change_html = f"<div style='color: {change_color}; margin-top: 5px;'>{change_icon} {change}%</div>" if change else ""
    return f"""
    <div class="metric-card">
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
        {change_html}
    </div>
    """

# ===================================
# 🚀 CONFIGURAÇÃO INICIAL
# ===================================
st.set_page_config(page_title="AI de Criativos", layout="wide")

# ===================================
# 📁 UPLOAD DE ARQUIVO
# ===================================
st.sidebar.markdown("<h3 style='color: #00FFFF;'>🔼 Upload de Dados</h3>", unsafe_allow_html=True)
uploaded_file = st.sidebar.file_uploader("Carregue seu CSV", type=["csv"])

# Dados simulados (se não houver upload)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("✅ Dados carregados!")
else:
    np.random.seed(42)
    tipos = ["imagem única", "carrossel", "vídeo curto"]
    imagens = ["pessoa sorrindo", "produto", "antes/depois"]
    ctas = ["Compre agora", "Saiba mais", "Comece grátis", "Experimente"]
    canais = ["Meta Ads", "Google Ads", "TikTok Ads"]
    
    data = []
    for i in range(300):
        tipo = np.random.choice(tipos)
        imagem = np.random.choice(imagens)
        cta = np.random.choice(ctas)
        canal = np.random.choice(canais)
        impressoes = np.random.randint(1000, 50000)
        cliques = np.random.binomial(impressoes, 0.02)
        leads = np.random.binomial(cliques, 0.1)
        conversoes = np.random.binomial(leads, 0.05)
        custo = np.random.uniform(500, 5000)
        
        if imagem == "pessoa sorrindo" and cta == "Comece grátis":
            conversoes = int(conversoes * 1.8)
        if tipo == "vídeo curto" and canal == "TikTok Ads":
            conversoes = int(conversoes * 2.0)
            
        data.append({
            'canal': canal,
            'tipo_criativo': tipo,
            'imagem_tipo': imagem,
            'cta': cta,
            'impressoes': impressoes,
            'cliques': cliques,
            'leads': leads,
            'conversoes': conversoes,
            'custo_total': custo
        })
    df = pd.DataFrame(data)

# ===================================
# 🧭 MENU LATERAL
# ===================================
menu = st.sidebar.selectbox("Navegação", [
    "🏠 Home / Resumo Geral",
    "🎯 CAC por Criativo",
    "🎥 Desempenho de Criativos",
    "📈 Canal & País",
    "🧠 Sugestões da IA"
])

# ===================================
# 🏠 HOME
# ===================================
if menu == "🏠 Home / Resumo Geral":
    st.markdown("<h1 class='dashboard-title'>AI de Otimização de Criativos</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #aaa;'>Descubra os melhores criativos com inteligência artificial</p>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(create_metric_card("28%", "ROAS", "5.2", "positive"), unsafe_allow_html=True)
    with col2:
        st.markdown(create_metric_card("R$ 180", "CAC", "15.3", "positive"), unsafe_allow_html=True)
    with col3:
        st.markdown(create_metric_card("48k", "CONVERSÕES", "8.7", "positive"), unsafe_allow_html=True)
    with col4:
        st.markdown(create_metric_card("3.2x", "ROI", "4.1", "positive"), unsafe_allow_html=True)
    
    # Gráfico de linha neon
    line_data = {'x': list(range(30)), 'y': [20 + 10*np.sin(x/5) + np.random.normal(0, 2) for x in range(30)]}
    st.plotly_chart(create_neon_line_chart(line_data, "📈 Evolução do ROAS"), use_container_width=True)

# ===================================
# 🎯 CAC por Criativo
# ===================================
elif menu == "🎯 CAC por Criativo":
    st.markdown("<h2 class='dashboard-title'>CAC por Criativo</h2>", unsafe_allow_html=True)
    
    df['cac'] = df['custo_total'] / df['conversoes'].replace(0, 1)
    cac_por_criativo = df.groupby(['tipo_criativo', 'cta'])['cac'].mean().reset_index()
    
    st.dataframe(cac_por_criativo.style.format({"cac": "R$ {:.2f}"}))
    
    fig = px.bar(cac_por_criativo, x='tipo_criativo', y='cac', color='cta', title="CAC por Tipo de Criativo")
    fig.update_traces(marker=dict(line=dict(width=1, color='white')))
    st.plotly_chart(fig, use_container_width=True)

# ===================================
# 🧠 Sugestões da IA
# ===================================
elif menu == "🧠 Sugestões da IA":
    st.markdown("<h2 class='dashboard-title'>Sugestões da IA</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='glass-card'>
        <h3>🎯 Recomendações Automáticas</h3>
        <p><span class='status-indicator status-online'></span> <strong>Brasil:</strong> Reduzir TikTok Ads em 20%</p>
        <p><span class='status-indicator status-warning'></span> <strong>EUA:</strong> Aumentar Google Ads em 15%</p>
        <p><span class='status-indicator status-online'></span> <strong>Alemanha:</strong> Manter orçamento atual</p>
        <p><span class='status-indicator status-warning'></span> <strong>CTA ideal:</strong> 'Comece grátis' converte 68% mais</p>
    </div>
    """, unsafe_allow_html=True)

# ===================================
# 📦 RODAPÉ
# ===================================
st.markdown("---")
st.markdown("💼 Projeto de portfólio por Marina vieira Nagashima | GitHub: https://github.com/maryvnagashima/")
