import streamlit as st 
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
sns.set_style('darkgrid')
color = ['#ED72A3','#8565F0','#22559C', '#F27370','#FA9856','#EDE862']


# função de rótulos no gráfico de barra
def rotulo(axes):
  for retangulo in axes.patches:
    bar_value = retangulo.get_height()
    text = f'{bar_value:,.1f}'
    axes.text(retangulo.get_x() + retangulo.get_width() / 2,
            np.nan_to_num(retangulo.get_height() + 22),
            text,
            ha = 'center',rotation=90, size=12, color='black')

# carregando os dados
df = pd.read_csv('HR-Employee-Attrition.csv')
df.drop(['EmployeeCount','EmployeeNumber','StandardHours','Over18'],axis=1,inplace=True)

#? estrutura da página
st.title('Visualização Geral')
st.markdown(''' 
    Para ampliar as imagens arraste o mouse em cima do gráfico, ao lado esquerdo da tela, verá **duas setas** oposta,
    clique e a imagem ampliará.
    O conjunto de dados se trata da existência de atritos nas profissões entre os gêneros, quanto tempo uma pessoa
    trabalhou na empresa, se teve promoção, em qual cargo e qual média da renda por gênero.
''')
#? ------------------------------
tab1,tab2 = st.tabs(['gráfico1','gráfico2'])

with tab1:
    st.write('#### Correlação dos Dados')
    fig = plt.figure(figsize=(18,9))
    sns.heatmap(df.corr(), annot=True, fmt='.1f')
    st.pyplot(fig)
with tab2:
    st.write('#### Correlação forte entre os dados')
    fig1 = plt.figure(figsize=(10,7))
    # correlação forte entre as colunas
    colunas = ['Education','Age','MonthlyIncome','JobLevel','NumCompaniesWorked','TotalWorkingYears','YearsAtCompany',
        'YearsInCurrentRole', 'YearsSinceLastPromotion',
        'YearsWithCurrManager']
    sns.heatmap(df[colunas].corr(), annot=True, fmt='.1f')
    st.pyplot(fig1)

#? ---------------------------------
st.write('## Quantidade de tempo')
tab3,tab4,tab5 = st.tabs(['gráfico3','gráfico4','gráfico5'])
with tab3:
    st.write('#### Total de Anos de Trabalho')
    # Correlação: Total de Anos de Trabalho
    colunas = ['YearsAtCompany','YearsInCurrentRole', 'YearsSinceLastPromotion','YearsWithCurrManager']
    for i in colunas:
        fig2, axes = plt.subplots(figsize=(16,4))
        sns.pointplot(x=df[i], y=df['TotalWorkingYears'], hue=df['Gender'], palette=color, ci=None)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=12)
        plt.tight_layout()
        st.pyplot(fig2)
with tab4:
    st.write('#### Anos na Empresa')
    # Correlação: Anos na Empresa
    colunas = ['YearsInCurrentRole', 'YearsSinceLastPromotion','YearsWithCurrManager']
    for i in colunas:
        fig3, axes = plt.subplots(figsize=(16,4))
        sns.pointplot(x=df[i], y=df['YearsAtCompany'], hue=df['Gender'], palette=color, ci=None)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=12)
        plt.tight_layout()
        st.pyplot(fig3)
with tab5:
    st.write('#### Anos na função atual')
    # Correlação: Anos na função atual
    colunas = ['YearsSinceLastPromotion','YearsWithCurrManager']
    for i in colunas:
        fig4, axes = plt.subplots(figsize=(16,4))
        sns.pointplot(x=df[i], y=df['YearsInCurrentRole'], hue=df['Gender'], palette=color, ci=None)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=12)
        plt.tight_layout()
        st.pyplot(fig4)

#? --------------------------
st.write('## Distribuição')
tab6, tab7 = st.tabs(['gráfico6','gráfico7'])
with tab6:
    st.write('#### Distribuição de gênero entre os dados categóricos')
    colunas = ['WorkLifeBalance','TrainingTimesLastYear','StockOptionLevel',
        'RelationshipSatisfaction','PerformanceRating','NumCompaniesWorked',
    'JobInvolvement', 'JobLevel', 'JobSatisfaction',
    'EnvironmentSatisfaction','Education']
    fig5 = plt.figure(figsize=(9,36))
    for i,col in enumerate(colunas):
        axes = plt.subplot(13,2, i + 1)
        sns.countplot(x=df[col], hue=df['Gender'], palette=['#ED72A3','#8565F0'])
    plt.tight_layout()
    st.pyplot(fig5)
