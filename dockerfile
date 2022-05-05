FROM python

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get update;apt-get upgrade;apt-get install -y unixodbc-dev;pip install -r requirements.txt

COPY . .

CMD ["python3","main.py"]
