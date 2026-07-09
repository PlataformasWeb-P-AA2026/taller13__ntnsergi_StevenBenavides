from config import usuario, clave 
from flask import Flask, request, render_template, redirect, url_for, flash
import requests
import json

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'una-clave-secreta-000001'

token = '72b0726d255e819dddf4680838b125a1edb9fe95'
headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/edificios')
def edificios():
    """
    """
    r = requests.get("http://localhost:8000/api/edificios/", headers=headers)
    print("---------------------")
    print(r.content)
    print("---------------------")
    
    data = json.loads(r.content)
    
    edificios_lista = data['results'] if isinstance(data, dict) and 'results' in data else data

    return render_template("listar_edificios.html", edificios=edificios_lista)


@app.route('/departamentos')
def departamentos():
    """
    """
    r = requests.get("http://localhost:8000/api/departamentos/", headers=headers)
    data = json.loads(r.content)
    departamentos_lista = data['results'] if isinstance(data, dict) and 'results' in data else data

    datos2 = []
    for d in departamentos_lista:
        datos2.append(
            {
                'id': d.get('id', ''),
                'propietario': d['propietario'],
                'costo': d['costo'],
                'num_cuartos': d['num_cuartos'],
                'edificio': obtener_edificio(d['edificio'])
            }
        )
    return render_template("listar_departamentos.html", departamentos=datos2)


# Funciones ayuda
def obtener_edificio(id_o_url):
    """
    
    """
    try:
        if str(id_o_url).startswith('http'):
            url = id_o_url
        else:
            url = f"http://localhost:8000/api/edificios/{id_o_url}/"
            
        r = requests.get(url, headers=headers)
        nombre_edificio = json.loads(r.content)['nombre']
        return nombre_edificio
    except Exception as e:
        return str(id_o_url)


@app.route('/crear_edificios', methods=['GET', 'POST'])
def crear_edificios():
    """
    """
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        tipo = request.form['tipo']

        edificio_data = {
            'nombre': nombre,
            'direccion': direccion,
            'ciudad': ciudad,
            'tipo': tipo
        }

        r = requests.post("http://localhost:8000/api/edificios/",
                              json=edificio_data,
                              headers=headers)

        print(f"Status Code (Crear Edificio): {r.status_code}")
        nuevo_edificio = json.loads(r.content)
        flash(f"Edificio '{nuevo_edificio['nombre']}' creado exitosamente!", 'success')
        return redirect(url_for('edificios'))

    return render_template('crear_edificios.html')


@app.route('/crear_departamentos', methods=['GET', 'POST'])
def crear_departamentos():
    """
    """
    
    r_edificios = requests.get("http://localhost:8000/api/edificios/", headers=headers)
    data = json.loads(r_edificios.content)
    edificios_disponibles = data['results'] if isinstance(data, dict) and 'results' in data else data

    if request.method == 'POST':
        propietario = request.form['propietario']
        costo = request.form['costo']
        num_cuartos = request.form['num_cuartos']
        edificio_val = request.form['edificio']

        departamento_data = {
            'propietario': propietario,
            'costo': costo,
            'num_cuartos': num_cuartos,
            'edificio': edificio_val
        }

        r = requests.post("http://localhost:8000/api/departamentos/",
                              json=departamento_data,
                              headers=headers)

        print(f"Status Code (Crear Departamento): {r.status_code}")
        nuevo_depto = json.loads(r.content)
        flash(f"Departamento del propietario '{nuevo_depto['propietario']}' creado exitosamente!", 'success')
        return redirect(url_for('departamentos'))

    return render_template('crear_departamentos.html', edificios=edificios_disponibles)


if __name__ == '__main__':
    app.run(debug=True)
