FROM python:3.11-slim

# Instalar dependências do PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev gcc

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Criar diretório de app
WORKDIR /app

# Copiar requirements
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar projeto
COPY . .

# Comando default (pode mudar no docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

