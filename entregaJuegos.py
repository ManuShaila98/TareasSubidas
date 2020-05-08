import json
import PySimpleGUI as sg
import ahorcadoConFunciones as ah
import reversegam as otte
import tictactoeModificado as TTT

def guardarDatos (juego):
	archivo = open("DatosJugadores.txt", "w")
	print("Ingresa tu nombre")
	nom = input()
	print("Ingresa tu email")
	mail = input()
	datos = [{"Nombre": nom, "Email": mail, "Juego": juego}]
	json.dump(datos, archivo)
	archivo.close()

def main(args):

	layout = [
		[sg.Text('Elija el juego', size=(25,1), justification='center', background_color='#DC8F7F', text_color='black', font='Helvetica')],
		[sg.Button('Ahorcado', key='ahorcado'), sg.Button('Ta-Te-Ti', key='TTT'), sg.Button('Otello', key='otte'), sg.Button('Salir', key='quit')]
	]

	window = sg.Window('Seleccion de juego', background_color='#DC8F7F', size=(350, 100)).Layout(layout)

	sigue = True

	while sigue:
		event, values = window.Read()
		if event in (None, 'quit'):
			sigue = False
			break
		if (event == 'ahorcado'):
			ah.main()
			guardarDatos('ahorcado')
		elif (event == 'TTT'):
			TTT.main()
			guardarDatos('Ta-Te-Ti')
		elif (event == 'otte'):
			otte.main()
			guardarDatos('Otello')
	window.Close()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


#Utilize JSON para guardar los datos ya que es mejor utilizarlo par aarchivos de texto. Y para guardar los datos se debe utilizar una lista de diccionarios.	