with tab7:
    st.write('#### Distribuição de gênero entre os dados numéricos')
    hist = ['Age', 'DailyRate','DistanceFromHome','HourlyRate','MonthlyIncome',
        'MonthlyRate']
    fig6 = plt.figure(figsize=(10,20))
    for i,col in enumerate(hist):
        axes = plt.subplot(6,2, i + 1)
        sns.histplot(x=df[col], hue=df['Gender'], palette=['#ED72A3','#8565F0'])
    plt.tight_layout()
    st.pyplot(fig6)

#? ------------------
st.write('## Renda Mensal')
tab8, tab9, tab10,tab11 = st.tabs(['gráfico8','gráfico9','gráfico10','gráfico11'])
with tab8:
    st.write('#### Renda mensal por anos de trabalho')
    colunas = ['Education','JobLevel','NumCompaniesWorked','TotalWorkingYears','YearsAtCompany',
       'YearsInCurrentRole', 'YearsSinceLastPromotion',
       'YearsWithCurrManager']
    for i in colunas:
        fig7, axes = plt.subplots(figsize=(16,4))
        sns.barplot(x=df[i], y=df['MonthlyIncome'], hue=df['Gender'], palette=color, ci=None)
        plt.xticks(fontsize=14)
        rotulo(axes) # função de rótulos nas barras
        plt.tight_layout()
        st.pyplot(fig7)
with tab9:
    st.write('#### Renda mensal por Atrito')
    colunas = ['Gender','Department','EducationField','Gender','MaritalStatus','BusinessTravel','JobRole']
    for i in colunas:
        fig8, axes = plt.subplots(figsize=(16,6))
        sns.barplot(x=df[i], y=df['MonthlyIncome'], hue=df['Attrition'], palette=color, ci=None)
        plt.xticks(rotation=50,fontsize=14)
        rotulo(axes)
        plt.tight_layout()
        st.pyplot(fig8)
with tab10:
    st.write('#### Renda mensal vs Hora extra')
    colunas = ['Gender','Department','EducationField','Gender','MaritalStatus','BusinessTravel','JobRole']
    for i in colunas:
        fig9, axes = plt.subplots(figsize=(16,6))
        sns.barplot(x=df[i], y=df['MonthlyIncome'], hue=df['OverTime'], palette=color, ci=None)
        plt.xticks(rotation=50,fontsize=14)
        rotulo(axes)
        plt.tight_layout()
        st.pyplot(fig9)
with tab11:
    st.write('#### Renda mensal por estado civil')
    colunas = ['Gender','Department','EducationField','Gender','BusinessTravel','JobRole']
    for i in colunas:
        fig10, axes = plt.subplots(figsize=(16,6))
        sns.barplot(x=df[i], y=df['MonthlyIncome'], hue=df['MaritalStatus'], palette=color, ci=None)
        plt.xticks(rotation=50,fontsize=14)
        rotulo(axes)
        plt.tight_layout()
        st.pyplot(fig10)

