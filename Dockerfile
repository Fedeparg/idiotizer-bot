FROM python:3.9.6-slim
COPY src/ .
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "python", "idiotizer.py" ]