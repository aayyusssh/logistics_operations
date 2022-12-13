import threading
from sqlalchemy import create_engine
import pandas as pd

class e(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        try:
            eng = create_engine('sqlite:///db.sqlite3')
            pd.read_sql_query('''update "MIS FULL" SET "Grn Number" = "Material Document";''',con= eng)

        except Exception as e:
            print(e)

