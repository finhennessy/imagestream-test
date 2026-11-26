# FROM python:3.12-ubi8
FROM registry.redhat.io/ubi8/python-312:latest
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY app.py app.py
CMD ["python3", "app.py"]