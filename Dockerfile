FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 6000
CMD [ "python", "app.py"]
