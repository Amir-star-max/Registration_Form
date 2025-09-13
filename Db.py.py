import sqlite3

class Database:
    def __init__(self,Path:str):
        self.con = sqlite3.connect(Path)
        self.cur = self.con.cursor() 
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Registration_Form 
                                    (Id INTEGER PRIMARY KEY ,Name TEXT , Lastname TEXT , Course TEXT , Gender TEXT , Tel TEXT)''')
        self.con.commit()

    def insert(self,name:str,lname:str,course:str,gender:str,tel:int):
        self.cur.execute('''INSERT INTO Registration_Form VALUES (NULL,?,?,?,?,?)''',(name,lname,course,gender,tel))
        self.con.commit()

    def select(self):
        self.cur.execute('''SELECT * FROM Registration_Form''')
        records = self.cur.fetchall()
        return records

    def end(self):
        self.con.close()  

    def delete(self,id):
        self.cur.execute('DELETE FROM Registration_Form WHERE id = ?',(id,))
        self.con.commit()

    def update(self,id,name,lname,tel,gender):
        self.cur.execute('''UPDATE
                             Registration_Form 
                                SET Name=? ,
                                Lastname=? , 
                                Gender=?,
                                Tel=?
                         WHERE Id = ?''',(name,lname,gender,tel,id))
        self.con.commit()          
        
