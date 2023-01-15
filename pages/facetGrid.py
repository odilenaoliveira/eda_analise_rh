import streamlit as st 
import pandas as pd
import seaborn as sns 
import warnings
warnings.filterwarnings('ignore')
sns.set_style('darkgrid')
color = ['#ED72A3','#8565F0','#22559C', '#F27370','#FA9856','#EDE862']

# carregando os dados
df = pd.read_csv('HR-Employee-Attrition.csv')
df.drop(['EmployeeCount','EmployeeNumber','StandardHours','Over18'],axis=1,inplace=True)

st.title('Visualização em Geral')
st.markdown(''' 
    Para ampliar as imagens arraste o mouse em cima do gráfico, ao lado esquerdo da tela, verá **duas setas** oposta,
    clique e a imagem ampliará.
    O conjunto de dados se trata da existência de atritos nas profissões entre os gêneros, quanto tempo uma pessoa
    trabalhou na empresa, se teve promoção, em qual cargo e qual média da renda por gênero.
    Abaixo, você pode usar os filtros e fazer a comparação entre os sexo masculino e feminino, cargo, 
    profissão.
''')

#todo: estrutura da página

with st.container():
    st.write('### Renda mensal de quem trabalhou por mais tempo pelo nível de trabalho')
    level = st.radio('JobLevel:', df['JobLevel'].unique(), horizontal=True)
    nivel = df[df['JobLevel'] == level]
    g = sns.FacetGrid(nivel, col='Gender' , row='JobLevel', height=7,sharex=False, sharey=False)
    g.map_dataframe(sns.barplot, x='TotalWorkingYears',y='MonthlyIncome',ci=None)
    g.set_titles(size=14, fontweight='bold')
    g.tick_params(axis='x', labelsize=14)
    g.set_xlabels('TotalWorkingYears',fontsize=14)
    g.set_ylabels('MonthlyIncome',fontsize=14)
    st.pyplot(g)
#? -----------------------------
with st.container():
    st.write('### Renda mensal por idade pelo nível de trabalho')
    level = st.radio('Job Level:', df['JobLevel'].unique(), horizontal=True)
    nivel = df[df['JobLevel'] == level]
    g1 = sns.FacetGrid(nivel, col='Gender' , row='JobLevel', height=7,sharex=False, sharey=False)
    g1.map_dataframe(sns.barplot, x='Age',y='MonthlyIncome',ci=None)
    g1.set_titles(size=14, fontweight='bold')
    g1.set_xlabels('Age',fontsize=14)
    g1.set_ylabels('MonthlyIncome',fontsize=14)
    st.pyplot(g1)
#? -----------------------------
with st.container():
    st.write('### Idade de quem trabalhou por mais tempo por nível de trabalho')
    level = st.radio('Joblevel:', df['JobLevel'].unique(), horizontal=True)
    nivel = df[df['JobLevel'] == level]
    g2 = sns.FacetGrid(nivel, col='Gender' , row='JobLevel', height=7, sharex=False, sharey=False)
    g2.map_dataframe(sns.barplot, x='TotalWorkingYears',y='Age',ci=None)
    g2.set_titles(size=14, fontweight='bold')
    g2.set_xlabels('TotalWorkingYears',fontsize=14)
    g2.set_ylabels('Age',fontsize=14)
    st.pyplot(g2)
#? -----------------------------
with st.container():
    st.write('### Renda mensal de quem trabalhou por mais tempo em cada departamento')
    dep = st.radio('Department:', df['Department'].unique(), horizontal=True)
    depart = df[df['Department'] == dep]
    g3 = sns.FacetGrid(depart, col='Gender' , row='Department', height=7,sharex=False, sharey=False)
    g3.map_dataframe(sns.barplot, x='TotalWorkingYears',y='MonthlyIncome',ci=None)
    g3.set_titles(size=14, fontweight='bold')
    g3.set_xlabels('TotalWorkingYears',fontsize=14)
    g3.set_ylabels('MonthlyIncome',fontsize=14)
    st.pyplot(g3)
#? -----------------------------
with st.container():
    st.write('### Renda mensal de quem trabalhou por mais tempo por nível de educacional')
    ed = st.radio('EducationField:', df['EducationField'].unique(), horizontal=True)
    educ = df[df['EducationField'] == ed]
    g4 = sns.FacetGrid(educ, col='Gender' , row='EducationField', height=6,sharex=False, sharey=False)
    g4.map_dataframe(sns.barplot, x='TotalWorkingYears',y='MonthlyIncome',ci=None)
    g4.set_titles(size=12, fontweight='bold')
    g4.set_xlabels('TotalWorkingYears',fontsize=14)
    g4.set_ylabels('MonthlyIncome',fontsize=14)
    st.pyplot(g4)
