import streamlit as st
import pandas as pd
import datetime


st.markdown("<h1 style = 'text-align: center;'> CUMA </h1>", unsafe_allow_html=True)
st.markdown("<h4 style = 'text-align: center;'> METAL MANUFACTURING SA DE CV </h4>", unsafe_allow_html=True)

#Limpiar variables de forma RFQ 


# Función para inicializar el DataFrame y st.session_state si no existen
def init():
    if 'clientes_df' not in st.session_state:
        clientes = ['ETM', 'WOLVENG', 'BOSCH','BRP','UL','CONTROL DIGITAL','3CON','BAKER HUGHES','PLASTICSMART','SAARGUMMI','EPS','NRMACHINING','CRG','KIMBERLY CLARK','DIICSA','DACOM','HARMAN','XOMERTRY','ICARUS','THYSSENKRUPP','SHUNK','IBERFLUID']
        id_cliente = ('ETM', 'WOL', 'BOS','BRP','UL','CON','3CO','BAK','PLA','SAA','EPS','NRM','CRG','KIM','DII','DAC','HAR','XOM','ICA','THY','SHU','IBE')
        st.session_state.clientes_df = pd.DataFrame({'cliente': clientes, 'id_cliente': id_cliente, 'consecutivo_de_cliente': 999, 'orden_RFQ': [f"{cliente}-999" for cliente in clientes]})
        st.session_state.numero_RFQ = None

# Inicializar o cargar el DataFrame y st.session_state
init()

# Mostrar dataframes RFQ_Control & Clientes_df

col_izq, col_der = st.columns([2,1.5])

col_izq.subheader("RFQ control")
rfq_control = pd.read_csv('1 rfq control.csv', encoding='latin-1')
col_izq.write(rfq_control.head(10))
col_der.subheader("Control clientes")
col_der.write(st.session_state.clientes_df)

# Función para actualizar el DataFrame y obtener el número de RFQ

def actualizar_consecutivo(cliente):
    print("Cliente ingresado:", cliente)
    print("Valores en la columna 'cliente':", st.session_state.clientes_df['cliente'].values)
    
    # Verificar si el cliente existe en el DataFrame
    if cliente in st.session_state.clientes_df['cliente'].values:
        st.write("Cliente encontrado en la base de datos.")
        # Obtener el índice del cliente en el DataFrame
        idx = st.session_state.clientes_df.index[st.session_state.clientes_df['cliente'] == cliente].tolist()[0]
        st.write("Índice del cliente encontrado:", idx)
        # Incrementar la columna 'consecutivo_de_cliente' en 1
        st.session_state.clientes_df.at[idx, 'consecutivo_de_cliente'] += 1
        # Actualizar la columna 'orden_RFQ' del registro correspondiente
        st.session_state.clientes_df.at[idx, 'orden_RFQ'] = f"{cliente}-{st.session_state.clientes_df.at[idx, 'consecutivo_de_cliente']}"
        # Guardar el valor actualizado de 'orden_RFQ' en la variable 'numero_RFQ'
        st.session_state.numero_RFQ = st.session_state.clientes_df.at[idx, 'orden_RFQ']
        st.success(f"Se ha actualizado el consecutivo para el cliente {cliente}. Número de RFQ: {st.session_state.numero_RFQ}")
    else:
        print("Cliente no encontrado en la base de datos.")
        st.error(f"No se encontró el cliente {cliente} en la base de datos.")

# Funcion para mostrar orden_RFQ actual

def show_current_ordenRFQ(customer):
    # Verificar si el cliente existe en el DataFrame
    if customer in st.session_state.clientes_df['cliente'].values:
        # Obtener el índice del cliente
        idx = st.session_state.clientes_df.index[st.session_state.clientes_df['cliente'] == customer].tolist()[0]
        # Obtener el valor de 'orden_RFQ' correspondiente
        orden_RFQ = st.session_state.clientes_df.at[idx, 'orden_RFQ']
        return orden_RFQ
    else:
        return None


# Inicializar variables, cliente_input, user_name

if 'client_input' not in st.session_state or 'user_name' not in st.session_state or 'descripcion' not in st.session_state or 'pm_asignado' not in st.session_state or 'rfq_inquiry_date' not in st.session_state or 'rfq_mail' not in st.session_state:
    st.session_state.client_input = ''
    st.session_state.user_name = ''
    st.session_state.descripcion = ''
    st.session_state.pm_asignado = ''
    st.session_state.rfq_inquiry_date = ''
    st.session_state.rfq_mail = ''


