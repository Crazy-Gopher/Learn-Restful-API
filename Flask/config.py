class Config:
    # For inside the container
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@postgres_flask:5432/flask"

    # For outside the container or local machine
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/flask"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
