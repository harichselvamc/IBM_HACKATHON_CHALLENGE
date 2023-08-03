import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from ocr import perform_ocr_image, perform_ocr_camera

def show_ocr_button():
    if st.button("OCR"):
        st.experimental_rerun()
def main():
    
    
    

    st.title("IBM HACK CHALLENGE")
    text = ""  # Initialize the text variable

    with st.sidebar:
        page=option_menu(
        menu_title="Option menu",
        options=["HOME","OCR"]
    )
    if page == "Home":
        st.subheader("Welcome to IBM Hackathon!")
        st.write("Select the 'OCR' option in the sidebar to perform OCR on images.")
        st.subheader("Welcome to IBM Hackathon!")
        st.write("Select the 'OCR' option in the sidebar to perform OCR on images.")
        show_ocr_button()  # Show the OCR button on the home page


    elif page == "OCR":
        st.subheader("OCR Options")

        # Add an expander for OCR options
        with st.expander("Perform OCR on:", expanded=True):
            ocr_option = st.radio("", ("Hold","Camera", "Upload"))

            if ocr_option == "Camera":
                st.subheader("Camera OCR")

                # Perform OCR on the camera frames
                with st.spinner("Processing..."):
                    text = perform_ocr_camera()

            elif ocr_option == "Upload":
                st.subheader("Upload OCR")

                # Allow user to upload an image
                uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

                if uploaded_image is not None:
                    # Read the image from the uploaded file
                    pil_image = Image.open(uploaded_image)

                    # Display the uploaded image on the Streamlit app
                    st.image(pil_image, caption="Uploaded Image", use_column_width=True)

                    # Perform OCR on the uploaded image
                    text = perform_ocr_image(pil_image)

    # Show the detected text
    if text:
        st.subheader("Detected Text:")
        st.write(text)
    
hide_st_style = """
<style>
    #MainMenu {visibility:hidden;}
    footer{visibility:hidden;}
    header{visibility:hidden;}
</style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)



if __name__ == "__main__":
    main()