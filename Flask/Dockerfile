FROM python:3.10-slim-bullseye
LABEL maintainer="Kapil Jain <kapiljain.jain93@gmail.com>"
EXPOSE 8002
WORKDIR /app
COPY requirements.txt /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app
ENV FLASK_APP=app
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "8002", "--reload"]
