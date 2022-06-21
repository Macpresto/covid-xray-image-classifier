import streamlit as st
from PIL import Image
import os

def load_image(image_file):
	img = Image.open(image_file)
	return img

st.sidebar.markdown("# Xray Classifier 🎈")
uploaded_files= st.sidebar.file_uploader("Upload Images",type=["png","jpg","jpeg"], 
                                          accept_multiple_files = True)

if uploaded_files is not None:
    # TO See details
    for image_file in uploaded_files:
        file_details = {"filename":image_file.name,"filetype":image_file.type,
                        "filesize":image_file.size}
        st.write(file_details)
        st.image(load_image(image_file), width=250)
        
        #Saving upload
        with open(os.path.join("./images",image_file.name),"wb") as f:
            f.write((image_file).getbuffer())
        
        st.success("File Saved")
