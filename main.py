import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="DashUF",
    layout="wide")

st.title("DASHUF: Um Dashboard sobre os Dados de Despesa da UFERSA - Anos 2022, 2023 e 2024")

df = pd.read_csv('despesaOrcamentaria 2022x2023x2024 - Possibilidades de Gráficos.csv')

col1, col2 = st.columns(2)

with col1: 
    # Seleciona as três primeiras colunas (índices 0, 1 e 2)
    df_filtered = df.iloc[:, :3]
    
    # Renomeia as colunas para facilitar o uso, já que os nomes se repetem
    df_filtered.columns = ['ANO', 'Orcamento_Atualizado', 'Orcamento_Realizado']
    
    # Converte a coluna 'ANO' para numérico, transformando erros em NaN
    df_filtered['ANO'] = pd.to_numeric(df_filtered['ANO'], errors='coerce')
    
    # Remove linhas onde a coluna 'ANO' é NaN (linhas vazias ou não numéricas)
    df_filtered = df_filtered.dropna(subset=['ANO'])
    
    def clean_currency(column):
        return (column.astype(str)
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
                .astype(float))
    
    df_filtered['Orcamento_Atualizado'] = clean_currency(df_filtered['Orcamento_Atualizado'])
    df_filtered['Orcamento_Realizado'] = clean_currency(df_filtered['Orcamento_Realizado'])
    
    df_filtered['ANO'] = df_filtered['ANO'].astype(int)
    
    fig1 = px.histogram(df_filtered, x='ANO', y=['Orcamento_Atualizado', 'Orcamento_Realizado'],
    title='Grupo de Natureza de Despesa Pessoal e Encargos Sociais',
    barmode = 'group', text_auto=True)
    fig1.update_layout(xaxis_title = 'Ano', yaxis_title = 'Valor em R$')
    
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    # Seleciona as colunas G, H e I (índices 6, 7 e 8)
    df_filtered = df.iloc[:7, 6:9]
    
    # Renomeia as colunas para facilitar o uso
    df_filtered.columns = ['ANO', 'Orcamento_Atualizado', 'Orcamento_Realizado']
    
    # Converte a coluna 'ANO' para numérico, transformando erros em NaN
    df_filtered['ANO'] = pd.to_numeric(df_filtered['ANO'], errors='coerce')
    
    # Remove linhas onde a coluna 'ANO' é NaN (linhas vazias ou não numéricas)
    df_filtered = df_filtered.dropna(subset=['ANO'])
    
    # Função para limpar e converter colunas de moeda
    def clean_currency(column):
        return (column.astype(str)
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
                .astype(float))
    
    # Aplica a limpeza às colunas de orçamento
    df_filtered['Orcamento_Atualizado'] = clean_currency(df_filtered['Orcamento_Atualizado'])
    df_filtered['Orcamento_Realizado'] = clean_currency(df_filtered['Orcamento_Realizado'])
    
    # Converte a coluna 'ANO' para inteiro
    df_filtered['ANO'] = df_filtered['ANO'].astype(int)
    
    df_filtered.head()
    
    fig2 = px.histogram(df_filtered, x='ANO', y=['Orcamento_Atualizado', 'Orcamento_Realizado'],
    title='Grupo de Natureza de Despesa Corrente',
    barmode = 'group', text_auto=True,
                        
    color_discrete_map={'Orcamento_Atualizado': 'blue', 'Orcamento_Realizado': 'red'})
    fig2.update_layout(xaxis_title = 'Ano', yaxis_title = 'Valor em R$')
    
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

row2_col1, row2_col2 = st.columns(2)
with row2_col1:
    # Seleciona as colunas L, M e N (índices 11, 12 e 13)
    df_filtered = df.iloc[:, 11:14]
    
    # Renomeia as colunas para facilitar o uso
    df_filtered.columns = ['ANO', 'Orcamento_Atualizado', 'Orcamento_Realizado']
    
    # Converte a coluna 'ANO' para numérico, transformando erros em NaN
    df_filtered['ANO'] = pd.to_numeric(df_filtered['ANO'], errors='coerce')
    
    # Remove linhas onde a coluna 'ANO' é NaN (linhas vazias ou não numéricas)
    df_filtered = df_filtered.dropna(subset=['ANO'])
    
    # Função para limpar e converter colunas de moeda
    def clean_currency(column):
        return (column.astype(str)
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
                .astype(float))
    
    # Aplica a limpeza às colunas de orçamento
    df_filtered['Orcamento_Atualizado'] = clean_currency(df_filtered['Orcamento_Atualizado'])
    df_filtered['Orcamento_Realizado'] = clean_currency(df_filtered['Orcamento_Realizado'])
    
    # Converte a coluna 'ANO' para inteiro
    df_filtered['ANO'] = df_filtered['ANO'].astype(int)
    
    df_filtered.head()
    
    fig3 = px.histogram(df_filtered, x='ANO', y=['Orcamento_Atualizado', 'Orcamento_Realizado'],
    title='Grupo de Natureza de Despesa Investimento',
    barmode = 'group', text_auto=True,
                        
    color_discrete_map={'Orcamento_Atualizado': 'blue', 'Orcamento_Realizado': 'red'})
    fig3.update_layout(xaxis_title = 'Ano', yaxis_title = 'Valor em R$')
    
    st.plotly_chart(fig3, use_container_width=True)

