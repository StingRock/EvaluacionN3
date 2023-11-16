from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def inicio():
    if request.method == 'POST':
        if 'ejercicio1' in request.form:
            return redirect(url_for('ejercicio1'))
        elif 'ejercicio2' in request.form:
            return redirect(url_for('ejercicio2'))

    return render_template('main.html')

########################################################################################################################

@app.route('/ejercicio1', methods=['GET', 'POST'])
def notas():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        if not (10 <= nota1 <= 70) or not (10 <= nota2 <= 70) or not (10 <= nota3 <= 70) or not (0 <= asistencia <= 100):
            return "Las notas deben estar entre 10 y 70, y la asistencia entre 0 y 100."

        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        return render_template('ejercicio1.html', promedio=promedio, estado=estado)

########################################################################################################################

def nombre_mas_largo(nombre1, nombre2, nombre3):
    nombres = [nombre1, nombre2, nombre3]
    nombre_largo = max(nombres, key=len)
    return nombre_largo, len(nombre_largo)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def contador():

    resultado = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

    if nombre1 and nombre2 and nombre3:
        nombre_largo, longitud = nombre_mas_largo(nombre1, nombre2, nombre3)
        resultado = {'nombre_largo': nombre_largo, 'longitud': longitud }

    return render_template('ejercicio2.html', resultado=resultado)

########################################################################################################################

if __name__ == '__main__':
    app.run(debug=True)