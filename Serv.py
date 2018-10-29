from flask import Flask, request
import mysql.connector

conexion = mysql.connector.connect(user="jorge", password="nano199699", database="Invernadero")
cursor = conexion.cursor()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

#/login/?usuario=jorge&password=nano199699

@app.route("/login/", methods=['GET'])
def login():
    usuario=request.args.get('usuario')
    password=request.args.get('password')
    userDB = Usuario(conexion, cursor)
    
    
    print(userDB.login(usuario, password))
    return usuario

app.run(debug=True)