with row2_col2:
    # Seleciona as colunas E, F e G (índices 4, 5 e 6) e as linhas 31 a 37
    df_filtered = df.iloc[30:37, 4:7]
    
    # Renomeia as colunas para facilitar o uso
    df_filtered.columns = ['AÇÃO', 'Orcamento_Inicial', 'Orcamento_Atualizado']
    
    # Função para limpar e converter colunas de moeda
    def clean_currency(column):
        return (column.astype(str)
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
                .astype(float))
    
    # Aplica a limpeza às colunas de orçamento
    df_filtered['Orcamento_Atualizado'] = clean_currency(df_filtered['Orcamento_Atualizado'])
    df_filtered['Orcamento_Inicial'] = clean_currency(df_filtered['Orcamento_Inicial'])
    
    fig4 = px.histogram(df_filtered, x='AÇÃO', y=['Orcamento_Inicial', 'Orcamento_Atualizado'],
    title='Comparativo da Despesa de Pessoal e Encargos Sociais - 2022',
    barmode = 'group', text_auto=True,
    color_discrete_map={'Orcamento_Inicial': 'blue', 'Orcamento_Atualizado': 'red'})
    fig4.update_layout(yaxis_title = 'Valor em R$')

    st.plotly_chart(fig4, use_container_width=True)

st.divider()

row3_col1, row3_col2 = st.columns(2)

with row3_col1:
    
    # Seleciona as colunas E, F e G (índices 4, 5 e 6) e as linhas 57 a 63
    df_filtered = df.iloc[57:63, 4:7]
    
    # Renomeia as colunas para facilitar o uso
    df_filtered.columns = ['AÇÃO', 'Orcamento_Inicial', 'Orcamento_Atualizado']
    
    # Função para limpar e converter colunas de moeda
    def clean_currency(column):
        return (column.astype(str)
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
                .astype(float))
    
    # Aplica a limpeza às colunas de orçamento
    df_filtered['Orcamento_Atualizado'] = clean_currency(df_filtered['Orcamento_Atualizado'])
    df_filtered['Orcamento_Inicial'] = clean_currency(df_filtered['Orcamento_Inicial'])
    
    fig5 = px.histogram(df_filtered, x='AÇÃO', y=['Orcamento_Inicial', 'Orcamento_Atualizado'],
    title='Comparativo da Despesa de Pessoal e Encargos Sociais - 2023',
    barmode = 'group', text_auto=True,
    color_discrete_map={'Orcamento_Inicial': 'blue', 'Orcamento_Atualizado': 'red'})
    fig5.update_layout(yaxis_title = 'Valor em R$')
    
    st.plotly_chart(fig5, use_container_width=True)

with row3_col2:

    # Seleciona as colunas E, F e G (índices 4, 5 e 6) e as linhas 85 a 93
    df_filtered = df.iloc[87:93, 4:7]
    
    # Renomeia as colunas para facilitar o uso
    df_filtered.columns = ['AÇÃO', 'Orcamento_Inicial', 'Orcamento_Atualizado']
    
    # Função para limpar e converter colunas de moeda
    def clean_currency(column):
        return (column.astype(str)
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
                .astype(float))
    
    # Aplica a limpeza às colunas de orçamento
    df_filtered['Orcamento_Atualizado'] = clean_currency(df_filtered['Orcamento_Atualizado'])
    df_filtered['Orcamento_Inicial'] = clean_currency(df_filtered['Orcamento_Inicial'])
    
    fig6 = px.histogram(df_filtered, x='AÇÃO', y=['Orcamento_Inicial', 'Orcamento_Atualizado'],
    title='Comparativo da Despesa de Pessoal e Encargos Sociais - 2024',
    barmode = 'group', text_auto=True,
    color_discrete_map={'Orcamento_Inicial': 'blue', 'Orcamento_Atualizado': 'red'})
    fig6.update_layout(yaxis_title = 'Valor em R$')
    
    st.plotly_chart(fig6, use_container_width=True)

