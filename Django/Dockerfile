FROM python:3.10-slim-bullseye
LABEL maintainer="Kapil Jain <kapiljain.jain93@gmail.com>"
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
