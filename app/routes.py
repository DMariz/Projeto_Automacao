from flask import Blueprint, render_template, request, redirect, url_for, flash
import fitz  # PyMuPDF
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('upload.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and file.filename.endswith('.pdf'):
        file_path = os.path.join('app/uploads', file.filename)
        file.save(file_path)
        text = extract_text_from_pdf(file_path)
        return render_template('result.html', text=text)
    
    flash('Invalid file format. Please upload a PDF.')
    return redirect(request.url)

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text
