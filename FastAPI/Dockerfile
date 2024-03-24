FROM python:3.10-slim-bullseye
LABEL maintainer="Kapil Jain <kapiljain.jain93@gmail.com>"
EXPOSE 8001
WORKDIR /app 
COPY requirements.txt /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
