from contextlib import contextmanager


class FingDB:
    def __init__(self):
        self.conn = "new"

class DBContext:
    
    def __init__(self, conn):
        self.conn = conn
   
    def __enter__(self):
        print("entering the context")
        self.conn = "started"

    def __exit__(self, *args):
        print("exiting the context")
        self.conn = "exit"

@contextmanager
def db_context(conn):
    print("starting the context", conn)
    try:
        yield
    finally:
        print("exiting the context", conn)

if __name__ == "__main__":
    db = FingDB()
    with DBContext(db.conn) as conn:
        print("this is from db")
        print(conn)

    with db_context(db.conn) as conn:
        print(conn)
