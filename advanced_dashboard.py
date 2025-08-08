import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def create_neon_line_chart(data, title="Performance Trend"):
    """Cria gráfico de linha com efeito neon similar à imagem"""
    
    fig = go.Figure()
    
    # Linha principal com efeito neon
    fig.add_trace(go.Scatter(
        x=data['x'],
        y=data['y'],
        mode='lines',
        name='Main Trend',
        line=dict(
            color='#00FFFF',
            width=3,
            shape='spline'
        ),
        fill='tonexty',
        fillcolor='rgba(0, 255, 255, 0.1)'
    ))
    
    # Área de fundo preenchida
    fig.add_trace(go.Scatter(
        x=data['x'],
        y=[0] * len(data['x']),
        mode='lines',
        line=dict(color='rgba(0,0,0,0)'),
        fill='tonexty',
        fillcolor='rgba(0, 255, 255, 0.05)',
        showlegend=False
    ))
    
    fig.update_layout(
        title={
            'text': title,
            'font': {'size': 16, 'color': '#00FFFF'},
            'x': 0.02
        },
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': '#ffffff'},
        xaxis={
            'gridcolor': 'rgba(255,255,255,0.1)',
            'zerolinecolor': 'rgba(255,255,255,0.1)',
            'color': '#ffffff',
            'showgrid': True
        },
        yaxis={
            'gridcolor': 'rgba(255,255,255,0.1)',
            'zerolinecolor': 'rgba(255,255,255,0.1)',
            'color': '#ffffff',
            'showgrid': True
        },
        height=250,
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=False
    )
    
    return fig

def create_circular_progress(value, max_value, title, color='#00FFFF'):
    """Cria indicador circular como na imagem"""
    
    percentage = (value / max_value) * 100
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title, 'font': {'size': 14, 'color': '#ffffff'}},
        number={'font': {'size': 24, 'color': color}},
        gauge={
            'axis': {'range': [None, max_value], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': color, 'thickness': 0.3},
            'bgcolor': "rgba(255,255,255,0.1)",
            'borderwidth': 2,
            'bordercolor': "rgba(255,255,255,0.2)",
            'steps': [
                {'range': [0, max_value], 'color': "rgba(255,255,255,0.05)"}
            ],
        },
        domain={'x': [0, 1], 'y': [0, 1]}
    ))
    
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={'color': "white"},
        height=200,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    return fig

def create_bar_chart_vertical(data, title="Performance by Category"):
    """Cria gráfico de barras vertical com estilo neon"""
    
    fig = go.Figure(data=[
        go.Bar(
            x=data['categories'],
            y=data['values'],
            marker=dict(
                color=['#00FFFF', '#0080FF', '#40E0D0', '#20B2AA', '#48D1CC'],
                line=dict(color='#ffffff', width=1)
            ),
            text=[f'{x:.0f}' for x in data['values']],
            textposition='outside',
            textfont=dict(color='#ffffff')
        )
    ])
    
    fig.update_layout(
        title={
            'text': title,
            'font': {'size': 16, 'color': '#00FFFF'},
            'x': 0.02
        },
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': '#ffffff'},
        xaxis={
            'gridcolor': 'rgba(255,255,255,0.1)',
            'color': '#ffffff',
            'showgrid': False
        },
        yaxis={
            'gridcolor': 'rgba(255,255,255,0.1)',
            'color': '#ffffff',
            'showgrid': True
        },
        height=250,
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=False
    )
    
    return fig

def create_heatmap_calendar(data, title="Activity Heatmap"):
    """Cria heatmap de calendário como na imagem"""
    
    # Simular dados de calendário
    days = ['S', 'M', 'T', 'W', 'T', 'F', 'S']
    weeks = 6
    
    # Gerar matriz de dados
    calendar_data = np.random.randint(0, 100, size=(weeks, 7))
    
    fig = go.Figure(data=go.Heatmap(
        z=calendar_data,
        x=days,
        y=[f'W{i+1}' for i in range(weeks)],
        colorscale=[[0, 'rgba(0,0,0,0.1)'], [0.5, 'rgba(0,255,255,0.3)'], [1, '#00FFFF']],
        showscale=False,
        hoverongaps=False
    ))
    
    fig.update_layout(
        title={
            'text': title,
            'font': {'size': 14, 'color': '#00FFFF'},
            'x': 0.02
        },
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': '#ffffff'},
        xaxis={'color': '#ffffff', 'showgrid': False},
        yaxis={'color': '#ffffff', 'showgrid': False},
        height=180,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    return fig

def create_scatter_plot(data, title="Correlation Analysis"):
    """Cria scatter plot com efeito neon"""
    
    fig = go.Figure(data=go.Scatter(
        x=data['x'],
        y=data['y'],
        mode='markers',
        marker=dict(
            size=data.get('size', [10] * len(data['x'])),
            color='#00FFFF',
            opacity=0.7,
            line=dict(width=2, color='#ffffff'),
            sizemode='diameter',
            sizeref=2.*max(data.get('size', [10]))/40.**2
        ),
        text=data.get('labels', [f'Point {i}' for i in range(len(data['x']))]),
        textposition="top center",
        textfont=dict(color='#ffffff')
    ))
    
    fig.update_layout(
        title={
            'text': title,
            'font': {'size': 16, 'color': '#00FFFF'},
            'x': 0.02
        },
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': '#ffffff'},
        xaxis={
            'gridcolor': 'rgba(255,255,255,0.1)',
            'color': '#ffffff',
            'showgrid': True
        },
        yaxis={
            'gridcolor': 'rgba(255,255,255,0.1)',
            'color': '#ffffff',
            'showgrid': True
        },
        height=250,
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=False
    )
    
    return fig

def create_metric_card_html(value, label, change=None, change_type="positive"):
    """Cria card de métrica personalizado em HTML"""
    
    change_color = "#00FF80" if change_type == "positive" else "#FF4444"
    change_icon = "▲" if change_type == "positive" else "▼"
    change_html = f"""
        <div style="color: {change_color}; font-size: 0.9rem; margin-top: 5px;">
            {change_icon} {change}%
        </div>
    """ if change else ""
    
    return f"""
    <div style="
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 255, 255, 0.3);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        backdrop-filter: blur(20px);
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.1);
        transition: all 0.3s ease;
        margin: 10px 0;
    ">
        <div style="
            font-size: 2.2rem;
            font-weight: bold;
            color: #00FFFF;
            text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
            font-family: 'Orbitron', monospace;
        ">{value}</div>
        <div style="
            font-size: 0.9rem;
            color: rgba(176, 176, 176, 0.8);
            margin-top: 5px;
            letter-spacing: 2px;
            text-transform: uppercase;
            font-weight: 600;
        ">{label}</div>
        {change_html}
    </div>
    """

def create_status_indicator(status, label):
    """Cria indicador de status com cores"""
    
    colors = {
        'online': '#00FF80',
        'warning': '#FFD700', 
        'offline': '#FF4444',
        'active': '#00FFFF'
    }
    
    color = colors.get(status, '#00FFFF')
    
    return f"""
    <div style="display: flex; align-items: center; margin: 10px 0;">
        <div style="
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background-color: {color};
            box-shadow: 0 0 10px {color};
            margin-right: 10px;
            animation: pulse 2s infinite;
        "></div>
        <span style="color: #ffffff; font-size: 0.9rem;">{label}</span>
    </div>
    """

def create_mini_sparkline(data, color='#00FFFF'):
    """Cria mini gráfico sparkline"""
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=list(range(len(data))),
        y=data,
        mode='lines',
        line=dict(color=color, width=2),
        fill='tonexty',
        fillcolor=f'rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.1)'
    ))
    
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis={'visible': False},
        yaxis={'visible': False},
        height=60,
        margin=dict(l=0, r=0, t=0, b=0)
    )
    
    return fig

