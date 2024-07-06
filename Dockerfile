FROM python:3.9-slim
WORKDIR /application
COPY application/ .
RUN pip install -r requirements.txt
CMD ["python", "application.py"]