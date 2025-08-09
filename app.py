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
# 📁 UPLOAD DE ARQUIVO (com limite de 3MB)
# ===================================
st.sidebar.markdown("<h3 style='color: #00FFFF;'>🔼 Upload de Dados</h3>", unsafe_allow_html=True)

MAX_FILE_SIZE = 3 * 1024 * 1024  # 3MB

uploaded_file = st.sidebar.file_uploader(
    "Carregue seu CSV (máx. 3MB)",
    type=["csv"],
    help="Arquivos maiores que 3MB serão rejeitados"
)

if uploaded_file is not None:
    if uploaded_file.size > MAX_FILE_SIZE:
        st.sidebar.error("❌ Arquivo muito grande! O limite é 3MB.")
        st.stop()
    try:
        df = pd.read_csv(uploaded_file)
        st.sidebar.success(f"✅ Dados carregados! ({uploaded_file.size // 1024} KB)")
    except Exception as e:
        st.sidebar.error(f"❌ Erro ao ler o CSV: {e}")
        st.stop()
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
# 🧭 ABAS HORIZONTAIS
# ===================================
tabs = st.tabs([
    "🏠 Home / Resumo Geral",
    "🎯 CAC por Criativo",
    "🎥 Desempenho de Criativos",
    "📈 Canal & País",
    "🧠 Sugestões da IA"
])

# === 1. HOME ===
with tabs[0]:
    st.markdown("<h2 class='dashboard-title'>Resumo Geral</h2>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(create_metric_card("28%", "ROAS", "5.2", "positive"), unsafe_allow_html=True)
    with col2:
        st.markdown(create_metric_card("R$ 180", "CAC", "15.3", "positive"), unsafe_allow_html=True)
    with col3:
        st.markdown(create_metric_card("48k", "CONVERSÕES", "8.7", "positive"), unsafe_allow_html=True)
    with col4:
        st.markdown(create_metric_card("3.2x", "ROI", "4.1", "positive"), unsafe_allow_html=True)
    
    line_data = {'x': list(range(30)), 'y': [20 + 10*np.sin(x/5) + np.random.normal(0, 2) for x in range(30)]}
    st.plotly_chart(create_neon_line_chart(line_data, "📈 Evolução do ROAS"), use_container_width=True)

# === 2. CAC POR CRIATIVO ===
with tabs[1]:
    st.markdown("<h2 class='dashboard-title'>CAC por Criativo</h2>", unsafe_allow_html=True)
    
    df['cac'] = df['custo_total'] / df['conversoes'].replace(0, 1)
    cac_por_criativo = df.groupby(['tipo_criativo', 'cta'])['cac'].mean().reset_index()
    
    st.dataframe(cac_por_criativo.style.format({"cac": "R$ {:.2f}"}))
    
    fig = px.bar(cac_por_criativo, x='tipo_criativo', y='cac', color='cta', title="CAC por Tipo de Criativo")
    fig.update_traces(marker=dict(line=dict(width=1, color='white')))
    st.plotly_chart(fig, use_container_width=True)

# === 3. DESEMPENHO DE CRIATIVOS ===
with tabs[2]:
    st.markdown("<h2 class='dashboard-title'>Desempenho de Criativos</h2>", unsafe_allow_html=True)

    st.subheader("🖼️ Pré-visualização de Criativos")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://via.placeholder.com/150/00FFFF/000000?text=Video+Short", caption="Vídeo curto - Pessoa sorrindo")
        st.markdown("**CTR:** 3.2% | **CPA:** R$ 58")
    with col2:
        st.image("https://via.placeholder.com/150/0080FF/FFFFFF?text=Carrossel", caption="Carrossel - Antes/Depois")
        st.markdown("**CTR:** 2.8% | **CPA:** R$ 65")
    with col3:
        st.image("https://via.placeholder.com/150/40E0D0/000000?text=Imagem+Unica", caption="Imagem única - Produto")
        st.markdown("**CTR:** 1.9% | **CPA:** R$ 89")

    st.subheader("📊 CTR por Tipo de Criativo")
    ctr_data = df.groupby('tipo_criativo')['cliques'].sum() / df.groupby('tipo_criativo')['impressoes'].sum()
    fig_ctr = px.bar(ctr_data, title="CTR por Tipo de Criativo", color_discrete_sequence=['#00FFFF'])
    fig_ctr.update_traces(marker=dict(line=dict(width=1, color='white')))
    st.plotly_chart(fig_ctr, use_container_width=True)

# === 4. CANAL & PAÍS ===
with tabs[3]:
    st.markdown("<h2 class='dashboard-title'>Desempenho por Canal e País</h2>", unsafe_allow_html=True)

    st.subheader("🌍 ROAS por País")
    roas_por_pais = {
        'Brasil': 2.8,
        'EUA': 3.2,
        'Alemanha': 2.5,
        'França': 2.1,
        'Canadá': 3.0
    }
    pais_df = pd.DataFrame(list(roas_por_pais.items()), columns=['País', 'ROAS'])
    fig_pais = px.bar(pais_df, x='País', y='ROAS', title="ROAS por País", color='ROAS', color_continuous_scale='Blues')
    st.plotly_chart(fig_pais, use_container_width=True)

    st.subheader("🌎 Mapa de Desempenho por País")
    mapa_data = pd.DataFrame({
        'country': ['Brazil', 'United States', 'Germany', 'France', 'Canada', 'UK', 'Japan'],
        'conversions': [4500, 6200, 3100, 2800, 3800, 4100, 2900],
        'roas': [2.8, 3.2, 2.5, 2.1, 3.0, 3.1, 2.3],
        'clicks': [45000, 62000, 31000, 28000, 38000, 41000, 29000]
    })

    # ✅ Corrigido: título no px.choropleth, sem update_layout problemático
    fig_mapa = px.choropleth(
        mapa_data,
        locations='country',
        locationmode='country names',
        color='roas',
        hover_name='country',
        hover_data={'conversions': True, 'clicks': True, 'roas': ':.2f'},
        color_continuous_scale='deep',
        range_color=[1.5, 3.5],
        title="ROAS por País",  # ✅ Título aqui, não no update_layout
        labels={'roas': 'ROAS'}
    )

    # ✅ Apenas configurações seguras no update_layout
    fig_mapa.update_layout(
        font=dict(color='#ffffff'),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='natural earth',
            bgcolor='rgba(0,0,0,0)',
            landcolor='rgba(30, 30, 50, 0.8)',
            showcountries=True,
            countrycolor='rgba(255, 255, 255, 0.1)'
        ),
        coloraxis_colorbar=dict(
            title="ROAS",
            titlefont=dict(color='#00FFFF'),
            tickfont=dict(color='#ffffff'),
            bgcolor='rgba(0,0,0,0)'
        )
    )

    st.plotly_chart(fig_mapa, use_container_width=True)

# === 5. SUGESTÕES DA IA ===
with tabs[4]:
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
    
    st.markdown("""
    <div class='glass-card'>
        <h3>💡 Insights da IA</h3>
        <p>• Criativos com <strong>imagem de pessoa sorrindo</strong> têm CTR 40% maior</p>
        <p>• Formato <strong>vídeo curto</strong> no TikTok converte 2x mais</p>
        <p>• Melhor horário: <strong>segundas entre 18h-20h</strong></p>
    </div>
    """, unsafe_allow_html=True)

# ===================================
# 📦 RODAPÉ
# ===================================
st.markdown("<div class='footer'>💼 Projeto de portfólio | by Marina Vieira Nagashima</div>", unsafe_allow_html=True)
