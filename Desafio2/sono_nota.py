import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Configuração da página
st.set_page_config(
    page_title="Análise Sono vs Notas",
    page_icon="😴📊",
    layout="wide"
)

# Dados
horas_sono = [2, 4, 6, 8, 10]
notas = [1, 3, 6, 7, 9]

# Criar DataFrame
df = pd.DataFrame({
    'Horas de Sono': horas_sono,
    'Notas': notas
})

# Cálculo de correlação
correlacao = df.corr().iloc[0,1]

# Layout do aplicativo
def main():
    st.title('😴📈 Relação entre Horas de Sono e Desempenho Acadêmico')
    st.markdown("---")
    
    # Sidebar com informações
    with st.sidebar:
        st.header("Sobre o Projeto")
        st.markdown("""
        Esta análise explora a relação entre:
        - **Horas de sono** (Grupo A)
        - **Notas acadêmicas** (Grupo B)
        """)
        st.markdown("---")
        st.metric("Correlação", f"{correlacao:.2f}", 
                 help="Coeficiente de correlação de Pearson")
        st.markdown("""
        **Interpretação:**
        - 0 a 0.3: Fraca
        - 0.3 a 0.7: Moderada
        - 0.7 a 1: Forte
        """)
    
    # Layout em colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("📊 Visualização dos Dados")
        
        # Gráfico de dispersão
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        sns.regplot(x='Horas de Sono', y='Notas', data=df, 
                   scatter_kws={'s': 100, 'color': '#4C78A8'}, 
                   line_kws={'color': '#E45756'}, ax=ax1)
        plt.title('Relação entre Horas de Sono e Notas', pad=20)
        plt.xlabel('Horas de Sono')
        plt.ylabel('Notas (0-10)')
        plt.grid(alpha=0.3)
        st.pyplot(fig1)
        
        # Mostrar tabela de dados
        st.subheader("📋 Dados Brutos")
        st.dataframe(df.style.highlight_max(axis=0, color='#F7D65A'))
    
    with col2:
        st.header("📈 Análise Estatística")
        
        # Gráfico de barras comparativo
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        sns.barplot(x='Horas de Sono', y='Notas', data=df, 
                   palette='viridis', ax=ax2)
        plt.title('Média de Notas por Horas de Sono', pad=20)
        plt.xlabel('Horas de Sono')
        plt.ylabel('Nota Média')
        plt.ylim(0, 10)
        st.pyplot(fig2)
        
        # Estatísticas
        st.subheader("🔍 Métricas Estatísticas")
        
        stats_col1, stats_col2 = st.columns(2)
        
        with stats_col1:
            st.metric("Média de Sono", f"{np.mean(horas_sono):.1f} horas")
            st.metric("Desvio Padrão (Sono)", f"{np.std(horas_sono):.2f}")
        
        with stats_col2:
            st.metric("Média de Notas", f"{np.mean(notas):.1f}")
            st.metric("Desvio Padrão (Notas)", f"{np.std(notas):.2f}")
        
        # Teste de correlação
        st.subheader("🧪 Teste de Pearson")
        st.code(f"""
        Coeficiente r = {correlacao:.2f}
        p-valor = {stats.pearsonr(horas_sono, notas)[1]:.4f}
        """)
    
    # Rodapé
    st.markdown("---")
    st.caption("Desenvolvido por [Seu Nome] - Análise de Dados Educacionais")

if __name__ == '__main__':
    main()