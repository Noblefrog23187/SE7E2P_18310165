import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

# Nombre del archivo JSON
archivo_db = 'paises.json'

# Cargar paises desde el archivo JSON
def cargar_paises():
    if os.path.exists(archivo_db):
        with open(archivo_db, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return []  # Retorna una lista vacía si el archivo no existe

# Guardar paises en el archivo JSON
def guardar_paises(paises):
    with open(archivo_db, 'w', encoding='utf-8') as file:
        json.dump(paises, file, ensure_ascii=False, indent=4)

# Clase del juego
class AkinatorPaises:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego: Adivina el Pais")
        self.root.geometry("500x450")

        # Cargar y configurar el fondo
        self.fondo_img = Image.open("fondo.jpeg")
        self.fondo_img = self.fondo_img.resize((500, 450), Image.LANCZOS)
        self.fondo = ImageTk.PhotoImage(self.fondo_img)
        self.background_label = tk.Label(root, image=self.fondo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.paises = cargar_paises()
        self.preguntas = [
            ("tiene_acceso_mar", "¿El pais tiene acceso al mar?"),
            ("es_de_america", "¿El pais esta en America?"),
            ("es_union_europea", "¿Es miembro de la Union Europea?"),
            ("es_isla", "¿Es una isla?"),
            ("es_grande", "¿Es un pais grande?")
        ]
        self.posibles = self.paises.copy()
        self.current_question = 0

        # Header simple
        self.header = tk.Label(root, text="¡Adivina el pais que piensas!", font=("Arial", 20, "bold"), bg="lightblue")
        self.header.pack(pady=10, fill=tk.X)

        self.label = tk.Label(root, text="", font=("Arial", 14), bg="lightblue")
        self.label.pack(pady=20)

        self.button_start = tk.Button(root, text="Empezar", command=self.iniciar_juego, width=20, height=2, font=("Arial", 12, "bold"))
        self.button_start.pack(pady=5)

        # Cambiar la función para cerrar la ventana correctamente
        self.button_exit = tk.Button(root, text="Salir", command=root.destroy, width=20, height=2, font=("Arial", 12, "bold"))
        self.button_exit.pack(pady=5)

        self.frame_respuestas = tk.Frame(root, bg="lightblue")
        self.frame_respuestas.pack(pady=20)

    def iniciar_juego(self):
        self.label.config(text="Responde las preguntas para adivinar tu pais.")
        self.posibles = self.paises.copy()
        self.current_question = 0
        self.mostrar_respuestas(False)
        self.preguntar()

    def mostrar_respuestas(self, mostrar):
        for widget in self.frame_respuestas.winfo_children():
            widget.destroy()

        if mostrar:
            self.button_start.pack_forget()
            self.button_exit.pack_forget()

            btn_si = tk.Button(self.frame_respuestas, text="Sí", command=lambda: self.responder("sí"), width=10, height=2, font=("Arial", 12, "bold"))
            btn_si.grid(row=0, column=0, padx=10, pady=10)

            btn_no = tk.Button(self.frame_respuestas, text="No", command=lambda: self.responder("no"), width=10, height=2, font=("Arial", 12, "bold"))
            btn_no.grid(row=0, column=1, padx=10, pady=10)

            btn_salir = tk.Button(self.frame_respuestas, text="Salir", command=self.root.destroy, width=10, height=2, font=("Arial", 12, "bold"))
            btn_salir.grid(row=1, column=0, columnspan=2, pady=10)

    def preguntar(self):
        if self.current_question < len(self.preguntas):
            atributo, pregunta = self.preguntas[self.current_question]
            self.label.config(text=pregunta)
            self.mostrar_respuestas(True)
        else:
            self.fin_juego(None)

    def responder(self, respuesta):
        atributo, pregunta = self.preguntas[self.current_question]

        if respuesta == "no":
            self.posibles = [p for p in self.posibles if not p[atributo]]
        else:
            self.posibles = [p for p in self.posibles if p[atributo]]

        self.current_question += 1
        if len(self.posibles) == 1:
            self.fin_juego(self.posibles[0]["nombre"])
        elif len(self.posibles) == 0:
            self.fin_juego(None)
        else:
            self.preguntar()

    def fin_juego(self, resultado):
        self.mostrar_respuestas(False)
        if resultado:
            confirmacion = messagebox.askyesno("Confirmacion", f"¿Tu pais es {resultado}?", parent=self.root)
            if confirmacion:
                self.label.config(text=f"¡Adivine! Tu pais es {resultado}.")
                self.root.after(2000, self.iniciar_juego)
            else:
                self.label.config(text="No pude adivinar. ¿Quieres agregar un nuevo pais?")
                self.mostrar_botones_agregar()
        else:
            self.label.config(text="No pude adivinar. ¿Quieres agregar un nuevo pais?")
            self.mostrar_botones_agregar()

    def mostrar_botones_agregar(self):
        btn_si = tk.Button(self.frame_respuestas, text="Sí", command=self.agregar_pais, width=10)
        btn_si.pack(side=tk.LEFT, padx=5)

        btn_no = tk.Button(self.frame_respuestas, text="No", command=self.iniciar_juego, width=10)
        btn_no.pack(side=tk.LEFT, padx=5)

    def agregar_pais(self):
        nombre = simpledialog.askstring("Nombre del pais", "¿Cual es el nombre del pais?", parent=self.root)
        if nombre:
            self.ask_preguntas_agregar(nombre)

    def ask_preguntas_agregar(self, nombre):
        tiene_acceso_mar = messagebox.askyesno("Atributo", "¿Tiene acceso al mar?", parent=self.root)
        es_de_america = messagebox.askyesno("Atributo", "¿Esta en America?", parent=self.root)
        es_union_europea = messagebox.askyesno("Atributo", "¿Es miembro de la Union Europea?", parent=self.root)
        es_isla = messagebox.askyesno("Atributo", "¿Es una isla?", parent=self.root)
        es_grande = messagebox.askyesno("Atributo", "¿Es un pais grande?", parent=self.root)

        nuevo_pais = {
            "nombre": nombre,
            "tiene_acceso_mar": tiene_acceso_mar,
            "es_de_america": es_de_america,
            "es_union_europea": es_union_europea,
            "es_isla": es_isla,
            "es_grande": es_grande,
        }
        self.paises.append(nuevo_pais)
        guardar_paises(self.paises)
        self.label.config(text=f"{nombre} ha sido agregado a la base de datos!")
        self.root.after(2000, self.iniciar_juego)

if __name__ == "__main__":
    root = tk.Tk()
    juego = AkinatorPaises(root)
    root.mainloop()
