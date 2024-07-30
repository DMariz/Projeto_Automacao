# Usa uma imagem base oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de requerimentos e instala as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia o conteúdo da aplicação para o container
COPY . .

# Expõe a porta que a aplicação Flask vai rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python3", "run.py"]
