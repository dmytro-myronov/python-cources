FROM python:3.12.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy your aliases file into the container
COPY dev_aliases.sh /etc/profile.d/dev_aliases.sh
RUN chmod +x /etc/profile.d/dev_aliases.sh
RUN echo "source /etc/profile.d/dev_aliases.sh" >> ~/.bashrc

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
