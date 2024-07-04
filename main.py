import streamlit as st
from langchain.llms import OpenAI
st.title("Pizzería JAF - DELIVERY")
openai.api_key = st.sidebar.text_input("Ingresa tu API Key para acceder a la IA ", type="password")
def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Escriba su pedido:', 'Cual de nuestras especialidades desea solicitasr ? ')
    submitted = st.form_submit_button('Pedir')
    if not openai_api_key.startswith('sk-'):
        st.warning('Por favor ingrese una Api key para poder continuar', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)