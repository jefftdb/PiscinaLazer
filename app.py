from flask import Flask,render_template
import os
from controller.imagem_controller import *

todasAsImagens = Imagem_modal().todasAsImagens


app = Flask(__name__, template_folder=os.path.abspath('view/templates'), static_folder=os.path.abspath("view/static"))

from controller.calendario_controller import *


@app.route('/')
def index():
    return render_template('index.html',todasAsImagens = todasAsImagens,hoje = hoje_DataTime)




     