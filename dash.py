import streamlit as st
import pandas as pd
import plotly.express as px

# Carregando os dados
df = pd.read_csv("oficial_base.csv")

# Titulo da página do dash
st.set_page_config(
    page_title="Dashbord de Reserva de Petróleo",
    page_icon="📊",
    layout="wide",
)   

# Titulo principal
st.title("Análise de Dados das Reservas Mundiais de Petróleo")

# Barra lateral
st.sidebar.header("🔍 Filtros")

# Filtro de ano
anos_disponiveis = sorted(df['ANO'].unique())
anos_selecionados = st.sidebar.selectbox('Ano', anos_disponiveis, index=None, placeholder='Selecione um ano')

if anos_selecionados is None:
    st.info("👈 Selecione um ano para começar a análise")
    st.stop()

# Filtro de bloco
tipo_bloco = sorted(df['BLOCO'].unique())
bloco_selecionados = st.sidebar.multiselect('Tipo de Bloco', tipo_bloco, default=[])

# Filtro das regiões geográficas
if bloco_selecionados:
    regioes_disponiveis = sorted(
        df[df['BLOCO'].isin(bloco_selecionados)]['REGIÃO GEOGRÁFICA'].unique()
    )
else:
    regioes_disponiveis = sorted(df['REGIÃO GEOGRÁFICA'].unique())
regioes_selecionadas = st.sidebar.multiselect('Região Geográfica', regioes_disponiveis, default=[])

# Filtro dos países
if regioes_selecionadas:
    paises_disponiveis = sorted(
        df[df['REGIÃO GEOGRÁFICA'].isin(regioes_selecionadas)]['PAÍS'].unique()
    )
else:
    paises_disponiveis = sorted(df['PAÍS'].unique())
paises_selecionados = st.sidebar.multiselect('Países', paises_disponiveis, default=[])

# Atualiza os dados conforme as escolhas dos filtros
df_atualizado = df.copy()

if bloco_selecionados:
    df_atualizado = df_atualizado[df_atualizado['BLOCO'].isin(bloco_selecionados)]

if anos_selecionados:
    df_atualizado = df_atualizado[df_atualizado['ANO'] == anos_selecionados]

if regioes_selecionadas:
    df_atualizado = df_atualizado[df_atualizado['REGIÃO GEOGRÁFICA'].isin(regioes_selecionadas)]

if paises_selecionados:
    df_atualizado = df_atualizado[df_atualizado['PAÍS'].isin(paises_selecionados)]

if anos_selecionados:
    titulo_anos = str(anos_selecionados)
else:
    titulo_anos = ""

# KPIs
st.subheader("Métricas gerais")

if not df_atualizado.empty:
    qntd_reserva_mundial = df_atualizado['RESERVA PETRÓLEO'].sum()
    maximo_num_reserva = df_atualizado['RESERVA PETRÓLEO'].max()
    regiao_mais_frequente = (df_atualizado.groupby('REGIÃO GEOGRÁFICA')['PAÍS'].nunique().idxmax())
    pais_maior_reserva = (df_atualizado.groupby("PAÍS")['RESERVA PETRÓLEO'].sum().idxmax())
else:
    qntd_reserva_mundial, maximo_num_reserva, regiao_mais_frequente, pais_maior_reserva = 0,0,'',''

info1, info2, info3, info4 = st.columns(4)
info1.metric('Quantidade Mundial de Petróleo', f'${qntd_reserva_mundial:,.3f}')
info2.metric('Maior Reserva Individual', f'${maximo_num_reserva:,.3f}')
info3.metric('Região com mais países produtores', regiao_mais_frequente)
info4.metric('País com Maior Reserva', pais_maior_reserva)
    
st.markdown("---")

# Gráficos
st.subheader("Gráficos 📊")

graf1, graf2 = st.columns(2)

with graf1:
    if not df_atualizado.empty:
        agrupamento_por_bloco = df_atualizado[['BLOCO', 'PAÍS']].drop_duplicates().groupby('BLOCO').size().reset_index(name='QTD_PAISES').sort_values(by='QTD_PAISES', ascending=False)
        grafico_de_blocos = px.bar(
            agrupamento_por_bloco,
            x='BLOCO',
            y='QTD_PAISES',
            labels={
                'BLOCO': 'Tipo de Bloco',
                'QTD_PAISES': 'Quantidade de Países'
            },
            title=f'Número de Países Participantes do OPEP - {titulo_anos}',
        )
        grafico_de_blocos.update_layout(title_x=0.25)
        grafico_de_blocos.update_yaxes(tickformat=".2s")
        st.plotly_chart(grafico_de_blocos)
    else:
        st.warning("Nenhum dado para exibir")

with graf2:
    if not df_atualizado.empty:
        maiores_reservas_por_regiao = df_atualizado.groupby('REGIÃO GEOGRÁFICA')['RESERVA PETRÓLEO'].sum().sort_values(ascending=False).head().reset_index()
        grafico_num_petroleo_por_regiao = px.bar(
            maiores_reservas_por_regiao,
            x='RESERVA PETRÓLEO',
            y='REGIÃO GEOGRÁFICA',
            orientation='h',
            labels={
                'REGIÃO GEOGRÁFICA': 'Região',
                'RESERVA PETRÓLEO': 'Reserva de Petróleo (bilhões de barris)'
            },
            title=f'Região com Maiores Reserva de Petróleo - {titulo_anos}',
            
        )
        grafico_num_petroleo_por_regiao.update_layout(title_x=0.25)
        st.plotly_chart(grafico_num_petroleo_por_regiao)
    else:
        st.warning("Nenhum dado para exibir")    

graf3, graf4 = st.columns(2)

with graf3:
    if not df_atualizado.empty:
        paises_maiores_reservas = df_atualizado.groupby('PAÍS')['RESERVA PETRÓLEO'].sum().sort_values(ascending=False).head().reset_index()
        grafico_num_petroleo_por_pais = px.bar(
            paises_maiores_reservas,
            x='PAÍS',
            y='RESERVA PETRÓLEO',
            labels={
                'PAÍS': 'País',
                'RESERVA PETRÓLEO': 'Reserva de Petróleo (bilhões de barris)'
            },
            title=f'Países com Maiores Reserva de Petróleo - {titulo_anos}'
        )
        grafico_num_petroleo_por_pais.update_layout(title_x=0.25)   
        st.plotly_chart(grafico_num_petroleo_por_pais)
    else:
        st.warning("Nenhum dado para exibir")

# Gráfico Mapa
with graf4:
    if not df_atualizado.empty:
        pais_df = (df_atualizado.groupby(["ISO3", "PAÍS"])["RESERVA PETRÓLEO"].sum().reset_index())
        mapa_paises_reservas = px.choropleth(
            pais_df,
            locations="ISO3",
            color="RESERVA PETRÓLEO",
            hover_name="PAÍS",
            color_continuous_scale="YlOrRd",
            labels={
                'ISO3': 'Siglas',
                'RESERVA PETRÓLEO': 'Reserva de Petróleo (bilhões de barris)'
            },
            title=f"Distribuição Mundial das Reservas de Petróleo - {titulo_anos}"
        )
        mapa_paises_reservas.update_layout(title_x=0.17)
        st.plotly_chart(mapa_paises_reservas, width="stretch")


