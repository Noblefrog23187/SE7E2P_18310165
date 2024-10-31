
import os
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import random

# Datos del juego
historias = [
     {
        'descripcion': "Un miembro de la familia ha sido asesinado en la casa. Encuentra al culpable.",
        'personas': ['Mamá', 'Papá', 'Hijo mayor', 'Hijo mediano', 'Hijo menor'],
        'objetos': ['Cuchillo', 'Pistola', 'Veneno', 'Cuerda', 'Llave Inglesa'],
        'lugares': ['Cocina', 'Sala de estar', 'Jardín', 'Garaje', 'Dormitorio'],
        'asesino': 'Hijo mediano',
        'objeto_asesino': 'Cuerda',
        'lugar_asesinato': 'Garaje',
        'pistas': {
            'Mamá': 'Mamá estaba cocinando en la cocina durante el asesinato.',
            'Papá': 'Papá fue visto en la sala de estar mirando televisión.',
            'Hijo mayor': 'Hijo mayor fue visto saliendo del garaje poco después del asesinato.',
            'Hijo mediano': 'Hijo mediano fue visto cerca del garaje minutos antes del asesinato.',
            'Hijo menor': 'Hijo menor estaba durmiendo en su dormitorio en el momento del asesinato.',
            'Cuchillo': 'El cuchillo no parece haber sido usado en el crimen.',
            'Pistola': 'No se escucharon disparos en la casa.',
            'Veneno': 'No hay signos de envenenamiento en el cuerpo.',
            'Cuerda': 'Parece que la víctima fue estrangulada con una cuerda.',
            'Llave Inglesa': 'La llave inglesa está limpia, no se utilizó.',
            'Cocina': 'La cocina estaba llena de actividad y no hay indicios de lucha.',
            'Sala de estar': 'La sala de estar estaba tranquila, nadie reportó nada sospechoso.',
            'Jardín': 'El jardín es un lugar tranquilo, no se escucharon ruidos fuertes.',
            'Garaje': 'El garaje muestra signos de una pelea.',
            'Dormitorio': 'El dormitorio estaba en silencio, Hijo menor fue visto durmiendo.'
        }
    },
    {
        'descripcion': "Un miembro de la familia ha sido asesinado en la casa. Encuentra al culpable.",
        'personas': ['Mamá', 'Papá', 'Hijo mayor', 'Hijo mediano', 'Hijo menor'],
        'objetos': ['Hacha', 'Veneno', 'Cuchillo', 'Cadena', 'Llave Inglesa'],
        'lugares': ['Jardín', 'Sala', 'Cocina', 'Garaje', 'Sótano'],
        'asesino': 'Hijo mayor',
        'objeto_asesino': 'Cuchillo',
        'lugar_asesinato': 'Jardín',
        'pistas': {
            'Mamá': 'Mamá estaba limpiando la cocina en el momento del asesinato.',
            'Papá': 'Papá estaba viendo televisión en la sala.',
            'Hijo mayor': 'Hijo mayor fue visto saliendo del jardín después del asesinato.',
            'Hijo mediano': 'Hijo mediano estaba reparando el coche en el garaje.',
            'Hijo menor': 'Hijo menor estaba en el sótano jugando con herramientas.',
            'Hacha': 'No se utilizó el hacha en el asesinato.',
            'Veneno': 'No hay signos de envenenamiento.',
            'Cuchillo': 'El cuchillo fue encontrado con rastros de sangre.',
            'Cadena': 'La cadena no fue usada para el crimen.',
            'Llave Inglesa': 'La llave inglesa no muestra signos de uso.',
            'Jardín': 'El jardín está apartado y tranquilo, un lugar ideal para el crimen.',
            'Sala': 'La sala estaba tranquila, no se reportó actividad sospechosa.',
            'Cocina': 'La cocina estaba limpia y en orden.',
            'Garaje': 'El garaje estaba ocupado, pero no se oyó nada extraño.',
            'Sótano': 'El sótano estaba desordenado, pero no se escucharon ruidos.'
        }
    },
    # Caso 3
    {
        'descripcion': "Un miembro de la familia ha sido asesinado en la casa. Encuentra al culpable.",
        'personas': ['Mamá', 'Papá', 'Hijo mayor', 'Hijo mediano', 'Hijo menor'],
        'objetos': ['Martillo', 'Veneno', 'Cuerda', 'Pistola', 'Cuchillo'],
        'lugares': ['Sótano', 'Cocina', 'Jardín', 'Sala de estar', 'Garaje'],
        'asesino': 'Papá',
        'objeto_asesino': 'Martillo',
        'lugar_asesinato': 'Sótano',
        'pistas': {
            'Mamá': 'Mamá estaba regando las plantas en el jardín.',
            'Papá': 'Papá fue visto entrando en el sótano antes del asesinato.',
            'Hijo mayor': 'Hijo mayor estaba en la sala de estar jugando videojuegos.',
            'Hijo mediano': 'Hijo mediano estaba en su dormitorio haciendo la tarea.',
            'Hijo menor': 'Hijo menor estaba comiendo en la cocina.',
            'Martillo': 'El martillo fue encontrado con rastros de sangre.',
            'Veneno': 'No se encontraron signos de envenenamiento.',
            'Cuerda': 'No hay indicios de que la cuerda se haya usado.',
            'Pistola': 'La pistola no parece haber sido disparada.',
            'Cuchillo': 'El cuchillo estaba en su lugar, sin signos de uso.',
            'Sótano': 'El sótano está desordenado y hay señales de lucha.',
            'Cocina': 'La cocina está limpia y ordenada.',
            'Jardín': 'El jardín estaba tranquilo, sin nada fuera de lo común.',
            'Sala de estar': 'La sala de estar estaba en silencio, sin actividad inusual.',
            'Garaje': 'El garaje estaba vacío, no se oyó nada extraño.'
        }
    },
    # Caso 4
    {
        'descripcion': "Un miembro de la familia ha sido asesinado en la casa. Encuentra al culpable.",
        'personas': ['Mamá', 'Papá', 'Hijo mayor', 'Hijo mediano', 'Hijo menor'],
        'objetos': ['Llave Inglesa', 'Cadena', 'Cuchillo', 'Hacha', 'Veneno'],
        'lugares': ['Garaje', 'Sala de estar', 'Dormitorio', 'Jardín', 'Cocina'],
        'asesino': 'Mamá',
        'objeto_asesino': 'Llave Inglesa',
        'lugar_asesinato': 'Garaje',
        'pistas': {
            'Mamá': 'Mamá fue vista saliendo del garaje justo después del asesinato.',
            'Papá': 'Papá estaba durmiendo en el dormitorio en el momento del asesinato.',
            'Hijo mayor': 'Hijo mayor estaba viendo televisión en la sala de estar.',
            'Hijo mediano': 'Hijo mediano estaba jugando en el jardín.',
            'Hijo menor': 'Hijo menor estaba en la cocina preparando algo para comer.',
            'Llave Inglesa': 'La llave inglesa fue encontrada con rastros de sangre.',
            'Cadena': 'La cadena no muestra signos de uso.',
            'Cuchillo': 'El cuchillo estaba limpio y guardado en su lugar.',
            'Hacha': 'El hacha no parece haber sido utilizada.',
            'Veneno': 'No hay signos de envenenamiento.',
            'Garaje': 'El garaje muestra signos de una pelea.',
            'Sala de estar': 'La sala de estar estaba tranquila, sin actividad inusual.',
            'Dormitorio': 'El dormitorio estaba en silencio, Papá estaba durmiendo.',
            'Jardín': 'El jardín estaba tranquilo, sin nada fuera de lo común.',
            'Cocina': 'La cocina estaba desordenada, pero no parece haber ninguna evidencia importante.'
        }
    },
    # Caso 5
    {
        'descripcion': "Un miembro de la familia ha sido asesinado en la casa. Encuentra al culpable.",
        'personas': ['Mamá', 'Papá', 'Hijo mayor', 'Hijo mediano', 'Hijo menor'],
        'objetos': ['Cuchillo', 'Veneno', 'Martillo', 'Pistola', 'Cuerda'],
        'lugares': ['Cocina', 'Garaje', 'Sala de estar', 'Jardín', 'Dormitorio'],
        'asesino': 'Hijo menor',
        'objeto_asesino': 'Veneno',
        'lugar_asesinato': 'Cocina',
        'pistas': {
            'Mamá': 'Mamá estaba en el jardín cuidando las plantas.',
            'Papá': 'Papá estaba trabajando en el coche en el garaje.',
            'Hijo mayor': 'Hijo mayor estaba en la sala de estar viendo televisión.',
            'Hijo mediano': 'Hijo mediano estaba estudiando en su dormitorio.',
            'Hijo menor': 'Hijo menor fue visto entrando a la cocina antes del asesinato.',
            'Cuchillo': 'El cuchillo no fue usado en el crimen.',
            'Veneno': 'Se encontró veneno en la comida de la víctima.',
            'Martillo': 'El martillo estaba guardado en su sitio, sin signos de uso.',
            'Pistola': 'La pistola no fue disparada.',
            'Cuerda': 'No se utilizó la cuerda en el asesinato.',
            'Cocina': 'La cocina muestra signos de que alguien manipuló la comida.',
            'Garaje': 'El garaje estaba tranquilo, Papá estaba ocupado con el coche.',
            'Sala de estar': 'La sala estaba tranquila, no hubo nada inusual.',
            'Jardín': 'El jardín estaba en paz, sin actividad sospechosa.',
            'Dormitorio': 'El dormitorio estaba tranquilo, Hijo mediano estaba estudiando.'
        }
    }
]

