import sqlite3
def lista_to_fichero(res):
    file = open("jugadores.txt", "w")
    for dni in res:
        cur = con.cursor()
        cur.execute("select * from jugadores where dni = ?", (dni[0],))
        jugador = cur.fetchall()[0]
        if jugador[1!=None]:
            jugadorStr = jugador[0] + "," + jugador[1] + "," + str(jugador[2]) + "," + str(jugador[3]) + "\n"
        else:
            jugadorStr = jugador[0] + "," + str(jugador[2]) + "," + str(jugador[3]) + "\n"
        file.write(jugadorStr)
    file.close()


def filtrar_peso(pesoInferior, pesoSuperior):
    if pesoInferior>pesoSuperior:
        print("El valor inferior tiene que ser menor al superior")
    else:
        cur = con.cursor()
        result = cur.execute("select dni from jugadores where peso between " + str(pesoInferior) + " and " + str(pesoSuperior))
        return result.fetchall()

con = sqlite3.connect("equipo.db")
res = filtrar_peso(80, 85);
cur = con.cursor()
dniDeTodosLosJugadores = cur.execute("select dni from jugadores").fetchall()
lista_to_fichero(dniDeTodosLosJugadores)

con.close()
