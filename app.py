import connexion

def hello_world():
    return "Hello World!"

app = connexion.App(__name__, specification_dir='.', server='tornado', options={'swagger_ui':True})
app.add_api('swagger.yaml')
app.run(port=8080)