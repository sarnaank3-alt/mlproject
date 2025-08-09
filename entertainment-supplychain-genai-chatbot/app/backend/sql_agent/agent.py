from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

class SQLAgent:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)

    def execute_query(self, query, params=None):
        try:
            with self.engine.connect() as connection:
                result = connection.execute(text(query), params)
                return [dict(row) for row in result]
        except SQLAlchemyError as e:
            print(f"Error executing query: {e}")
            return None

    def safe_query(self, query, params=None):
        # Implement additional safety checks if necessary
        return self.execute_query(query, params)