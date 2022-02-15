import pandas as pd 
import numpy as np 
import streamlit as st 
from PIL import Image
import plotly as plt 
import plotly.express as px
import plotly.graph_objects as go 
from plotly.offline import iplot
import plotly.figure_factory as ff

st.title('Understanding Schizophrenia')

   
st.markdown('Schizophrenia is a functional psychotic disorder characterized by the presence of delusional beliefs,hallucinations and disturbances in thought,perception,and behavior')
st.markdown('Neuroimaging have shown substantive evidence of brain structual,functional,and neurochemical alterations that are more pronoucned in the association cortex and subcortical regions')
st.image('neuro.jpg',use_column_width=True) 

#Loading Data
data=pd.read_csv('prevalence-of-schizophrenia-in-males-vs-females.csv')
data_1=pd.read_csv('share-of-population-with-schizophrenia.csv')

st.write(data_1.rename(columns={'Entity':'Entity','Code':'Code','Year':'Year','Prevalence - Schizophrenia - Sex: Both - Age: Age-standardized (Percent)':
                      'Prevalence of Schizophrenia','Flag_country':'Flag_country'},inplace=True))


st.header("Prevalence of Schizophrenia across different regions")

fig=px.line(data_1, x='Year', y='Prevalence of Schizophrenia',color='Entity')
st.plotly_chart(fig)

st.write(df_only_countries=data_1[data_1['Flag_country'] != 0])

fig_1=px.choropleth(data_1, locations="Code", color="Prevalence of Schizophrenia", hover_name="Entity",animation_frame="Year",color_continuous_scale=px.colors.sequential.Plasma,projection="hammer")
st.plotly_chart(fig_1)

st.header("Highest Prevalence in developed countries")

if st.button('Click for further explanation'):

    st.write('Many factors for such a finding can play a role')
    st.write('1.Developed countries have less stigma against mental illness, which leads to seeking help and higher documentation')
    st.write('2.Risk Factors that affect Schizophrenia are cultural identity and attachment, being a minority all of which is found higher in developed countries')




st.write(data.rename(columns={'Entity':'Entity','Code':'Code','Year':'Year','Prevalence - Schizophrenia - Sex: Male - Age: Age-standardized (Percent)':
                      'Prevalence of  Schizophrenia in Males','Prevalence - Schizophrenia - Sex: Female - Age: Age-standardized (Percent)':'Prevalence of Schizophrenia in Females',
                       'Population (historical estimates)':'Population'}
                       ,inplace=True))

data=data.dropna()

st.header("Can gender play a role?")

fig_2=px.scatter(data,x='Prevalence of  Schizophrenia in Males',y='Prevalence of Schizophrenia in Females',size='Population',
          size_max=70,color='Code',animation_frame='Year',animation_group='Entity',log_x=True)
st.plotly_chart(fig_2)
fig_3=px.choropleth(data, locations="Code", color="Prevalence of  Schizophrenia in Males", hover_name="Entity",animation_frame="Year",color_continuous_scale=px.colors.sequential.Plasma,projection="hammer")
st.plotly_chart(fig_3)

fig_4=px.choropleth(data, locations="Code", color="Prevalence of Schizophrenia in Females", hover_name="Entity",animation_frame="Year",color_continuous_scale=px.colors.sequential.Plasma,projection="hammer")
st.plotly_chart(fig_4)

fig_5=px.choropleth(data, locations="Code", color="Prevalence of  Schizophrenia in Males", hover_name="Entity",animation_frame="Year",color_continuous_scale=px.colors.sequential.Plasma,projection="hammer")

st.plotly_chart(fig_5)



fig_6= px.scatter_3d(data, x='Prevalence of  Schizophrenia in Males', y='Population', z='Year',size='Prevalence of  Schizophrenia in Males', size_max=10,
                    color='Entity')

fig_7=px.scatter_3d(data, x='Prevalence of Schizophrenia in Females', y='Population', z='Year',size='Prevalence of Schizophrenia in Females', size_max=10,
                    color='Entity')


if st.checkbox('Show 3D plots'):
    st.plotly_chart(fig_6)
    st.plotly_chart(fig_7)

st.subheader("The above graphs show, a higher prevalence of schiophrenia in males than females")

if st.button('Click to know why'):
    st.write("There is not definite answer for the above, but here are some explanations based on several researchs:")
    st.write("1.Studies have shown that higher prevalence is due to higher florid in males than females")
    st.write("2.Males are more collerated with higher brain injuries in chilhood, a risk factor of schizophrenia")
    st.write("3.Psychological social pressure on men may accelrate occurences, a reason for diagnosis of schizophrenia at a lower age in males than females")
    st.write("4.There are anatomical brain differences such as volume of the brain between men and women and how they react on a neurochemical level, which research is still seeking for further studies")


st.header("Schizophrenia in Lebanon")

Schizo_Lebanon= data_1[data_1['Entity'] == 'Lebanon']

fig_8=px.line(Schizo_Lebanon,x='Year',y='Prevalence of Schizophrenia')
fig_8.update_layout(title='Schizophrenia Prevalence in Lebanon')
st.plotly_chart(fig_8)

st.subheader("What happened in Lebanon between 2010-2015?")


