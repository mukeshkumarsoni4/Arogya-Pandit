from dotenv import load_dotenv
load_dotenv()

import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai
from docx import Document  # Import to handle DOC/DOCX files

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get the response from the Gemini model
def get_gemini_response(input_text, content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, content[0], prompt])
    return response.text

# Function to handle PDF uploads and convert the first page to an image
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to images
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        # Convert the first page to bytes
        first_page = images[0]
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        # Encode the image to base64
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No PDF file uploaded")

# Function to handle DOC/DOCX uploads and extract text
def input_doc_setup(uploaded_file):
    if uploaded_file is not None:
        # Read DOC/DOCX file
        doc = Document(uploaded_file)
        doc_text = "\n".join([para.text for para in doc.paragraphs])

        # Split text into parts (if needed for large content)
        doc_parts = [
            {
                "mime_type": "text/plain",
                "data": base64.b64encode(doc_text.encode()).decode()  # encode to base64
            }
        ]
        return doc_parts
    else:
        raise FileNotFoundError("No DOC/DOCX file uploaded")

# Function to get the top 10 interview questions based on the resume
def get_top_10_interview_questions(resume_content, job_description):
    prompt = f"""
    Based on the resume content and the provided job description, generate the top 10 interview questions
    that the candidate is likely to be asked in a technical interview. The questions should focus on the 
    candidate's skills, experience, and qualifications relevant to the job description.
    """
    response = get_gemini_response(job_description, resume_content, prompt)
    return response

## Streamlit App

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

# Input for the job description
input_text = st.text_area("Job Description: ", key="input")

# Upload options: PDF or DOC/DOCX
uploaded_file = st.file_uploader("Upload your resume (PDF or DOC/DOCX)...", type=["pdf", "docx"])

if uploaded_file is not None:
    file_type = uploaded_file.type
    if file_type == "application/pdf":
        st.write("PDF Uploaded Successfully")
    elif file_type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
        st.write("DOC/DOCX Uploaded Successfully")

# Buttons for different functionalities
submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage Match")
submit4 = st.button("Top 10 Interview Questions")  # New button for interview questions

# Prompts for the AI model
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Provide the percentage match between the resume and 
the job description, followed by missing keywords, and final thoughts.
"""

# Processing for the "Tell Me About the Resume" button
if submit1:
    if uploaded_file is not None:
        file_type = uploaded_file.type
        if file_type == "application/pdf":
            # Handle PDF file
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_text, pdf_content, input_prompt1)
        elif file_type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
            # Handle DOC/DOCX file
            doc_content = input_doc_setup(uploaded_file)
            response = get_gemini_response(input_text, doc_content, input_prompt1)
        
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.write("Please upload the resume")

# Processing for the "Percentage Match" button
elif submit3:
    if uploaded_file is not None:
        file_type = uploaded_file.type
        if file_type == "application/pdf":
            # Handle PDF file
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_text, pdf_content, input_prompt3)
        elif file_type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
            # Handle DOC/DOCX file
            doc_content = input_doc_setup(uploaded_file)
            response = get_gemini_response(input_text, doc_content, input_prompt3)
        
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.write("Please upload the resume")

# Processing for the "Top 10 Interview Questions" button
elif submit4:
    if uploaded_file is not None:
        file_type = uploaded_file.type
        if file_type == "application/pdf":
            # Handle PDF file
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_top_10_interview_questions(pdf_content, input_text)
        elif file_type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
            # Handle DOC/DOCX file
            doc_content = input_doc_setup(uploaded_file)
            response = get_top_10_interview_questions(doc_content, input_text)
        
        st.subheader("Top 10 Interview Questions Based on the Resume:")
        st.write(response)
    else:
        st.write("Please upload the resume")



























        