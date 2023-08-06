from flask import Flask, make_response
from markupsafe import escape
from flask import render_tamplate
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_tamplate("index.html")

@app.route("/cad/usuario")
def usuario():
    return render_tamplate('usuario.html')

@app.route("/cad/caduser",methods=['POST'])
def caduser():
    return request.form


@app.route("/anuncios")
def anuncio():
    return render_tamplate('anuncio.html')

@app.route("/categoria")
def categoria():
    return render_tamplate('cateroria.html')

@app.route("/relatorio/compra_venda")
def relatorios():
    return render_tamplate('relatorios_html')












