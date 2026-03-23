# Usa uma imagem leve de Python para otimizar espaço
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o ficheiro de dependências primeiro (otimização de cache de layer)
COPY requirements.txt .

# Instala as bibliotecas necessárias sem guardar cache do pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia o script, a config e o restante código para o container
COPY . .

# Comando que será executado ao iniciar o container
CMD ["python", "collector.py"]