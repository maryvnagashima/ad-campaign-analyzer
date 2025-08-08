import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import datetime
from datetime import datetime, timedelta
import random

# Configuração da página
st.set_page_config(
    page_title="CAC Optimization Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    """Carrega o CSS externo"""
    with open("style.css", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Chame no início do app
load_css()

# Função para gerar dados sintéticos para demo
@st.cache_data
def generate_demo_data():
    np.random.seed(42)
    
    # Dados de performance por canal
    channels = ['Google Ads', 'Facebook', 'Instagram', 'LinkedIn', 'TikTok']
    
    # Dados mensais
    months = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
    
    # Métricas principais
    metrics = {
        'total_campaigns': 1247,
        'total_spend': 2847593,
        'total_conversions': 48392,
        'avg_cac': 58.84,
        'optimized_cac': 41.19,
        'savings': 853477,
        'roi_improvement': 29.8
    }
    
    # Performance por canal
    channel_data = []
    for channel in channels:
        data = {
            'channel': channel,
            'spend': np.random.randint(300000, 800000),
            'conversions': np.random.randint(5000, 15000),
            'cac': np.random.uniform(35, 85),
            'ctr': np.random.uniform(0.015, 0.045),
            'quality_score': np.random.uniform(6.5, 9.2)
        }
        channel_data.append(data)
    
    channel_df = pd.DataFrame(channel_data)
    
    # Dados temporais
    daily_data = []
    for i in range(90):  # últimos 90 dias
        date = datetime.now() - timedelta(days=i)
        daily_data.append({
            'date': date,
            'spend': np.random.randint(15000, 35000),
            'conversions': np.random.randint(250, 600),
            'cac': np.random.uniform(45, 75),
            'impressions': np.random.randint(800000, 1500000)
        })
    
    daily_df = pd.DataFrame(daily_data).sort_values('date')
    
    return metrics, channel_df, daily_df

# Função para criar gráfico com tema escuro
def create_dark_theme_chart():
    layout = {
        'plot_bgcolor': 'rgba(0,0,0,0)',
        'paper_bgcolor': 'rgba(0,0,0,0)',
        'font': {'color': '#ffffff'},
        'xaxis': {
            'gridcolor': 'rgba(255,255,255,0.1)',
            'zerolinecolor': 'rgba(255,255,255,0.1)',
            'color': '#ffffff'
        },
        'yaxis': {
            'gridcolor': 'rgba(255,255,255,0.1)',
            'zerolinecolor': 'rgba(255,255,255,0.1)',
            'color': '#ffffff'
        }
    }
    return layout

# Header principal
st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
    <h1 style="font-size: 3rem; margin-bottom: 0;">🚀 CAC OPTIMIZATION AI</h1>
    <p style="font-size: 1.2rem; color: #B0B0B0;">Real-time Marketing Performance Dashboard</p>
</div>
""", unsafe_allow_html=True)

# Carregar dados
metrics, channel_df, daily_df = generate_demo_data()

# KPIs principais - Layout em 4 colunas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{metrics['total_campaigns']:,}</div>
        <div class="metric-label">TOTAL CAMPAIGNS</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">R$ {metrics['avg_cac']:.2f}</div>
        <div class="metric-label">CURRENT CAC</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">R$ {metrics['optimized_cac']:.2f}</div>
        <div class="metric-label">OPTIMIZED CAC</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{metrics['roi_improvement']:.1f}%</div>
        <div class="metric-label">ROI IMPROVEMENT</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Layout principal em 2 colunas
left_col, right_col = st.columns([2, 1])

with left_col:
    # Gráfico principal - CAC Evolution
    fig_main = go.Figure()
    
    # Linha principal com glow effect
    fig_main.add_trace(go.Scatter(
        x=daily_df['date'],
        y=daily_df['cac'],
        mode='lines',
        name='CAC Atual',
        line=dict(color='#00FFFF', width=3),
        fill='tonexty'
    ))
    
    # Linha otimizada
    optimized_cac = daily_df['cac'] * 0.7  # 30% de redução
    fig_main.add_trace(go.Scatter(
        x=daily_df['date'],
        y=optimized_cac,
        mode='lines',
        name='CAC Otimizado',
        line=dict(color='#00FF80', width=3, dash='dash'),
        fill='tonexty'
    ))
    
    fig_main.update_layout(
        title={
            'text': "📈 CAC Evolution - Last 90 Days",
            'x': 0.02,
            'font': {'size': 20, 'color': '#00FFFF'}
        },
        **create_dark_theme_chart(),
        height=400,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color='#ffffff')
        )
    )
    
    st.plotly_chart(fig_main, use_container_width=True)