# Funciones del juego
def iniciar_juego():
    global caso
    caso = random.choice(historias)
    texto_descripcion.set(caso['descripcion'])
    # Actualizamos los menús desplegables con las nuevas opciones del caso
    menu_personas.set(caso['personas'][0])
    menu_objetos.set(caso['objetos'][0])
    menu_lugares.set(caso['lugares'][0])
    opciones_personas['menu'].delete(0, 'end')
    opciones_objetos['menu'].delete(0, 'end')
    opciones_lugares['menu'].delete(0, 'end')

    for persona in caso['personas']:
        opciones_personas['menu'].add_command(label=persona, command=tk._setit(menu_personas, persona))
    for objeto in caso['objetos']:
        opciones_objetos['menu'].add_command(label=objeto, command=tk._setit(menu_objetos, objeto))
    for lugar in caso['lugares']:
        opciones_lugares['menu'].add_command(label=lugar, command=tk._setit(menu_lugares, lugar))
    
    boton_iniciar.pack_forget()
    frame_juego.pack(expand=True)

def reiniciar_juego():
    frame_juego.pack_forget()
    iniciar_juego()

def elegir_opcion():
    eleccion_persona = menu_personas.get()
    eleccion_objeto = menu_objetos.get()
    eleccion_lugar = menu_lugares.get()

    if (eleccion_persona == caso['asesino'] and
        eleccion_objeto == caso['objeto_asesino'] and
        eleccion_lugar == caso['lugar_asesinato']):
        
        resultado.set(f"¡Has resuelto el caso! El culpable es {eleccion_persona}, usó {eleccion_objeto} en {eleccion_lugar}")
        frame_juego.after(3000, reiniciar_juego)
    else:
        pista_persona = caso['pistas'].get(eleccion_persona, "Sin pistas.")
        pista_objeto = caso['pistas'].get(eleccion_objeto, "Sin pistas.")
        pista_lugar = caso['pistas'].get(eleccion_lugar, "Sin pistas.")
        
        resultado.set(f"Pista sobre el familiar: {pista_persona}\n"
                      f"Pista sobre el objeto: {pista_objeto}\n"
                      f"Pista sobre el lugar: {pista_lugar}")

