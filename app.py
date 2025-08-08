# 1. Instalação forçada
import subprocess
import sys
import importlib

def install_and_import(package):
    try:
        importlib.import_module(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = importlib.import_module(package)

install_and_import('plotly')
install_and_import('pandas')
install_and_import('numpy')

# 2. Agora importe normalmente
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# 3. Resto do seu código (CSS, funções, etc)
# ===================================
# 🔮 ESTILO CSS COMPLETO (seu código)
# ===================================
def load_css():
    st.markdown(
        """
        <style>
        /* Dashboard Moderno - Estilos CSS Avançados */
        :root {
            --primary-color: #00FFFF;
            --secondary-color: #0080FF;
            --accent-color: #40E0D0;
            --success-color: #00FF80;
            --warning-color: #FFD700;
            --danger-color: #FF4444;
            --dark-bg: #0a0b1e;
            --dark-secondary: #1a1b3a;
            --glass-bg: rgba(255, 255, 255, 0.05);
            --border-glow: rgba(0, 255, 255, 0.3);
        }

        * { box-sizing: border-box; }

        .stApp {
            background: linear-gradient(135deg, var(--dark-bg) 0%, var(--dark-secondary) 100%);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
            min-height: 100vh;
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .metric-card, .glass-card {
            background: var(--glass-bg);
            border: 1px solid var(--border-glow);
            border-radius: 15px;
            padding: 20px;
            margin: 10px 0;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.1), inset 0 1px 1px rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .metric-card:hover, .glass-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 40px rgba(0, 255, 255, 0.2), inset 0 1px 1px rgba(255, 255, 255, 0.2);
            border-color: var(--primary-color);
        }

        .metric-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(0, 255, 255, 0.1), transparent);
            transform: rotate(45deg);
            animation: shine 3s linear infinite;
        }

        @keyframes shine {
            0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
            100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        }

        .metric-value {
            font-size: 2.5rem;
            font-weight: bold;
            color: var(--primary-color);
            text-shadow: 0 0 10px var(--primary-color), 0 0 20px var(--primary-color), 0 0 30px var(--primary-color);
            font-family: 'Orbitron', monospace;
            animation: glow 2s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { text-shadow: 0 0 10px var(--primary-color), 0 0 20px var(--primary-color), 0 0 30px var(--primary-color); }
            to { text-shadow: 0 0 20px var(--primary-color), 0 0 30px var(--primary-color), 0 0 40px var(--primary-color); }
        }

        .metric-label {
            font-size: 0.9rem;
            color: rgba(176, 176, 176, 0.8);
            margin-top: 5px;
            letter-spacing: 2px;
            text-transform: uppercase;
            font-weight: 600;
            font-family: 'Roboto Mono', monospace;
        }

        h1, h2, h3 {
            background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold;
            margin-bottom: 1rem;
        }

        .stButton > button {
            background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
            color: #000;
            border: none;
            border-radius: 10px;
            padding: 12px 24px;
            font-weight: bold;
            font-size: 1rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .stButton > button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s;
        }

        .stButton > button:hover::before {
            left: 100%;
        }

        .status-indicator {
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 8px;
            animation: pulse 2s infinite;
        }

        .status-online { background-color: var(--success-color); box-shadow: 0 0 10px var(--success-color); }
        .status-warning { background-color: var(--warning-color); box-shadow: 0 0 10px var(--warning-color); }
        .status-offline { background-color: var(--danger-color); box-shadow: 0 0 10px var(--danger-color); }

        @keyframes pulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 currentColor; }
            70% { transform: scale(1); box-shadow: 0 0 0 10px transparent; }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 transparent; }
        }

        .dashboard-title {
            font-size: 3rem;
            font-weight: 800;
            text-align: center;
            margin-bottom: 2rem;
            background: linear-gradient(45deg, var(--primary-color), var(--secondary-color), var(--accent-color));
            background-size: 300% 300%;
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientText 4s ease infinite;
        }

        @keyframes gradientText {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        .footer {
            background: var(--glass-bg);
            border-top: 1px solid var(--border-glow);
            backdrop-filter: blur(10px);
            padding: 20px;
            text-align: center;
            color: rgba(176, 176, 176, 0.8);
            font-size: 0.9rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# ===================================
# 📈 FUNÇÕES DE GRÁFICOS (seu código)
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
        font={'color': '#ffffff'}, xaxis={'gridcolor': 'rgba(255,255,255,0.1)', 'zerolinecolor': 'rgba(255,255,255,0.1)', 'color': '#ffffff'},
        yaxis={'gridcolor': 'rgba(255,255,255,0.1)', 'zerolinecolor': 'rgba(255,255,255,0.1)', 'color': '#ffffff'},
        height=250, margin=dict(l=20, r=20, t=40, b=20), showlegend=False
    )
    return fig

def create_metric_card(value, label, change=None, change_type="positive"):
    change_color = "var(--success-color)" if change_type == "positive" else "var(--danger-color)"
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
load_css()

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
    # Gerar dados simulados
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
    
    # Gráficos
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
st.markdown("<div class='footer'>💼 Projeto de portfólio | by [Seu Nome]</div>", unsafe_allow_html=True)
