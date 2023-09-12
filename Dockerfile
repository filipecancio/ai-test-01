FROM python:3

WORKDIR /app
RUN pip install nltk

COPY . .

CMD ["python", "app/index.py"]