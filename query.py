#!/usr/bin/python

import mysql.connector as mariadb

def consultas():
    html = '<h2>Modulos:</h1>'
    html += showSelect("select idModulo, Alias, idGrupo from modulos LIMIT 10")
    html += '<h2>Grupos hola a todo el mundo:</h1>'
    html += showSelect("select * from grupos LIMIT 10")
    html += '<h2>Incidencias:</h1>'
    html += showSelect("select * from incidencias LIMIT 10")
    
    return html

def showSelect(sql):
    # Open database connection
    mariadb_connection = mariadb.connect(user='csi1', password='altair', host='altair1.altair.edu.es', database='csi2crm')
    
    # prepare a cursor object using cursor() method
    cursor = mariadb_connection.cursor()
    res = ''
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        res += '<table class="table table-bordered table-responsive table-striped text-center">'
        
        res += '<tr>'
        for desc in cursor.description:
            res += '<th class="text-center">%s</th>' % (str(desc[0]))
        res += '</tr>'
        
        for row in results:
            res += '<tr>'
            for field in row:
                try:
                    res += '<td>%s</td>' % (str(field))
                except:
                    res += ''
        # Now print fetched result
        res += '</tr>'
        res += '<tfoot><tr><td><b>resultados: %s</b></td></tr></tfoot>' % (len(results))
        res += '</table>'
    except:
        res += '<i>No hay resultados</i>'

    # disconnect from server
    cursor.close()
    mariadb_connection.close();
    return res;