with right_col:
    # Performance por canal - Donut chart
    fig_donut = go.Figure(data=[go.Pie(
        labels=channel_df['channel'],
        values=channel_df['spend'],
        hole=0.6,
        marker=dict(
            colors=['#00FFFF', '#0080FF', '#40E0D0', '#00CED1', '#20B2AA'],
            line=dict(color='#000000', width=2)
        ),
        textinfo='label+percent',
        textfont=dict(color='#ffffff')
    )])
    
    fig_donut.update_layout(
        title={
            'text': "💰 Spend by Channel",
            'x': 0.5,
            'font': {'size': 16, 'color': '#00FFFF'}
        },
        **create_dark_theme_chart(),
        height=300,
        showlegend=False,
        annotations=[dict(text='SPEND', x=0.5, y=0.5, font_size=20, showarrow=False, font_color='#00FFFF')]
    )
    
    st.plotly_chart(fig_donut, use_container_width=True)
    
    # Mini métricas
    st.markdown(f"""
    <div style="background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 10px; margin-top: 1rem;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
            <span style="color: #B0B0B0;">Total Spend:</span>
            <span style="color: #00FFFF; font-weight: bold;">R$ {metrics['total_spend']:,}</span>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
            <span style="color: #B0B0B0;">Conversions:</span>
            <span style="color: #00FFFF; font-weight: bold;">{metrics['total_conversions']:,}</span>
        </div>
        <div style="display: flex; justify-content: space-between;">
            <span style="color: #B0B0B0;">Savings:</span>
            <span style="color: #00FF80; font-weight: bold;">R$ {metrics['savings']:,}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Segunda linha de gráficos
col1, col2, col3 = st.columns(3)

with col1:
    # Bar chart - CAC por canal
    fig_bar = go.Figure(data=[
        go.Bar(
            x=channel_df['channel'],
            y=channel_df['cac'],
            marker=dict(
                color='#00FFFF',
                line=dict(color='#ffffff', width=1)
            ),
            text=[f'R$ {x:.1f}' for x in channel_df['cac']],
            textposition='outside'
        )
    ])
    
    fig_bar.update_layout(
        title={
            'text': "📊 CAC by Channel",
            'font': {'size': 16, 'color': '#00FFFF'}
        },
        **create_dark_theme_chart(),
        height=300,
        xaxis_tickangle=-45
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    # Conversion rate scatter
    fig_scatter = go.Figure(data=[
        go.Scatter(
            x=channel_df['cac'],
            y=channel_df['ctr'],
            mode='markers+text',
            marker=dict(
                size=[x/1000 for x in channel_df['spend']],
                color='#00FFFF',
                opacity=0.7,
                line=dict(width=2, color='#ffffff')
            ),
            text=channel_df['channel'],
            textposition="top center",
            textfont=dict(color='#ffffff')
        )
    ])
    
    fig_scatter.update_layout(
        title={
            'text': "🎯 CAC vs CTR",
            'font': {'size': 16, 'color': '#00FFFF'}
        },
        **create_dark_theme_chart(),
        height=300,
        xaxis_title="CAC (R$)",
        yaxis_title="CTR (%)"
    )
    
    st.plotly_chart(fig_scatter, use_container_width=True)

with col3:
    # Quality Score gauge
    avg_quality = channel_df['quality_score'].mean()
    
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=avg_quality,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "⭐ Avg Quality Score", 'font': {'color': '#00FFFF'}},
        delta={'reference': 8.0, 'increasing': {'color': '#00FF80'}, 'decreasing': {'color': '#FF4444'}},
        gauge={
            'axis': {'range': [None, 10], 'tickcolor': '#ffffff'},
            'bar': {'color': "#00FFFF"},
            'steps': [
                {'range': [0, 5], 'color': "rgba(255, 68, 68, 0.3)"},
                {'range': [5, 7], 'color': "rgba(255, 255, 0, 0.3)"},
                {'range': [7, 10], 'color': "rgba(0, 255, 128, 0.3)"}
            ],
            'threshold': {
                'line': {'color': "white", 'width': 4},
                'thickness': 0.75,
                'value': 8.5
            }
        }
    ))
    
    fig_gauge.update_layout(
        **create_dark_theme_chart(),
        height=300,
        font={'color': '#ffffff'}
    )
    
    st.plotly_chart(fig_gauge, use_container_width=True)

# Footer com controles
st.markdown("<br><br>", unsafe_allow_html=True)

# Controles interativos
with st.container():
    st.markdown("### 🎛️ Optimization Controls")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        budget_multiplier = st.slider("Budget Allocation", 0.5, 2.0, 1.0, 0.1)
    
    with col2:
        target_cac = st.number_input("Target CAC (R$)", min_value=20.0, max_value=100.0, value=45.0, step=5.0)
    
    with col3:
        optimization_mode = st.selectbox("Optimization Mode", ["Conservative", "Balanced", "Aggressive"])
    
    with col4:
        if st.button("🚀 Run Optimization", type="primary"):
            st.success(f"✅ Optimization completed! Projected CAC reduction: {np.random.uniform(15, 35):.1f}%")

# Rodapé
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666666; font-size: 0.9rem;">
    CAC Optimization Dashboard | Powered by AI & Machine Learning
</div>
""", unsafe_allow_html=True)
