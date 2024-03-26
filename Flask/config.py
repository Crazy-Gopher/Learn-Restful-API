class Config:
    def _init_(self):
        self.SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/flask"
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
