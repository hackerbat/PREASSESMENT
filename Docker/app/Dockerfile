FROM python:3.5
COPY . /app
WORKDIR /app
EXPOSE 8080
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]