import sqlite3
import bcrypt
from msg import getMsg

class db:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("db.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """ 
                CREATE TABLE IF NOT EXISTS todos(
                    id INTEGER PRIMARY KEY,
                    title VARCHAR(255),
                    content VARCHAR(255),
                    user_id INT
                )
            """
        )
        self.cursor.execute(
            """ 
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(255),
                    password VARCHAR(555)
                )
            """
        )
        self.conn.commit()


class Todo(db):
    def __init__(self, title=None, content=None, user_id=None, id=None):
        super().__init__()
        self.title =  title
        self.content =  content
        self.user_id =  user_id
        self.id = id

    def todoExist (self):
        query = "SELECT * FROM todos WHERE id == ? and user_id == ?"
        data = self.cursor.execute(query, (self.id, self.user_id))
        todo = data.fetchall()
        if todo:
            return True
        else : 
            return False

    def Create(self):    
        query = "INSERT INTO todos (title, content, user_id) VALUES (?,?,?)"
        self.cursor.execute(query, (self.title, self.content, self.user_id))
        self.conn.commit()

    def Get(self):
        query = "SELECT * FROM todos WHERE user_id == ?"
        data = self.cursor.execute(query, (self.user_id,))
        return data.fetchall()

    def Delete (self):
        if self.todoExist():
            query = "DELETE FROM todos WHERE id == ? and user_id == ?"
            self.cursor.execute(query, (self.id, self.user_id))
            self.conn.commit()
            return getMsg(msg="Successfully removed")    
        else:
            return getMsg(mode="Error", msg="The todo does not exist")

    def Edit(self):
        if self.todoExist():
            query = "UPDATE todos SET title = ?, content = ? WHERE id == ? and user_id == ?"
            self.cursor.execute(query, (self.title, self.content, self.id, self.user_id))
            self.conn.commit()
            return getMsg(msg="successfully edited")
        else:
            return getMsg(mode="Error", msg="The todo does not exist")  
        
class User (db):
    def __init__(self, name, password):
        super().__init__()
        self.name = name 
        self.password = password 
    
    def isRegistered(self):
        query = "SELECT * FROM users WHERE name = ?"
        data = self.cursor.execute(query, (self.name,))
        if data.fetchall():
            return True
        else:
            return False
        
    def Id (self):
        query = "SELECT * FROM users WHERE name = ?"
        data = self.cursor.execute(query, (self.name,))
        user = data.fetchall()
        print(user)
        return user[0][0]
             
         
    def Create(self):
        if not self.isRegistered():
            salt = bcrypt.gensalt()
            encodePassword = self.password.encode("utf-8")
            hashed = bcrypt.hashpw(encodePassword, salt) 
            query = "INSERT INTO users (name, password) VALUES (?, ?)"
            self.cursor.execute(query, (self.name, hashed))
            self.conn.commit()
            id =  self.Id()
            return {
                "mode": "success",
                "id": id         
            }
        else:
            return getMsg(msg="User already exists", mode="error")

    def Login(self):
        if self.isRegistered():
            encodePassword = self.password.encode("utf-8")
            query = "SELECT * FROM users WHERE name == ?"
            data = self.cursor.execute(query, (self.name,))
            user = data.fetchall()
            password = user[0][2]
            if bcrypt.checkpw(encodePassword, password):
                id = self.Id()
                return {
                    "mode": "success",
                    "id": id
                }
            else:
                return getMsg(mode="error", msg="Wrong password")
        else:
            return getMsg(msg="Username does not exist", mode="error")

