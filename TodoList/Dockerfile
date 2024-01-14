FROM python:3.12
WORKDIR /app

COPY main.py /app
COPY requirements.txt /app
COPY static /app/static
COPY templates /app/templates

RUN pip install -r requirements.txt
EXPOSE 5000
CMD python main.py