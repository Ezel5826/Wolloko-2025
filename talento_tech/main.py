import streamlit as st
import groq as Groq
st.set_page_config("MI CHAT BOT",page_icon=":robot:")

MODELOS = ["llama3-8b-8191","llama3-70b-8192","mixtral-8x7b-32768"]

def config_page(nombre):
    st.title("mi chat ia")
    if st.button("saludar") and not nombre=="":
        if len(nombre) > 2:
            st.write(f"hola {nombre}")
        else:
            st.write("ingrese un nombre mayor a 3 caracteres")
    st.sidebar.title("configurar modelos","100")
    modelo_elegido= st.sidebar.selectbox("modelos",MODELOS,index=0)
    return modelo_elegido

def crear_usuario():
    clave_secreta = st.secrets["CLAVE_API"]
    return Groq(apy_key=clave_secreta)

def configurar_modelo(cliente,modelo,mensaje_entrada):
    return cliente.chat.completions.create(
        model=modelo,
        messages = [{"role":"user","content": mensaje_entrada}],
        stream = True
    )

def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes =[]

usuario_groq =crear_usuario()
inicializar_estado()
modelo_actual=config_page()
mensaje=st.chat_input("escribe un prompt")
if mensaje:
    configurar_modelo(usuario_groq,modelo_actual,mensaje)
    print(mensaje)

mensaje = st.chat_input("escribí un promp")