#? -----------------------------
with st.container():
    st.write('### Renda mensal de quem trabalhou por mais tempo pelo cargo de trabalho')
    job = st.radio('JobRole:', df['JobRole'].unique(), horizontal=True)
    jobrole = df[df['JobRole'] == job]
    g5 = sns.FacetGrid(jobrole, col='Gender' , row='JobRole', height=7,sharex=False, sharey=False)
    g5.map_dataframe(sns.barplot, x='TotalWorkingYears',y='MonthlyIncome',ci=None)
    g5.set_titles(size=14, fontweight='bold')
    g5.set_xlabels('TotalWorkingYears',fontsize=14)
    g5.set_ylabels('MonthlyIncome',fontsize=14)
    st.pyplot(g5)
#? -----------------------------
with st.container():
    st.write('### Atrito devido aos anos trabalhados na empresa e cargo de trabalho')
    job = st.radio('Job Role:', df['JobRole'].unique(), horizontal=True)
    jobrole = df[df['JobRole'] == job]
    g6 = sns.FacetGrid(jobrole, col='Gender' , row='JobRole', hue='Attrition', height=6,sharex=False, sharey=False)
    g6.map_dataframe(sns.barplot, x='TotalWorkingYears',y='Age',alpha=0.6,ci=None)
    g6.set_titles(size=14, fontweight='bold')
    g6.set_xlabels('TotalWorkingYears',fontsize=14)
    g6.set_ylabels('Age',fontsize=14)
    g6.add_legend()
    st.pyplot(g6)
#? -----------------------------
with st.container():
    st.write('### Atrito devido aos anos trabalhados na empresa em cada departamento')
    dep = st.radio('Escolha o Departamento:', df['Department'].unique(), horizontal=True)
    depart = df[df['Department'] == dep]
    g7 = sns.FacetGrid(depart, col='Gender' , row='Department', hue='Attrition', height=8,sharex=False, sharey=False)
    g7.map_dataframe(sns.barplot, x='TotalWorkingYears',y='Age',alpha=0.6,ci=None)
    g7.set_titles(size=14, fontweight='bold')
    g7.set_xlabels('TotalWorkingYears',fontsize=14)
    g7.set_ylabels('Age',fontsize=14)
    g7.add_legend()
    st.pyplot(g7)
#? -----------------------------
with st.container():
    st.write('### Atrito devido aos anos trabalhados na empresa e por viagem a serviço')
    bu = st.radio('BusinessTravel:', df['BusinessTravel'].unique(), horizontal=True)
    business = df[df['BusinessTravel'] == bu]
    g8 = sns.FacetGrid(business, col='Gender', row='BusinessTravel', hue='Attrition', height=8,sharex=False, sharey=False)
    g8.map_dataframe(sns.barplot, x='TotalWorkingYears',y='Age',alpha=0.6,ci=None)
    g8.set_titles(size=14, fontweight='bold')
    g8.set_xlabels('TotalWorkingYears',fontsize=14)
    g8.set_ylabels('Age',fontsize=14)
    g8.add_legend()
    st.pyplot(g8)
#? -----------------------------
with st.container():
    st.write('### Atrito por anos trabalhados na empresa e estado civil')
    married = st.radio('Escolha o Departamento abaixo:', df['MaritalStatus'].unique(), horizontal=True)
    marital = df[df['MaritalStatus'] == married]
    g9 = sns.FacetGrid(marital, col='Gender', row='MaritalStatus', hue='Attrition', height=8,sharex=False, sharey=False)
    g9.map_dataframe(sns.barplot, x='TotalWorkingYears',y='Age',alpha=0.6,ci=None)
    g9.set_titles(size=14, fontweight='bold')
    g9.set_xlabels('TotalWorkingYears',fontsize=14)
    g9.set_ylabels('Age',fontsize=14)
    g9.add_legend()
    st.pyplot(g9)
#? -----------------------------
with st.container():
    st.write('### Hora extra por departamento')
    dep = st.radio('Escolha o Departamento abaixo:', df['Department'].unique(), horizontal=True)
    depart = df[df['Department'] == dep]
    g10 = sns.FacetGrid(depart, col='Gender', row='Department', hue='OverTime', height=8,sharex=False, sharey=False)
    g10.map_dataframe(sns.barplot, x='TotalWorkingYears',y='Age',alpha=0.6,ci=None)
    g10.set_titles(size=14, fontweight='bold')
    g10.set_xlabels('TotalWorkingYears',fontsize=14)
    g10.set_ylabels('Age',fontsize=14)
    g10.add_legend()
    st.pyplot(g10)