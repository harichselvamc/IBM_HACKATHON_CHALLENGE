# # # # import streamlit as st
# # # # from drowsiness import drowsiness_detection

# # # # def main():
# # # #     st.title("IBM HACK CHALLENGE")
# # # #     st.subheader("Drowsiness Detection using Dlib")
# # # #     st.write("Select the 'Start Drowsiness Detection' button to begin.")

# # # #     if st.button("Start Drowsiness Detection"):
# # # #         # Modify the arguments below as needed
# # # #         shape_predictor = "shape_predictor_68_face_landmarks.dat"
# # # #         alarm_path = "alarm.wav"
# # # #         webcam_index = 0
# # # #         drowsiness_detection(shape_predictor, alarm_path, webcam_index)

# # # # hide_st_style = """
# # # # <style>
# # # #     #MainMenu {visibility:hidden;}
# # # #     footer{visibility:hidden;}
# # # #     header{visibility:hidden;}
# # # # </style>
# # # # """

# # # # st.markdown(hide_st_style, unsafe_allow_html=True)

# # # # if __name__ == "__main__":
# # # #     main()


# # # import streamlit as st
# # # from streamlit_option_menu import option_menu
# # # from PIL import Image
# # # from ocr import perform_ocr_image, perform_ocr_camera
# # # from drowsiness import drowsiness_detection

# # # def show_ocr_button():
# # #     if st.button("OCR"):
# # #         st.experimental_rerun()

# # # def main():
# # #     st.title("IBM HACK CHALLENGE")
# # #     text = ""  # Initialize the text variable

# # #     with st.sidebar:
# # #         page = option_menu(
# # #             menu_title="Option menu",
# # #             options=["HOME", "OCR", "Drowsiness Detection"]
# # #         )
# # #     if page == "HOME":
# # #         st.subheader("Welcome to IBM Hackathon!")
# # #         st.write("Select the 'OCR' option in the sidebar to perform OCR on images.")
# # #         st.write("Select the 'Drowsiness Detection' option in the sidebar to detect drowsiness using Dlib.")
# # #         show_ocr_button()  # Show the OCR button on the home page

# # #     elif page == "OCR":
# # #         st.subheader("OCR Options")

# # #         # Add an expander for OCR options
# # #         with st.expander("Perform OCR on:", expanded=True):
# # #             ocr_option = st.radio("", ("Camera", "Upload"))

# # #             if ocr_option == "Camera":
# # #                 st.subheader("Camera OCR")

# # #                 # Perform OCR on the camera frames
# # #                 with st.spinner("Processing..."):
# # #                     text = perform_ocr_camera()

# # #             elif ocr_option == "Upload":
# # #                 st.subheader("Upload OCR")

# # #                 # Allow user to upload an image
# # #                 uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# # #                 if uploaded_image is not None:
# # #                     # Read the image from the uploaded file
# # #                     pil_image = Image.open(uploaded_image)

# # #                     # Display the uploaded image on the Streamlit app
# # #                     st.image(pil_image, caption="Uploaded Image", use_column_width=True)

# # #                     # Perform OCR on the uploaded image
# # #                     text = perform_ocr_image(pil_image)

# # #     elif page == "Drowsiness Detection":
# # #         st.subheader("Drowsiness Detection using Dlib")
# # #         st.write("Select the 'Start Drowsiness Detection' button to begin. press 'q' to stop")

# # #         if st.button("Start Drowsiness Detection"):
# # #             # Modify the arguments below as needed
# # #             shape_predictor = "shape_predictor_68_face_landmarks.dat"
# # #             alarm_path = "alarm.wav"
# # #             webcam_index = 0
# # #             drowsiness_detection(shape_predictor, alarm_path, webcam_index)

# # #     # Show the detected text
# # #     if text:
# # #         st.subheader("Detected Text:")
# # #         st.write(text)

# # # hide_st_style = """
# # # <style>
# # #     #MainMenu {visibility:hidden;}
# # #     footer {visibility:hidden;}
# # #     header {visibility:hidden;}
# # # </style>
# # # """

