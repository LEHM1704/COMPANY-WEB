import streamlit as st
from PIL import Image

st.set_page_config(page_title="Valerapp",page_icon="🤖",layout="wide")
email_contact="luishuancas1704@gmail.com"

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>",unsafe_allow_html=True)

css_load("style/main.css")

#introduccion

with st.container():
    st.header("Hola, somos Valerapp 👋")
    st.title("Creamos soluciones para acelerar tu negocio")
    st.write("Somos apasionados de la tecnologia y la innovación, especialización en el sector de la digitalización y automatización de negocios")
    st.write("[Saber más >](https://valerapp.com/)")
    
#sobre nosotros

with st.container():
    st.write("---")
    text_colum,animation_colum=st.columns(2)
    with text_colum:
        st.header("Sobre nosotros")
        st.write(
            """
            Nuestro objetivo es poder valorar a los negocios ayudandoles a ahorrar tiempo y dinero
            
            - Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero
            - Tines trabajo que emplean parte de tu jornada a realizar tareas repetitivas sin valor añadido para tu negocio
            - No tienes claras la métricas de tu negocio y quieres tomar decisiones basada en datos
            - quieres mejorar la experiencia de tus clientes
            - Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y bolígrafo
            
            ***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página***
            """
        )
        st.write("[Más sobre nosotros >](https://valerapp.com/about/)")
    
    with animation_colum:
        st.empty()
        
        
#servicios

with st.container():
    st.write("---")
    st.header("Servicios 🔨")
    st.write("##")
    image_colum, text_colum=st.columns((1,2))
    with image_colum:
        image=Image.open("imagenes/fondoindex.png")
        st.image(image,use_column_width=True)
    
    with text_colum:
        st.subheader("Diseño de aplicaciones")
        st.write(
            """
            Si tus procesos diarios tienen que introducir información en diferentes fuentes de datos o bien tienes que trabaja con documentación
            """
        )
        st.write("[Ver servicios >](https://valerapp.com/services)")

with st.container():
    st.write("---")
    st.header("Servicios 🔨")
    st.write("##")
    image_colum, text_colum=st.columns((1,2))
    with image_colum:
        image=Image.open("imagenes/model.png")
        st.image(image,use_column_width=True)
    
    with text_colum:
        st.subheader("Diseño de aplicaciones")
        st.write(
            """
            Si tus procesos diarios tienen que introducir información en diferentes fuentes de datos o bien tienes que trabaja con documentación
            """
        )
        st.write("[Ver servicios >](https://valerapp.com/services)")
        
        
#contacto

with st.container():
    st.write("---")
    st.header("Contacta con nosotros 📲")
    st.write("##")
    contact_form=f"""
    <form action="https://formsubmit.co/{email_contact}" method="POST">
        <input type="hidden" name="_capcha" value="false">
        <input type="text" name="name"  placeholder="Ingresa tu nombre" required>
        <input type="email" name="email" placeholder="Ingresa tu correo electrónico" equired>
        <textarea type="message" name="message" placeholder="Ingresa tu mensaje aquí" required></textarea>
        <button type="submit">Enviar </button>
    </form>
    """
    
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
        
    with right_column:
        st.empty()
