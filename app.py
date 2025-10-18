import streamlit as st
from PIL import Image
import easyocr
import numpy as np
import sympy as sp
import re

# --- APP CONFIGURATION ---
st.set_page_config(
    page_title="Handwritten Math Solver",
    page_icon="🧮",
    layout="centered"
)

# --- EMOJI BASED STYLING ---
st.markdown("""
    <style>
    .stApp {
        background-color: #C82909;
        color: #fff;
        font-family: sans-serif;
    }
    </style>
""", unsafe_allow_html=True)


# --- HEADER SECTION ---
st.title("🧮 Handwritten Math Solver")
st.write("A fun AI-powered app that reads kids’ handwritten math problems and helps them learn!")

# --- SIDEBAR FOR INFO ---
with st.sidebar:
    st.header("About the App")
    st.write("""
        This mini-project supports **SDG 4: Quality Education** 🌍  
        Upload a photo of a handwritten math problem (like '3 + 2')  
        and the app will read and solve it automatically.
    """)
    st.info("Built with Streamlit + EasyOCR + SymPy")

# --- IMAGE UPLOAD SECTION ---
st.subheader("✏️ Upload your handwritten math image")
uploaded_file = st.file_uploader(
    "Choose an image (JPG, PNG)",
    type=["jpg", "jpeg", "png"]
)

# --- IMAGE PREVIEW ---
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")
    st.success("✅ Image uploaded successfully!")

    #--- OCR RECOGNITION ---
    # Convert image to numpy array
    imgage_np = np.array(image)

    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en']) #load english model 

    # Perform OCR on the image
    with st.spinner("🔍 Recognizing text..."):
        result = reader.readtext(imgage_np)

    # Extract recognized text
    st.subheader("📝 Recognized Text")
    if result :
        recognized_text = ' '.join([res[1] for res in result])
        st.code(f"**Recognized Math Problem:** {recognized_text}")
        st.success("✅ Text recognized successfully!")

        # --- CLEANING LOGIC ---
        def clean_expression(expr):
            expr = expr.replace('x', '*')
            expr = expr.replace('X', '*')
            expr = expr.replace('-', '-')
            expr = re.sub(r'[^0-9+\-*/().]', '', expr) # remove unwanted chars
            expr = expr.replace('÷', '/')
            return expr
        
        cleaned_expr = clean_expression(recognized_text)

        # --- MATH SOLVING SECTION ---
        st.subheader("🧠 Solving the Math Problem")

        if not cleaned_expr or cleaned_expr.strip() == "":
            st.error("❌ INVALID EXPRESSION")
        else:
                try:
                    # Attempt to parse and solve the recognized text
                    expression = sp.sympify(cleaned_expr)
                    st.success(f"✅ Solution: {expression}")
                    st.balloons()

                except (sp.SympifyError, ValueError) as e:
                    st.error("❌ UNEXPECTED CHARACTERS")
                    st.write(f"Output read: `{cleaned_expr}`")
                except ZeroDivisionError as e:
                    st.error("❌ Division by zero encountered in the expression.")
                except Exception as e:
                    st.error("❌ An unexpected error occurred while solving the problem. Try a clearer image or simpler arithmetic.")
    else:
        st.error("❌ No text recognized. Please try a clearer image.")

else:
    st.warning("Please upload an image of a handwritten math problem to get started.")


# --- FOOTER SECTION ---
st.markdown("---")
st.markdown("Developed with ❤️ to make learning fun and accessible for kids!")

