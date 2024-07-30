from app import app
from flask import render_template, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    pdf_directory = request.form['pdf_directory']
    template_path = request.form['template_path']
    output_directory = request.form['output_directory']
    # Aqui você implementará a lógica de processamento
    return "Processamento concluído!"