# Entrada de dato para cliente_input
def customer():
    st.session_state.client_input = st.session_state.customer_key
    st.session_state.customer_key = None

client_input = st.selectbox('Cliente', ('ETM', 'WOLVENG', 'BOSCH','BRP','UL','CONTROL DIGITAL','3CON','BAKER HUGHES','PLASTICSMART',
                                         'SAARGUMMI','EPS','NRMACHINING','CRG','KIMBERLY CLARK','DIICSA','DACOM','HARMAN','XOMERTRY',
                                         'ICARUS','THYSSENKRUPP','SHUNK','IBERFLUID'), index=None,placeholder="Selecciona cliente",key='customer_key', on_change=customer)

st.write(f'Cliente seleccionado: {st.session_state.client_input}')

#Mostrar ultimo numero de orden_RFQ

if st.button("Mostrar Orden RFQ"):
    orden_RFQ = show_current_ordenRFQ(st.session_state.client_input)
    if orden_RFQ is not None:
        st.success(f"El valor actual de orden RFQ para {st.session_state.client_input} es: {orden_RFQ}")
    else:
        st.error(f"No se encontró el cliente {st.session_state.client_input} en la base de datos.")

st.divider()


# Entrada de dato para user_name

def username():
    st.session_state.user_name = st.session_state.user_name_key
    st.session_state.user_name_key = ''

st.text_input('Nombre y apellido de usuario', key='user_name_key', on_change=username,placeholder= "Proporciona nombre + apellido")

st.write(f'Nombre de usuario proporcionado: {st.session_state.user_name}')
st.divider()
    
# Entrada de dato para descripcion

def description():
    st.session_state.descripcion = st.session_state.descripcion_key
    st.session_state.descripcion_key = ''

st.text_input('Descripción',key = 'descripcion_key', on_change=description, placeholder='Describe la pieza a fabricar')

st.write(f'Descripción proporcionada: {st.session_state.descripcion}')
st.divider( )

# Entrada de dato para pm_asignado
def assigned_pm():
    st.session_state.pm_asignado = st.session_state.pm_asignado_key
    st.session_state.pm_asignado_key = None

pm_asignado = st.selectbox('Project Manager asignado',('Rodrigo Ramirez', 'Elian Sanabria','Sergio Santos'),index=None,placeholder="Selecciona encargado",key='pm_asignado_key', on_change=assigned_pm)

st.write(f'Representante de CUMA para el proyecto: {st.session_state.pm_asignado}')
st.divider()


# Entrada de dato para rfq_inquiry_date
def inquiry_date():
    st.session_state.rfq_inquiry_date = st.session_state.rfq_inquiry_date_key
    st.session_state.rfq_inquiry_date_key = None

rfq_inquiry_date = st.date_input("Fecha en que se solicita RFQ", format="DD/MM/YYYY", value = None,key='rfq_inquiry_date_key', on_change=inquiry_date)

st.write(f'Fecha en que se solicita la cotización {st.session_state.rfq_inquiry_date}')
st.divider()

# Entrada de dato para RFQ_email

def email_keywords():
    st.session_state.rfq_mail = st.session_state.rfq_mail_key
    st.session_state.rfq_mail_key = ''

rfq_mail = st.text_input("Palabras clave de correo",placeholder="Texto para buscar en correo",key='rfq_mail_key',on_change= email_keywords)

st.write(f'Texto clave a buscar en el correo: {st.session_state.rfq_mail}')
st.divider()

# Boton para crear RFQ

if st.button("Crear RFQ"):
     actualizar_consecutivo(st.session_state.client_input)
     st.success(f"Nuevo número de RFQ para el cliente {st.session_state.client_input}: {st.session_state.numero_RFQ}")
     

# Mostrar los datos a cargar

st.markdown("<h4 style = 'text-align: center;'>Datos a cargar </h4>", unsafe_allow_html=True)

    
new_data = {"RFQ_num":st.session_state.numero_RFQ,
            "RFQ_mail": st.session_state.rfq_mail,
            "RFQ_inquiry_date":st.session_state.rfq_inquiry_date,
            "Cliente": st.session_state.client_input,
            "Descripcion":st.session_state.descripcion
            }   

st.write(new_data)
st.warning(" Revisar si los datos estan correctos para poder cargarlos al sistema y confirmar")






# Confirmar informacion (boton) Subir diccionario a dataframe y borrar datos


#if st.button("Subir informacion a RFQ Control"):
   







