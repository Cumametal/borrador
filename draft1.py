
import streamlit as st
import numpy as np
import pandas as pd

# creating containers

header = st.container()
dataset = st.container()
features = st.container()
userInput = st.container()

with header:
    st.title('CUMA')
    st.text('METAL MANUFACTURING SA DE CV')




with dataset:
    st.header('Control de RFQ - dataset')
    st.text('Este apartado es para el formato de cada nuevo RFQ creado')
    rfq_control = pd.read_csv('1 rfq control.csv', encoding='latin-1')
    st.write(rfq_control.head(10))

    # end dataset








with features:
    st.header('Features para actualizacion de archivo excel / SQL')
    st.text('Este apartado es para la actualización del archivo Excel/SQL')






with userInput:    
    st.header('Here is where the user input the data')

    #creating columns here
    sel_col , disp_col = st.columns(2)    

    #Now for every linecode I need to reefer the column name instead "st"

    #Creating a slider

    max_depth = sel_col.slider("what should be the max?", min_value = 10 , max_value = 100, value = 20, step=10)

    #How Do I get the input, I asign all the code to a variable, as stated up here
    #Now I can print the gotten value

    disp_col.write(max_depth)

    #Another Input here

    #Estimators

    n_estimators = sel_col.selectbox("how many trees should be there?", options= [100,200,300,'No limit'],index = 0)

    #Input feature

    input_feature = sel_col.text_input('Which feature should be use?', 'Colocar palabra clave para buscar en email')