# Interfaz gráfica
root = tk.Tk()
root.title("Asesinato Familiar")
root.geometry("600x450")

# Fondo
bg_image = Image.open("fondo.jpeg")
bg_image = bg_image.resize((600, 450), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Pantalla de inicio
frame_inicio = tk.Frame(root, bg="#FFFFFF", bd=0, relief="flat")
frame_inicio.pack(pady=50)
frame_inicio.place(relx=0.5, rely=0.4, anchor="center")

label_bienvenida = tk.Label(frame_inicio, text="¡Bienvenido al juego del asesinato familiar!", bg="#FFFFFF", font=("Arial", 14))
label_bienvenida.pack(pady=5)

boton_iniciar = tk.Button(frame_inicio, text="Iniciar Juego", command=iniciar_juego, font=("Arial", 12), bg="#4CAF50", fg="white")
boton_iniciar.pack()

# Pantalla del juego
frame_juego = tk.Frame(root, bg="#FFFFFF", bd=0, relief="flat")

texto_descripcion = tk.StringVar()
label_descripcion = tk.Label(frame_juego, textvariable=texto_descripcion, wraplength=500, bg="#FFFFFF", font=("Arial", 12))
label_descripcion.pack(pady=10)

label_persona = tk.Label(frame_juego, text="Selecciona un familiar:", bg="#FFFFFF", font=("Arial", 10))
label_persona.pack(pady=5)

menu_personas = tk.StringVar(root)
menu_personas.set("Elige un familiar")
opciones_personas = tk.OptionMenu(frame_juego, menu_personas, "")
opciones_personas.config(bg="#FFFFFF", font=("Arial", 10), relief="flat")
opciones_personas.pack(pady=5)

label_objeto = tk.Label(frame_juego, text="Selecciona un objeto:", bg="#FFFFFF", font=("Arial", 10))
label_objeto.pack(pady=5)

menu_objetos = tk.StringVar(root)
menu_objetos.set("Elige un objeto")
opciones_objetos = tk.OptionMenu(frame_juego, menu_objetos, "")
opciones_objetos.config(bg="#FFFFFF", font=("Arial", 10), relief="flat")
opciones_objetos.pack(pady=5)

label_lugar = tk.Label(frame_juego, text="Selecciona un lugar:", bg="#FFFFFF", font=("Arial", 10))
label_lugar.pack(pady=5)

menu_lugares = tk.StringVar(root)
menu_lugares.set("Elige un lugar")
opciones_lugares = tk.OptionMenu(frame_juego, menu_lugares, "")
opciones_lugares.config(bg="#FFFFFF", font=("Arial", 10), relief="flat")
opciones_lugares.pack(pady=5)

boton_elegir = tk.Button(frame_juego, text="Elegir", command=elegir_opcion, font=("Arial", 12), bg="#4CAF50", fg="white")
boton_elegir.pack(pady=10)

resultado = tk.StringVar()
label_resultado = tk.Label(frame_juego, textvariable=resultado, wraplength=500, bg="#FFFFFF", font=("Arial", 10))
label_resultado.pack(pady=10)

# Ejecutar el programa
root.mainloop()
