#importar o flask #sen -> envia mensagem dentro do tunel
from flask import Flask, render_template
from flask_socketio import SocketIO, send

#app
app = Flask(__name__)    #(__name__) nome do arquivo que esta criando -> variável padrão para criar app no python
tunel = SocketIO(app, cors_allowed_origins="*")  #criar tunel de comunicação

#Funcionalidade para enviar mensagens
@tunel.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True) #enviar mensagem para todos que estão conectados no tunel 

#primeira rota
@app.route("/")  #definir rota / @ atribuir funcionalidade 
def homepage():   #definir função
    return render_template("index.html")  #toda função tem que ter o tab para dentro ->


#roda o app através de um localhost
tunel.run(app, host="")

#websocket
#instalar as ferramentas -> pip install python-socketio flask-socketio simple-websocket 
