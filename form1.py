import streamlit as st
import pandas as pd
import datetime




header = st.container()
userInput = st.container()
preview = st.container()
dataset = st.container()



# Creación de tabla de referencia de clientes para numero consecutivo

# Función para inicializar el DataFrame y st.session_state si no existen
def init():
    if 'clientes_df' not in st.session_state:
        clientes = ['ETM', 'WOLVENG', 'BOSCH','BRP','UL','CONTROL DIGITAL','3CON','BAKER HUGHES','PLASTICSMART','SAARGUMMI','EPS','NRMACHINING','CRG','KIMBERLY CLARK','DIICSA','DACOM','HARMAN','XOMERTRY','ICARUS','THYSSENKRUPP','SHUNK','IBERFLUID']
        id_cliente = ('ETM', 'WOL', 'BOS','BRP','UL','CON','3CO','BAK','PLA','SAA','EPS','NRM','CRG','KIM','DII','DAC','HAR','XOM','ICA','THY','SHU','IBE')
        st.session_state.clientes_df = pd.DataFrame({'cliente': clientes, 'id_cliente': id_cliente, 'consecutivo_de_cliente': 999, 'orden_RFQ': [f"{id_cliente}-999" for id_cliente in id_cliente]})
        st.session_state.numero_RFQ = None

# Función para actualizar el DataFrame y obtener el número de RFQ
def actualizar_consecutivo(cliente):
    if cliente in st.session_state.clientes_df['id_cliente'].values:
        idx = st.session_state.clientes_df.index[st.session_state.clientes_df['id_cliente'] == cliente].tolist()[0]
        st.session_state.clientes_df.at[idx, 'consecutivo_de_cliente'] += 1
        st.session_state.clientes_df.at[idx, 'orden_RFQ'] = f"{cliente}-{st.session_state.clientes_df.at[idx, 'consecutivo_de_cliente']}"
        st.session_state.numero_RFQ = st.session_state.clientes_df.at[idx, 'orden_RFQ']
        st.success(f"Se ha actualizado el consecutivo para el cliente {cliente}.")
    else:
        st.error(f"No se encontró el cliente {cliente} en la base de datos.")

# Inicializar o cargar el DataFrame y st.session_state
init()

RFQ_num = ""

with header:

    st.markdown("<h1 style = 'text-align: center;'> CUMA </h1>", unsafe_allow_html=True)
    st.markdown("<h4 style = 'text-align: center;'> METAL MANUFACTURING SA DE CV </h4>", unsafe_allow_html=True)
    
    col_izq, col_der = st.columns([2.5,1])

    col_izq.subheader("RFQ control")
    rfq_control = pd.read_csv('1 rfq control.csv', encoding='latin-1')
    col_izq.write(rfq_control.head(10))
    col_der.subheader("Control clientes")
    col_der.write(st.session_state.clientes_df)
    

with userInput:

    st.markdown("<h1 style = 'text-align: center;'>Nueva RFQ </h1>", unsafe_allow_html=True)
    st.subheader('Este apartado es para el formato de cada nuevo RFQ creado')

    # Interfaz de usuario

    cliente_input = st.selectbox('Cliente', ('ETM', 'WOLVENG', 'BOSCH','BRP','UL','CONTROL DIGITAL','3CON','BAKER HUGHES','PLASTICSMART','SAARGUMMI','EPS','NRMACHINING','CRG','KIMBERLY CLARK','DIICSA','DACOM','HARMAN','XOMERTRY','ICARUS','THYSSENKRUPP','SHUNK','IBERFLUID'),index=None,
    placeholder="Selecciona cliente")


    
    user_name = st.text_input("Nombre y apellido de usuario")
    

    descripcion = st.text_input("Descripción de parte")

    pm_asignado = st.selectbox('Project Manager asignado',('Rodrigo Ramirez', 'Elian Sanabria','Sergio Santos'),index=None,placeholder="Selecciona encargado")

    rfq_inquiry_date = st.date_input("Fecha en que se solicita RFQ", format="DD/MM/YYYY", value = None)

    RFQ_mail = st.text_input("Palabras clave de correo",placeholder="Texto para buscar en correo")

    if st.button("Crear RFQ"):
        RFQ_num = actualizar_consecutivo(cliente_input)
        st.success(f"Número de RFQ actualizado para el cliente {cliente_input}: {RFQ_num}")


with preview:

    st.markdown("<h4 style = 'text-align: center;'>Datos a cargar </h4>", unsafe_allow_html=True)

    new_data = {"RFQ_num":RFQ_num,
                "RFQ_mail": RFQ_mail,
                "RFQ_inquiry_date":rfq_inquiry_date,
                "Cliente": cliente_input,
                "Descripcion":descripcion
    
                }   
    st.write(new_data)
    


    




