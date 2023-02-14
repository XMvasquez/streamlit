import streamlit as at 

def bienvenida (nombre):
    my mensaje = 'bienvenido/a :' + nombre
    return mensaje

    myname = st.text_input ('nombre :')
    if (myname):
        mensaje = bienvenida (myname)
        st.write (" : {mensaje} ")
        