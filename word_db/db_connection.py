import mysql.connector
import csv
import creds

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=creds.password,
    database="pecha_schema",
    auth_plugin=creds.auth_plugin
)
mycursor = mydb.cursor()

# user_db has a user_id : 1 -> k
"""
! Separate user_db ! 
Select specific customer_id first, to return previous value. then use UPDATE to add ",entry" this will be top k, 
after it is maxed then remove from beginning
"""


class interact_with_db: 
    
    def __init__(self, entries = []):
        self.entries = entries

    def search_db(self, word): # supports search of a single word
        sql = f"SELECT * FROM manual_STLC_SQL WHERE english = '{word}'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult[0]
    
    def insert_into_db(self): # can support multiple entries.
        sql = "INSERT INTO manual_STLC_SQL (english, tibetan, phonetic) VALUES (%s, %s, %s)"
        mycursor.executemany(sql, self.entries)
        mydb.commit()
        print(mycursor.rowcount, "record(s) were inserted.")
    
    def delete_single_from_db(self): 
        mycursor.execute(self.query)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
    
    def delete_all_from_db(self):
        sql = "DELETE FROM manual_STLC_SQL"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "records deleted")


class interpret_csv: # transform csv into a list of tuples  
    def __init__(self, filename: str):
        self.filename = filename
    
    def csv_to_tuple(self) -> list:
        with open(self.filename) as f:
            next(f)
            reader = csv.reader(f)
            lst = list(tuple(line) for line in reader)
        return lst

# A = interpret_csv('manual_STLC.csv').csv_to_tuple()
# db = interact_with_db(A).insert_into_db()