def create_donut_chart_with_center_text(data, center_text, title):
    """Cria gráfico donut com texto central"""
    
    fig = go.Figure(data=[go.Pie(
        labels=data['labels'],
        values=data['values'],
        hole=0.6,
        marker=dict(
            colors=['#00FFFF', '#0080FF', '#40E0D0', '#20B2AA', '#48D1CC'],
            line=dict(color='#000000', width=2)
        ),
        textinfo='percent',
        textfont=dict(color='#ffffff', size=12),
        hovertemplate='<b>%{label}</b><br>Value: %{value}<br>Percent: %{percent}<extra></extra>'
    )])
    
    fig.update_layout(
        title={
            'text': title,
            'font': {'size': 16, 'color': '#00FFFF'},
            'x': 0.5,
            'xanchor': 'center'
        },
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': '#ffffff'},
        height=300,
        showlegend=False,
        annotations=[dict(
            text=center_text,
            x=0.5, y=0.5,
            font=dict(size=20, color='#00FFFF'),
            showarrow=False
        )]
    )
    
    return fig

# Função principal para demonstrar todos os componentes
def show_advanced_dashboard():
    """Demonstra todos os componentes avançados"""
    
    st.markdown("## 🎨 Advanced Dashboard Components")
    
    # Dados de exemplo
    line_data = {
        'x': list(range(30)),
        'y': [20 + 10*np.sin(x/5) + np.random.normal(0, 2) for x in range(30)]
    }
    
    bar_data = {
        'categories': ['CAT A', 'CAT B', 'CAT C', 'CAT D', 'CAT E'],
        'values': [450, 320, 280, 180, 120]
    }
    
    scatter_data = {
        'x': np.random.uniform(0, 100, 15),
        'y': np.random.uniform(0, 100, 15),
        'size': np.random.uniform(10, 30, 15),
        'labels': [f'Point {i+1}' for i in range(15)]
    }
    
    donut_data = {
        'labels': ['Google Ads', 'Facebook', 'Instagram', 'LinkedIn', 'TikTok'],
        'values': [35, 25, 20, 15, 5]
    }
    
    # Layout em colunas
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.plotly_chart(create_neon_line_chart(line_data, "📈 Performance Trend"), 
                       use_container_width=True)
    
    with col2:
        st.plotly_chart(create_circular_progress(78, 100, "🎯 Goal", "#00FFFF"), 
                       use_container_width=True)
    
    with col3:
        st.plotly_chart(create_heatmap_calendar({}, "📅 Activity"), 
                       use_container_width=True)
    
    # Segunda linha
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_bar_chart_vertical(bar_data, "📊 Categories"), 
                       use_container_width=True)
    
    with col2:
        st.plotly_chart(create_scatter_plot(scatter_data, "🔍 Correlation"), 
                       use_container_width=True)
    
    # Cards de métricas personalizados
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(create_metric_card_html("1,247", "CAMPAIGNS", "12.5", "positive"), 
                   unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_metric_card_html("R$ 58.84", "AVG CAC", "-15.3", "positive"), 
                   unsafe_allow_html=True)
    
    with col3:
        st.markdown(create_metric_card_html("48,392", "CONVERSIONS", "8.7", "positive"), 
                   unsafe_allow_html=True)
    
    with col4:
        st.markdown(create_metric_card_html("29.8%", "ROI BOOST", "5.2", "positive"), 
                   unsafe_allow_html=True)

if __name__ == "__main__":
    show_advanced_dashboard()