# # # st.markdown(hide_st_style, unsafe_allow_html=True)

# # # if __name__ == "__main__":
# # #     main()
# # import streamlit as st
# # from streamlit_option_menu import option_menu
# # from PIL import Image
# # from ocr import perform_ocr_image, perform_ocr_camera
# # from drowsiness import drowsiness_detection

# # # Global variable to stop drowsiness detection
# # stop_drowsiness = False

# # def show_ocr_button():
# #     if st.button("OCR"):
# #         st.experimental_rerun()

# # def main():
# #     global stop_drowsiness  # Declare the global variable
# #     st.title("IBM HACK CHALLENGE")
# #     text = ""  # Initialize the text variable

# #     with st.sidebar:
# #         page = option_menu(
# #             menu_title="Option menu",
# #             options=["HOME", "OCR", "Drowsiness Detection"]
# #         )
# #     if page == "HOME":
# #         st.subheader("Welcome to IBM Hackathon!")
# #         st.write("Select the 'OCR' option in the sidebar to perform OCR on images.")
# #         st.write("Select the 'Drowsiness Detection' option in the sidebar to detect drowsiness using Dlib.")
# #         show_ocr_button()  # Show the OCR button on the home page

# #     elif page == "OCR":
# #         st.subheader("OCR Options")

# #         # Add an expander for OCR options
# #         with st.expander("Perform OCR on:", expanded=True):
# #             ocr_option = st.radio("", ("Camera", "Upload"))

# #             if ocr_option == "Camera":
# #                 st.subheader("Camera OCR")

# #                 # Perform OCR on the camera frames
# #                 with st.spinner("Processing..."):
# #                     text = perform_ocr_camera()

# #             elif ocr_option == "Upload":
# #                 st.subheader("Upload OCR")

# #                 # Allow user to upload an image
# #                 uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# #                 if uploaded_image is not None:
# #                     # Read the image from the uploaded file
# #                     pil_image = Image.open(uploaded_image)

# #                     # Display the uploaded image on the Streamlit app
# #                     st.image(pil_image, caption="Uploaded Image", use_column_width=True)

# #                     # Perform OCR on the uploaded image
# #                     text = perform_ocr_image(pil_image)

# #     elif page == "Drowsiness Detection":
# #         st.subheader("Drowsiness Detection using Dlib")
# #         st.write("Select the 'Start Drowsiness Detection' button to begin. Press 'q' to stop.")

# #         if st.button("Start Drowsiness Detection"):
# #             # Modify the arguments below as needed
# #             shape_predictor = "shape_predictor_68_face_landmarks.dat"
# #             alarm_path = "alarm.wav"
# #             webcam_index = 0
# #             stop_drowsiness = False  # Reset the stop_drowsiness flag
# #             drowsiness_detection(shape_predictor, alarm_path, webcam_index)

# #         if st.button("Stop Drowsiness Detection"):
# #             stop_drowsiness = True  # Set the stop_drowsiness flag to stop the detection

# #     # Show the detected text
# #     if text:
# #         st.subheader("Detected Text:")
# #         st.write(text)

# # hide_st_style = """
# # <style>
# #     #MainMenu {visibility:hidden;}
# #     footer {visibility:hidden;}
# #     header {visibility:hidden;}
# # </style>
# # """

# # st.markdown(hide_st_style, unsafe_allow_html=True)

# # if __name__ == "__main__":
# #     main()
# import streamlit as st

# img_file_buffer = st.camera_input("Take a picture")

# if img_file_buffer is not None:
#     # To read image file buffer as bytes:
#     bytes_data = img_file_buffer.getvalue()
#     # Check the type of bytes_data:
#     # Should output: <class 'bytes'>
#     st.write(type(bytes_data))

import streamlit as st
from webcam import webcam

captured_image = webcam()
if captured_image is None:
    st.write("Waiting for capture...")
else:
    st.write("Got an image from the webcam:")
    st.image(captured_image)