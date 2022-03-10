import pandas as pd
import streamlit as st
import base64

st.header ('''Price Prediction Model "Team Alpha":muscle::muscle:''')

#Sidebar
selection = st.sidebar.radio("HOME",
                ("FileUploader", "Data Visualization & Model Prediction","Presentation Video"))



#File Uploader

if selection == 'FileUploader':
    st.header("File Uploader")
    if st.checkbox("File Uploader"):
        upload_file = st.file_uploader(label="Upload Your CSV or Excel File", type=['csv','xlsx'])
        global df
        if upload_file is not None:
            print("Please Upload the required format ")
            try:
                 df = pd.read_csv(upload_file) 
            except Exception as e:
                print(e)
                df = pd.read_excel(upload_file)
            
                
        try:
             st.write(df)
        except Exception as e:
            print(e)
            print('Please Upload File ')
        if selection =='Data Preview':
            st.header("Data Preview")
     
     
     
     
    if st.checkbox("Show head of the data"):  
        st.write(df.head(5))
    if st.checkbox("show the last five data"):
        st.write(df.tail(5))
    if st.checkbox("Data Shape"):
        st.write(df.shape)
    

    st.title ("Data Cleaning")
    st.write("In this part we will check if data needs any cleaning")

    if st.checkbox("check null Values"):
        st.write(df.isnull().sum())
    
    if st.checkbox("Drop Null Values"):
        st.write(df.dropna(axis=0, how='any'))

    

#Data Model
if selection == 'Data Visualization & Model Prediction':
    st.write("In this wepage we will show our model that predicts diamond price based on different algorithms. Due to we cannot deploy the model itself on streamlit and give us wrong prediction, We have embeded the Jupyter Notebook file here")

    def show_pdf(file):
        with open(file, 'rb') as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src ="data:application/pdf;base64,{base64_pdf}" width = "800" height = "800" type="application/pdf"></iframe>'

        #Display file
        st.markdown(pdf_display,unsafe_allow_html=True)

    show_pdf("model.pdf")

    
#Presentation Video
if selection == "Presentation Video":
    st.title("Our Project Presentation")
    #st.image(image=Image.open('robel.jpg'), caption='Team Alpha' )
