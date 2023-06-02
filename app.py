from flask import Flask, render_template, request
from flask_socketio import SocketIO
import secrets
from password_get import pegarsenha, lersenha, salvarUsername
from info import info
from users import search, users


app = Flask(__name__)
app.debug = True
app.secret_key = secrets.token_hex(16)
socket = SocketIO(app)
cous = 0
userlist = []
user = {}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/logar', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    log = lersenha(username, password)
    if log:

        return chat()
    else:
        return error()


@app.route('/cadastro')
def pag_cadastro():
    return render_template('cadastro.html')


@app.route('/cadastrar', methods=['POST'])
def cadastro():
    username_cad = request.form['username_cad']
    password_cad = request.form['password_cad']

    Cad = lersenha(password_cad, username_cad)
    print(bool(lersenha(password_cad, username_cad)))
    if Cad:
        return error(info=info(3))
    else:
        pegarsenha(username_cad, password_cad)
        return error(info=info(2))


@app.route('/chat', methods=['GET'])
def chat():

    username = request.form['username']
    ip_user = ip()
    user[ip()] = username
    users(user)
    retUs2, retUs1 = salvarUsername(username)
    nome = search(ip_user)
    return render_template(
        'chat.html', nome=nome, nome1=user, username=search(ip_user)
    )


@app.route('/info', methods=['POST'])
def error(info=info(1)):
    return render_template('info.html', msg=info)

@app.route('/')
def ip():
    ip_address = request.remote_addr
    return ip_address


@socket.on('disconnect')
def on_disconnect():
    global cous
    cous = -1
    print('Usuario desconectado', cous, ip())


@socket.on('connect')
def on_connect():
    global cous
    cous += 1
    print('Usuario conectado', cous, ip(), user)

    @socket.on('chat message')
    def on_chat_message(msg):
        socket.emit('chat message', msg)


if __name__ == '__main__':
    socket.run(app.run(host='0.0.0.0'))
