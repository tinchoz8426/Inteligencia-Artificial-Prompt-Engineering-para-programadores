import tkinter as tk
from tkinter import messagebox

# Función para calcular el IMC y determinar la categoría con recomendaciones
def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        if altura <= 0 or peso <= 0:
            messagebox.showerror("Error", "Peso y altura deben ser mayores que 0.")
            return
        
        imc = peso / (altura ** 2)
        imc = round(imc, 2)
        
        # Determinar la categoría y las recomendaciones
        if imc < 18.5:
            categoria = "Bajo peso"
            recomendaciones = (
                "Recomendaciones:\n- Consulta con un nutricionista.\n"
                "- Aumenta la ingesta calórica de manera saludable.\n"
                "- Incluye proteínas y carbohidratos complejos."
            )
        elif 18.5 <= imc < 24.9:
            categoria = "Peso normal"
            recomendaciones = (
                "Recomendaciones:\n- Mantén una dieta equilibrada.\n"
                "- Realiza ejercicio regularmente.\n"
                "- Continúa con hábitos saludables."
            )
        elif 25 <= imc < 29.9:
            categoria = "Sobrepeso"
            recomendaciones = (
                "Recomendaciones:\n- Considera reducir el consumo de calorías.\n"
                "- Aumenta la actividad física.\n"
                "- Consulta con un profesional de la salud."
            )
        else:
            categoria = "Obesidad"
            recomendaciones = (
                "Recomendaciones:\n- Consulta con un médico o nutricionista.\n"
                "- Adopta una dieta baja en grasas y azúcares.\n"
                "- Realiza ejercicio bajo supervisión médica."
            )
        
        label_resultado.config(text=f"IMC: {imc}\nCategoría: {categoria}")
        label_recomendaciones.config(text=recomendaciones)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de IMC")
ventana.geometry("500x500")  # Tamaño más grande de la ventana
ventana.resizable(False, False)

# Crear un Frame para centrar los widgets
frame_central = tk.Frame(ventana)
frame_central.place(relx=0.5, rely=0.5, anchor="center")

# Título
label_titulo = tk.Label(frame_central, text="Calculadora de IMC", font=("Arial", 18, "bold"))
label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Etiquetas y entradas para peso y altura
label_peso = tk.Label(frame_central, text="Peso (kg):", font=("Arial", 12))
label_peso.grid(row=1, column=0, pady=5)

entry_peso = tk.Entry(frame_central, font=("Arial", 12), justify="center")
entry_peso.grid(row=1, column=1, pady=5)

label_altura = tk.Label(frame_central, text="Altura (m):", font=("Arial", 12))
label_altura.grid(row=2, column=0, pady=5)

entry_altura = tk.Entry(frame_central, font=("Arial", 12), justify="center")
entry_altura.grid(row=2, column=1, pady=5)

# Botón para calcular
boton_calcular = tk.Button(frame_central, text="Calcular IMC", font=("Arial", 12), command=calcular_imc)
boton_calcular.grid(row=3, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(frame_central, text="IMC: \nCategoría: ", font=("Arial", 14), justify="center")
label_resultado.grid(row=4, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar recomendaciones
label_recomendaciones = tk.Label(frame_central, text="", font=("Arial", 10), justify="center", wraplength=400)
label_recomendaciones.grid(row=5, column=0, columnspan=2, pady=10)

# Nombre del creador
label_creador = tk.Label(ventana, text="Creado por: Pedro el Escamoso", font=("Arial", 10, "italic"))
label_creador.place(relx=0.5, rely=0.95, anchor="center")

ventana.mainloop()
