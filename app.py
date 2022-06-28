import streamlit as st
from PIL import Image
import os
from image_processing import predict


st.set_page_config(layout="wide")

padding_top = 0

st.markdown(f"""
    <style>
        .reportview-container .main .block-container{{
            padding-top: {padding_top}rem;
        }}
    </style>""",
    unsafe_allow_html=True,
)

st.title("CLAY: Your AI-based Chest Xray Classifier 🧐🧬")

def load_image(image_file):
	img = Image.open(image_file)
	return img

uploaded_files= st.sidebar.file_uploader("",type=["png","jpg","jpeg"], 
                                          accept_multiple_files = True)

st.sidebar.header('')
st.sidebar.header('')
st.sidebar.header('')
st.sidebar.header('')
st.sidebar.header('')
st.sidebar.header('')
st.sidebar.header('')
st.sidebar.header('')
st.sidebar.header('')
st.sidebar.write('***')
st.sidebar.header('About')
st.sidebar.write("Equipped with a custom-trained VGG-19 Model, Clay will help you predict whether an Xray image is a case of Pneumonia, COVID+ or COVID-! <b>Read more [here](https://tinyurl.com/clay-xray).</b>", unsafe_allow_html=True)
                                 

if uploaded_files is not None:
    # TO See details
    for image_file in uploaded_files:
        with open(os.path.join("./images",image_file.name),"wb") as f:
            f.write((image_file).getbuffer())
            
        print('#############')
        str_filename = str(image_file.name)
        prediction = predict(str_filename)

        if prediction == 0:
            predicted_class = 'NEGATIVE'
        elif prediction == 1:
            predicted_class = 'PNEUMONIA'
        else:
            predicted_class = 'POSITIVE'

        st.success(predicted_class)
            
        file_details = {"filename":image_file.name,"filetype":image_file.type,
                        "prediction":predicted_class}
        st.write(file_details)
        st.image(load_image(image_file), width=250)
        
        #Saving upload
        
        
        # st.success("File Saved")