#? ---------------------------------
st.write('## Porcentagem dos dados')
tab12,tab13,tab14,tab15,tab16,tab17,tab18,tab19 = st.tabs(['gráfico12','gráfico13','gráfico14','gráfico15','gráfico16','gráfico17','gráfico18','gráfico19'])
with tab12:
    fig11 = plt.figure(figsize=(20,40))
    df['Attrition'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('Attrition',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig11)
with tab13:
    fig12 = plt.figure(figsize=(20,40))
    df['BusinessTravel'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('BusinessTravel',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig12)
with tab14:
    fig13 = plt.figure(figsize=(20,40))
    df['Department'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('Department',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig13)
with tab15:
    fig14 = plt.figure(figsize=(20,40))
    df['EducationField'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('EducationField',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig14)
with tab16:
    fig15 = plt.figure(figsize=(20,40))
    df['Gender'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('Gender',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig15)
with tab17:
    fig16 = plt.figure(figsize=(20,40))
    df['JobRole'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('JobRole',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig16)
with tab18:
    fig17 = plt.figure(figsize=(20,40))
    df['MaritalStatus'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('MaritalStatus',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig17)
with tab19:
    fig18 = plt.figure(figsize=(20,40))
    df['OverTime'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('OverTime',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig18)

#? ----------------------

st.write('#### Porcentagem de dados por gênero')
tab20,tab21,tab22,tab23,tab24,tab25,tab26 = st.tabs(['gráfico20','gráfico21','gráfico22','gráfico23','gráfico24','gráfico25','gráfico26'])
with tab20:
    fig19 = plt.figure(figsize=(20,40))
    df.groupby(['Attrition'])['Gender'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('Attrition',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig19)
with tab21:
    fig20 = plt.figure(figsize=(20,40))
    df.groupby(['BusinessTravel'])['Gender'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('BusinessTravel',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig20)
with tab22:
    fig21 = plt.figure(figsize=(20,40))
    df.groupby(['Department'])['Gender'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('Department',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig21)
with tab23:
    fig22 = plt.figure(figsize=(20,40))
    df.groupby(['EducationField'])['Gender'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('EducationField',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig22)
with tab24:
    fig23 = plt.figure(figsize=(20,40))
    df.groupby(['JobRole'])['Gender'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('JobRole',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig23)
with tab25:
    fig24 = plt.figure(figsize=(20,40))
    df.groupby(['MaritalStatus'])['Gender'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('MaritalStatus',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig24)
with tab26:
    fig25 = plt.figure(figsize=(20,40))
    df.groupby(['OverTime'])['Gender'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('OverTime',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig25)
    
#? ----------------------

st.write('#### Porcentagem de dados por hora extra')
tab27,tab28,tab29,tab30,tab31,tab32 = st.tabs(['gráfico27','gráfico28','gráfico29','gráfico30','gráfico31','gráfico32'])
with tab27:
    fig26 = plt.figure(figsize=(20,40))
    df.groupby(['Attrition'])['OverTime'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('Attrition',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig26)
with tab28:
    fig27 = plt.figure(figsize=(20,40))
    df.groupby(['BusinessTravel'])['OverTime'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('BusinessTravel',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig27)
with tab29:
    fig28 = plt.figure(figsize=(20,40))
    df.groupby(['Department'])['OverTime'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('Department',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig28)
with tab30:
    fig29 = plt.figure(figsize=(20,40))
    df.groupby(['EducationField'])['OverTime'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('EducationField',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig29)
with tab31:
    fig30 = plt.figure(figsize=(20,40))
    df.groupby(['JobRole'])['OverTime'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('JobRole',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig30)
with tab32:
    fig31 = plt.figure(figsize=(20,40))
    df.groupby(['MaritalStatus'])['OverTime'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('MaritalStatus',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig31)

#? ----------------------

st.write('#### Porcentagem de dados por atrito')
tab33,tab34,tab35,tab36,tab37,tab38,tab39 = st.tabs(['gráfico33','gráfico34','gráfico35','gráfico36','gráfico37','gráfico38','gráfico39'])

with tab33:
    fig32 = plt.figure(figsize=(20,40))
    df.groupby(['BusinessTravel'])['Attrition'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('BusinessTravel',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig32)
with tab34:
    fig33 = plt.figure(figsize=(20,40))
    df.groupby(['Department'])['Attrition'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('Department',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig33)
with tab35:
    fig34 = plt.figure(figsize=(20,40))
    df.groupby(['EducationField'])['Attrition'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('EducationField',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig34)
with tab36:
    fig35 = plt.figure(figsize=(20,40))
    df.groupby(['JobRole'])['Attrition'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('JobRole',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig35)
with tab37:
    fig36 = plt.figure(figsize=(20,40))
    df.groupby(['MaritalStatus'])['Attrition'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('MaritalStatus',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig36)
with tab38:
    fig37 = plt.figure(figsize=(20,40))
    df.groupby(['OverTime'])['Attrition'].value_counts().plot.pie(autopct='%.2f', radius=0.5,colors=color,textprops={'size':26,'color':'black'})
    plt.title('OverTime',fontsize=26, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(fig37)