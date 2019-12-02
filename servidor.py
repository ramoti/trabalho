from flask import Flask, json, jsonify
from flask import request
from hylson.py import Time, Penalidade, Campeonato, Partida
from playhouse.shortcuts import model_to_dict

app = Flask (__name__)

@app.route ('/', methods = ['GET'])
def main ():

    return foi

@app.route ('/listar_penalidade')
def listar_penalidade ():

    penalidade = list(map(model_to_dict, Penalidade.select()))
    response = jsonify({"penalidade":penalidadee})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route ('/listar_campeonato')
def listar_campeonato ():

    campeonato = list(map(model_to_dict, Campeonato.select()))
    response = jsonify({"campeonato": campeonato})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route ('/listar_partida')
def listar_partida ():

    partida = list(map(model_to_dict, Partida.select()))
    response = jsonify({"partida": partida})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
app.run (debug=True, port =4999 )
