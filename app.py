from flask import Flask, request, jsonify
import tempfile
import os
import zipfile

PORT = 8080 # Modificar de ser necesario
app = Flask(__name__)

# Método con datos para que medieval sepa qué tipo de archivos puede enviarle a este módulo 
# Y la etiqueta utilizada para identificar al estudio médico desde el front
@app.route('/metadata', methods=['GET'])
def metadata():
    response = {
        "acceptedFormats": ["zip"],
        "acceptedTest": "Nombre del Estudio que se mostrará en los reportes"
    }
    return jsonify(response)

# Health check para docker
@app.route('/health-check', methods=['GET'])
def healthCheck():
    response = {
        "status": 200,
        "description": "Up and Normal :)"
    }
    return jsonify(response)


# Funcion que analizará un archivo contenido en el request y retornará un listado de resultados de validación
# En este ejemplo se asume un archivo .zip que debe ser extraído para procesar sus contenidos
@app.route('/evaluation', methods=['POST'])
def validate():
    request_file = request.files['file'] #El archivo a analizar está nombrado 'file' dentro del request HTTP 
    
    # La respuesta falla con status 400 si por algun motivo no es .zip
    if not request_file.name.endswith('.zip'):
        return "Formato no soportado. Solo .zip", 400
    
    # Se extraen los archivos a una carpeta temporal que se destruye al finalizar el método
    tempdir = tempfile.TemporaryDirectory()
    with zipfile.ZipFile(request_file, 'r') as zf:
        zf.extractall(tempdir)
    
    extracted_files = os.listdir(tempdir)
    
    # Ya teniendo los archivos a mano, se analizan los archivos y se obtiene un resultado
    response = analyzeFiles(extracted_files)
    return jsonify(response)


# Se retorna una lista de resultados, cada resultado tiene un nombre/titulo, un mensaje/descripción del resultado, y un booleano indicando el resultado. 
# Esta función debería ser modificada agregando la lógica interna del módulo, respetando el formato del resultado.
def analyzeFiles(files):
    return [
        {
            "name": "Validación #1",
            "message": "Resultado de Validación #1",
            "approved": True
        },
        {
            "name": "Validación #2",
            "message": "Resultado de Validación #2",
            "approved": False
        }
    ]

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)