st.divider()

row4_col1, row4_col2 = st.columns(2)

with row4_col1:
       
   df = pd.read_csv('despesaOrcamentaria 2022x2023x2024 - Tabela dinâmica 2.csv')
    
   df_filtered = df.copy()

   df_filtered.columns = ['Ação', 'SUM de Orçamento Atualizado', 'SUM de Orçamento Realizado']
    
   def clean_currency(column):
      return (column.astype(str)
               .str.replace('R$', '', regex=False)
               .str.replace('.', '', regex=False)
               .str.replace(',', '.', regex=False)
               .str.strip()
               .astype(float))
    
   df_filtered['SUM de Orçamento Atualizado'] = clean_currency(df_filtered['SUM de Orçamento Atualizado'])
   df_filtered['SUM de Orçamento Realizado'] = clean_currency(df_filtered['SUM de Orçamento Realizado'])
    
   fig7 = px.histogram(df_filtered, x='Ação', y=['SUM de Orçamento Atualizado', 'SUM de Orçamento Realizado'],
   title='Comparativo de Despesa Corrente',
   barmode = 'group', text_auto=True,
   color_discrete_map={'SUM de Orçamento Atualizado': 'blue', 'SUM de Orçamento Realizado': 'red'})
   fig7.update_layout(yaxis_title = 'Valor em R$')

   df_filtered = df.copy()
    
   df_filtered.columns = ['Ação', 'SUM de Orçamento Atualizado', 'SUM de Orçamento Realizado']
    
   def clean_currency(column):
       return (column.astype(str)
               .str.replace('R$', '', regex=False)
               .str.replace('.', '', regex=False)
               .str.replace(',', '.', regex=False)
               .str.strip()
               .astype(float))
    
   df_filtered['SUM de Orçamento Atualizado'] = clean_currency(df_filtered['SUM de Orçamento Atualizado'])
   df_filtered['SUM de Orçamento Realizado'] = clean_currency(df_filtered['SUM de Orçamento Realizado'])
   
   st.plotly_chart(fig7, use_container_width=True)
    
with row4_col2:
    df_ia = pd.read_csv('despesaOrcamentaria 2022x2023x2024 - Gráficos gerados pela IA.csv')

    # Create a copy to work with, avoiding modifying the original df
    df_temp_ia = df_ia.copy()
    
    # Set the second row (index 1) as the header
    new_columns = df_temp_ia.iloc[1].tolist()
    df_filtered_ia = df_temp_ia[2:].copy() # Select data from row 2 onwards
    df_filtered_ia.columns = new_columns # Assign the extracted header as new column names
    
    # Rename the columns to be consistent and easier to work with
    df_filtered_ia = df_filtered_ia.rename(columns={
        'Orçamento Atualizado(R$)': 'Orçamento Atualizado',
        'Orçamento Realizado (R$)': 'Orçamento Realizado'
    })
    
    # Reset index after dropping rows
    df_filtered_ia = df_filtered_ia.reset_index(drop=True)
    
    
    def clean_currency(column):
        return (column.astype(str)
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
                .astype(float))
    
    df_filtered_ia['Orçamento Atualizado'] = clean_currency(df_filtered_ia['Orçamento Atualizado'])
    df_filtered_ia['Orçamento Realizado'] = clean_currency(df_filtered_ia['Orçamento Realizado'])
    
    
    fig8 = px.histogram(df_filtered_ia, x='Função', y=['Orçamento Atualizado', 'Orçamento Realizado'],
    title='Execução orçamentária por FUNÇÃO',
    barmode = 'group', text_auto=True,
    color_discrete_map={'Orçamento Atualizado': 'blue', 'Orçamento Realizado': 'red'})
    fig8.update_layout(yaxis_title = 'Valor em R$')

    st.plotly_chart(fig8, use_container_width=True)

row5_col1, row5_col2 = st.columns(2)

