from tkinter.tix import Tree
from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS

from gestor import Gestor
from xml.etree import ElementTree as ET

app = Flask(__name__)
app.config["DEBUG"]=True

CORS(app)
#python manage.py runserver
gestor=Gestor()
idcancion=''
@app.route('/')
def home():
    return "TODO VA BIEN"

@app.route('/agregarCancion',methods=['POST'])
def agregarCancion():
    json=request.get_json()
    gestor.agregar_cancion(json['nombre'],json['artista'],json['genero'],json['anio'])
    return jsonify({'ok':True,'message':'Cancion añadida con exito'}),200

@app.route('/agregarCanciones',methods=['POST'])
def agregarCanciones():
    xml=request.data.decode('utf-8')
    raiz=ET.XML(xml)
    for elemento in raiz:
        if elemento.tag == 'playlistClientes':
            for subelemento in elemento:
                if subelemento.tag == 'playlist': 
                    idplay=subelemento.get('id')
                    for sub in subelemento:
                        if sub.tag == 'nitCliente':
                            nit =sub.text
                        elif sub.tag == 'vinyl':
                            vinyl = sub.text
                        elif sub.tag == 'compacto':
                            compacto = sub.text
                        elif sub.tag == 'categoria':
                            categoria = sub.text
                        elif sub.tag == 'canciones':
                            for sub1 in sub:
                                if sub1.tag=='cancion':
                                    global idcancion
                                    idcancion=sub1.get('id')
                                    for sub2 in sub1:
                                        if sub2.tag=='nombre':
                                            nombre=sub2.text
                                        elif sub2.tag=='anio':
                                            anio = sub2.text
                                        elif sub2.tag=='artista':
                                            artista = sub2.text
                                        elif sub2.tag=='genero':
                                            genero = sub2.text
                                    gestor.agregar_cancion(nombre,anio,artista,genero)
    return jsonify({'ok':True,'message':'Canciones cargadas con exito'}),200

@app.route('/canciones',methods=['GET'])
def get_canciones():
    c=gestor.obtener_canciones()
    return jsonify(c),200

@app.route('/ayuda')
def ayuda():
    return "aca aparece mi nombre"

@app.route('/eliminar', methods=['DELETE'])
def eliminar():
  xml_file = request.files['xml_file']
  song_id = request.form['song_id']

  # Parsea el archivo XML de la playlist
  tree = ET.parse(xml_file)
  root = tree.getroot()

  # Busca la canción con el ID especificado
  song = None
  for element in root.iter():
    if element.tag == 'cancion' and element.attrib['id'] == song_id:
      song = element
      break

  if song is not None:
    # Elimina la canción del árbol XML
    root.remove(song)

    # Graba el archivo XML de la playlist
    tree.write(xml_file)
    return 'Canción eliminada'
   

if __name__ =="__main__":
    app.run(debug=True)