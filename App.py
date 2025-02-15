import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
import io
pdf=None

st.title("PDF to word Converter")
st.write("Upload your PDF here:")
upload_file=st.file_uploader("",type=["pdf"])

if upload_file is not None:
    pdf=PdfReader(upload_file)
    st.write("PDF Sucessfully uploaded")

if pdf:
   st.write(f"Number of Pages:{len(pdf.pages)}")

   doc=Document()

   for page_num in range(len(pdf.pages)):
    page=pdf.pages[page_num]
    text=page.extract_text()
    doc.add_paragraph(text)

    word_io = io.BytesIO()

    doc.save(word_io)
    word_io.seek(0)
 
    st.download_button(
       label="Download Converted File",
       data=word_io,
       file_name="Converted.docx",
       mime="application/vnd.openxmlformats-officedocument.wordprocessngml.docx"
    )