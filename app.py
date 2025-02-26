from flask import Flask, request, jsonify 
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=[])

@app.route('/test', methods=['GET'])
def test ():
    return jsonify({'menssage' : 'Hello,word!'})

@app.route('/usuario/novo', methods = ['POST'])
def criar__novo__usuario():
    novo_usuario = request.json
    print (novo_usuario)
    return jsonify({ 
        'user': novo_usuario,
        'message': 'Usuário criado com sucesso!'
        })  

if __name__== '__main__' :
    app.run(port=5000)