FROM python:3

WORKDIR /app
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/index.py"]