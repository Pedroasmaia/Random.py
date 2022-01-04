import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

#Construir as funcionalidades
@app.route('/')
def homepage():
  return('A API está no ar')
@app.route('/pegarvendas')
def pegarvendas():
  table = pd.read_csv('adv.csv')
  total_vendas = table['Vendas'].sum()
  resposta = {'total de vendas' : total_vendas}
  return jsonify(resposta)
#Rodar nossa api
app.run(host='0.0.0.0')

