from book import Book
from sqlalchemy import create_engine


class BookRepository(Book):
    def get_all_data(self):
        engine = create_engine(
            f"postgresql+psycopg2://.....:.....@localhost/aaaaaa")
        conn = engine.connect()
        all_data = conn.execute()
        return all_data