with row5_col1:
    df = pd.read_csv('despesaOrcamentaria 2022x2023x2024 - Gráficos gerados pela IA (1).csv')
    # Create a copy to work with
    df_temp = df.copy()
    
    mask = (
        (pd.to_numeric(df_temp.iloc[:, 0], errors='coerce').isin([2022, 2023, 2024])) &
        (df_temp.iloc[:, 1].notna()) &
        (df_temp.iloc[:, 2].notna())
    )
    
    df_filtered_raw = df_temp[mask].copy()
    
    # Selecionar as colunas 0, 1 e 2 (Independente do nome delas)
    df_filtered = df_filtered_raw.iloc[:, 0:3].copy()
    
    # Explicitly assign the correct column names
    df_filtered.columns = ['ANO', 'DESPESA CORRENTE (R$)', 'DESPESA DE CAPITAL (R$)']
    
    # Convert 'ANO' to numeric
    df_filtered['ANO'] = pd.to_numeric(df_filtered['ANO'], errors='coerce')
    df_filtered = df_filtered.dropna(subset=['ANO'])
    
    def clean_currency(column):
        return (column.astype(str)
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
                .astype(float))
    
    # Apply cleaning
    df_filtered['DESPESA CORRENTE (R$)'] = clean_currency(df_filtered['DESPESA CORRENTE (R$)'])
    df_filtered['DESPESA DE CAPITAL (R$)'] = clean_currency(df_filtered['DESPESA DE CAPITAL (R$)'])
    
    # Convert 'ANO' to integer
    df_filtered['ANO'] = df_filtered['ANO'].astype(int)
    
    # --- GRÁFICO ---
    # Nota: Adicionei log_y=True de volta, pois na imagem original a diferença 
    # entre 300 milhões e 4 milhões exige escala logarítmica para ser visível.
    fig9 = px.histogram(
        df_filtered, 
        x='ANO', 
        y=['DESPESA CORRENTE (R$)', 'DESPESA DE CAPITAL (R$)'],
        title='Distribuição do Orçamento Realizado por Categoria Econômica (2022-2024)',
        barmode='group', 
        text_auto='.2s',
        log_y=True, # Recomendado baseado na sua imagem original
        color_discrete_map={'DESPESA CORRENTE (R$)': 'blue', 'DESPESA DE CAPITAL (R$)': 'red'}
    )
    
    fig9.update_layout(yaxis_title='Valor em R$ (Escala Log)')
    fig9.show()
    st.plotly_chart(fig9, use_container_width=True)

with row5_col2:
    df_temp = df.copy()
    # Seleciona as linhas 39, 42 e 45 e as colunas 0 e 2 (correspondentes a A e C)
    df_filtered = df.iloc[[39, 42, 45], [0, 2]].copy()
    
    # Renomeia as colunas para facilitar o uso
    df_filtered.columns = ['Elemento de Despesa', 'TOTAL']
    
    # Preenche valores NaN na coluna 'Elemento de Despesa' com o último valor válido
    df_filtered['Elemento de Despesa'] = df_filtered['Elemento de Despesa'].ffill().infer_objects(copy=False)
    
    def clean_currency(column):
        return (column.astype(str)
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
                .replace('nan', '0') # Se a célula estiver vazia, vira zero
                .astype(float))
    
    # Aplica a limpeza às colunas de orçamento
    df_filtered['TOTAL'] = clean_currency(df_filtered['TOTAL'])
    
    fig10 = px.bar(
        df_filtered,
        x='Elemento de Despesa',
        y='TOTAL',
        title='Top 3 Elementos de Despesa por Orçamento Realizado (2022 - 2024)',
        text_auto='.2s',
        color_discrete_sequence=['red']
    )
    fig10.update_layout(
    xaxis_title = 'Elemento de Despesa',
    yaxis_title = 'Valor Total (R$)',
    xaxis={'type': 'category'} # Força o eixo X a tratar os nomes como categorias, não números
    )
    fig10.update_layout(yaxis_title='Valor em R$ (Escala Log)')
    fig10.show()
    st.plotly_chart(fig10, use_container_width=True)

row6_col1, row6_col2 = st.columns(2)

