import streamlit as st
import os
import shutil
from ultralytics import YOLO
from PIL import Image
import glob

st.title("YOLOv8 Pose Detection")

upload_dir = "./input"
output_dir= "/runs/pose/predict"
os.makedirs(upload_dir, exist_ok=True)
uploaded_files = st.file_uploader("Upload images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        with open(os.path.join(upload_dir, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.read())

    st.success("Images uploaded successfully!")
    model = YOLO("yolov8x-pose.pt")  
    st.write("Processing images...")
    for img_path in glob.glob(f"{upload_dir}/*"):
        results = model(img_path, conf=0.1, show=False)  
        
    st.write("Processed images:")
    processed_images = glob.glob(f"{output_dir}/*")
    num_columns = 1  
    columns = st.columns(num_columns)
    
    for i, img_path in enumerate(processed_images):
        img = Image.open(img_path)
        with columns[i % num_columns]:  
            st.image(img, caption=os.path.basename(img_path), use_column_width=True)

    st.write("Download processed images:")
    for result_img_path in processed_images:
        st.download_button(
            label=f"Download {os.path.basename(result_img_path)}",
            data=open(result_img_path, "rb").read(),
            file_name=os.path.basename(result_img_path),
            mime="image/png"
        )
