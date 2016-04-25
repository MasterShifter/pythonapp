def pageUp():
    html = '<!doctype html>'
    html += '<head>'
    html += '  <meta charset="utf-8">'
    html += ' <title>Prueba web Python</title>'
    html += '    <meta name="viewport" content="width=device-width, initial-scale=1">'
    html += '    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">'
    html += '    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>'
    html += '    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>'
    html += '</head>'
    html += '<body>'
    html += '<div class="container">'
    html += '  <header class="page-header"><img class="img-responsive" src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"/>'
    html += '<h1 class="text-center">Web de prueba</h1></header>'
    return html
	
def pageDown():
    html = '</div>'
    html += '</body>'
    html += '</html>'
    return html
	
def indexBody():
    html = '<h1>Página principal</h1>'
    html += '<a href="python_app/consulta">Acceder a consultas</a>'
    return html