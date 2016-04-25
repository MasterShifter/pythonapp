# -*- coding: utf-8 -*-
from sys import path
path.append('/var/www/html/pythonapp')

import query
import default

def application(environ, start_response):
    peticion = environ['REQUEST_URI'] 	
    output = default.pageUp()

    if peticion.startswith('/python_app/consulta'): 
        output += query.consultas()
    elif peticion.startswith('/python_app/tambien'):
        output += query.consultas()
    else:
        output += default.indexBody()
    output += default.pageDown()

    start_response('200 OK', [('Content-Type', 'text/html')])
    return output