with row6_col1:

    # Seleciona as linhas 55 a 57 (índices 54 a 56) e as colunas 1, 2 e 3 (B, C, D)
    df_filtered = df.iloc[54:57, [1, 2, 3]].copy()
    
    # Renomeia as colunas para facilitar o uso
    df_filtered.columns = ['ANO', 'Orçamento Atualizado', 'Orçamento Realizado']
    
    def clean_currency(column):
        return (column.astype(str)
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
                .replace('nan', '0') # Se a célula estiver vazia, vira zero
                .astype(float))
    
    # Aplica a limpeza às colunas de orçamento
    df_filtered['Orçamento Atualizado'] = clean_currency(df_filtered['Orçamento Atualizado'])
    df_filtered['Orçamento Realizado'] = clean_currency(df_filtered['Orçamento Realizado'])
    
    # Converte a coluna 'ANO' para inteiro
    df_filtered['ANO'] = df_filtered['ANO'].astype(int)
    
    fig11 = px.bar(
        df_filtered,
        x='ANO',
        y=['Orçamento Atualizado', 'Orçamento Realizado'],
        title='Comparativo de Despesa com Educação por Ano', # Updated title to reflect correct rows
        barmode = 'group',
        text_auto=False, # Removed automatic text formatting/rounding
        color_discrete_map={'Orçamento Atualizado': 'blue', 'Orçamento Realizado': 'red'}
    )
    fig11.update_layout(
        xaxis_title = 'Ano',
        yaxis_title = 'Valor em R$',
        xaxis={'type': 'category'}
    )
    fig11.update_traces(texttemplate='%{y}', textposition='outside') # Reverted to display full y-value
    fig11.show()
    st.plotly_chart(fig11, use_container_width=True)

with row6_col2:

    # Seleciona as linhas 74 a 77 (índices 73 a 76) e as colunas 1, 2 e 3 (B, C, D)
    df_filtered = df.iloc[74:77, [1, 2, 3]].copy()
    
    # Renomeia as colunas para facilitar o uso
    df_filtered.columns = ['ANO', 'Orçamento Atualizado', 'Orçamento Realizado']
    
    def clean_currency(column):
        return (column.astype(str)
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
                .replace('nan', '0') # Se a célula estiver vazia, vira zero
                .astype(float))
    
    # Aplica a limpeza às colunas de orçamento
    df_filtered['Orçamento Atualizado'] = clean_currency(df_filtered['Orçamento Atualizado'])
    df_filtered['Orçamento Realizado'] = clean_currency(df_filtered['Orçamento Realizado'])
    
    # Converte a coluna 'ANO' para inteiro
    df_filtered['ANO'] = df_filtered['ANO'].astype(int)
    
    fig12 = px.bar(
        df_filtered,
        x='ANO',
        y=['Orçamento Atualizado', 'Orçamento Realizado'],
        title='Comparativo de Despesa com Previdência Social por Ano', # Updated title to reflect correct rows
        barmode = 'group',
        text_auto=False, # Removed automatic text formatting/rounding
        color_discrete_map={'Orçamento Atualizado': 'blue', 'Orçamento Realizado': 'red'}
    )
    fig12.update_layout(
        xaxis_title = 'Ano',
        yaxis_title = 'Valor em R$',
        xaxis={'type': 'category'}
    )
    fig12.update_traces(texttemplate='%{y}', textposition='outside') # Reverted to display full y-value
    fig12.show()

    st.plotly_chart(fig12, use_container_width=True)

row7_col1, row7_col2 = st.columns(2)

with row7_col1:

    # Seleciona as linhas 93 a 96 (índices 92 a 95) e as colunas 1, 2 e 3 (B, C, D)
    df_filtered = df.iloc[93:96, [1, 2, 3]].copy()
    
    # Renomeia as colunas para facilitar o uso
    df_filtered.columns = ['ANO', 'Orçamento Atualizado', 'Orçamento Realizado']
    
    def clean_currency(column):
        return (column.astype(str)
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
                .replace('nan', '0') # Se a célula estiver vazia, vira zero
                .astype(float))
    
    # Aplica a limpeza às colunas de orçamento
    df_filtered['Orçamento Atualizado'] = clean_currency(df_filtered['Orçamento Atualizado'])
    df_filtered['Orçamento Realizado'] = clean_currency(df_filtered['Orçamento Realizado'])
    
    # Converte a coluna 'ANO' para inteiro
    df_filtered['ANO'] = df_filtered['ANO'].astype(int)
    
    fig13 = px.bar(
        df_filtered,
        x='ANO',
        y=['Orçamento Atualizado', 'Orçamento Realizado'],
        title='Comparativo de Despesa com Encargos Especiais por Ano', # Updated title to reflect correct rows
        barmode = 'group',
        text_auto=False, # Removed automatic text formatting/rounding
        color_discrete_map={'Orçamento Atualizado': 'blue', 'Orçamento Realizado': 'red'}
    )
    fig13.update_layout(
        xaxis_title = 'Ano',
        yaxis_title = 'Valor em R$',
        xaxis={'type': 'category'}
    )
    fig13.update_traces(texttemplate='%{y}', textposition='outside') # Reverted to display full y-value
    fig13.show()

    st.plotly_chart(fig13, use_container_width=True)
