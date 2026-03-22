FROM python:3.12-slim
# Cria utilizador para segurança
RUN useradd -m bruno_user
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Garante permissão nos ficheiros necessários
RUN chown -R bruno_user:bruno_user /app
USER bruno_user
# monitor.py conforme a estrutura de pastas
CMD ["python", "-u", "monitor.py"]