import streamlit as st
from PIL import Image
import os
from image_processing import predict


def load_image(image_file):
	img = Image.open(image_file)
	return img


st.sidebar.markdown("# Xray Classifier 🫁")
uploaded_files= st.sidebar.file_uploader("Upload Images",type=["png","jpg","jpeg"], 
                                          accept_multiple_files = True)

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
            
        file_details = {"filename":image_file.name,"filetype":image_file.type,
                        "prediction":predicted_class}
        st.write(file_details)
        st.image(load_image(image_file), width=250)
        
        #Saving upload
        
        
        # st.success("File Saved")
