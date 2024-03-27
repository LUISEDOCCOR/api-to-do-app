from flask import Flask, jsonify, request
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from db import Todo
from db import User
from msg import getMsg

user = {
    "id": "1",
    "name": "Luis",
    "Password": "aldsakjsdkalsdajcb"
}

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "mysecretkey"
jwt = JWTManager(app)

#Login
@app.route("/login", methods=["POST"])
def login ():
    try:
        
        name = request.json["name"]
        password = request.json["password"]
        
        if (not (name == "" or password == "")):
            
            response = User(
                name=name,
                password=password
            ).Login()
            
            if response["mode"] == "success":
                access_token = create_access_token(identity=response["id"])
                return jsonify(access_token)
            else:
                return jsonify(response)
            
        else: return jsonify( getMsg(msg="The fields are empty", mode="error") )
    
    except Exception as e:
        print(e)
        return jsonify(getMsg(msg="There was an error in the request", mode="error"))
 
#SignUp
@app.route("/signup", methods=["POST"])
def signup ():
    try:
        
        name = request.json["name"]
        password = request.json["password"]
        
        if (not (name == "" or password == "")):
            
            response = User(
                name=name,
                password=password
            ).Create()
            
            if response["mode"] == "success":
                access_token = create_access_token(identity=response["id"])
                return jsonify(access_token)
            else:
                return jsonify(response)
            
        else: return jsonify( getMsg(msg="The fields are empty", mode="error") )
            
        
    except :
        return jsonify(getMsg(msg="There was an error in the request", mode="error"))

#borrar mi todo
@app.route("/todo/delete", methods=["DELETE"])
@jwt_required()
def deletetodo():
    try:
        id = request.json["id"]
        user_id = get_jwt_identity()
        if not id == "":
            return jsonify(Todo(id=id, user_id=user_id).Delete())
        else: return jsonify( getMsg(msg="The fields are empty", mode="error") )
    except:
        return jsonify(getMsg(msg="There was an error in the request", mode="error"))


#Obtener mis todos
@app.route("/todos", methods=["POST"])
@jwt_required()
def gettodos():
    if request.method == "POST":
        user_id = get_jwt_identity()
        return jsonify(Todo(user_id=user_id).Get())
    
    
#editar todo
@app.route("/todo/edit", methods=["PUT"])
@jwt_required()
def edittodo():
    try:
    
        title = request.json["title"]
        content = request.json["content"]
        id = request.json["id"]
        user_id = get_jwt_identity()
        
        if(not (title == "" or content == "" or id == "")):
            todo = Todo(
                user_id=user_id,
                id=id,
                title=title,
                content=content
            )
            return jsonify(todo.Edit())
        else: return jsonify( getMsg(msg="The fields are empty", mode="error") )    
    
    except:
        return jsonify(getMsg(msg="There was an error in the request", mode="error"))


#Crear todo
@app.route("/todo/create", methods=["POST"])
@jwt_required()
def createtodo ():
    try:
            title = request.json["title"]
            content = request.json["content"]
            user_id = get_jwt_identity()
            
            if(not (title == "" or content == "" )):
                Todo(
                    title= title,
                    content= content,
                    user_id= user_id
                ).Create()
                return jsonify (getMsg(msg="Successfully created"))
            
            else: return jsonify( getMsg(msg="The fields are empty", mode="error") )
                
    except:
        return jsonify(getMsg(msg="There was an error in the request", mode="error"))


if __name__ == "__main__":
    app.run(port=4321, debug=True)