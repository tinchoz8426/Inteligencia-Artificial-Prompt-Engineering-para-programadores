import datetime
import openai
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

class BlogApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Generador de Ideas para Blogs")
        self.geometry("800x600")
        
        # Variable para almacenar el contenido generado
        self.contenido_generado = None
        
        self.crear_widgets()
    
    def crear_widgets(self):
        # Frame principal para organización
        main_frame = ttk.Frame(self)
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Entrada de tema
        ttk.Label(main_frame, text="Tema para el blog:").pack(anchor=tk.W)
        self.entrada_tema = ttk.Entry(main_frame, width=60)
        self.entrada_tema.pack(pady=5, fill=tk.X)
        
        # Botón de generación
        self.btn_generar = ttk.Button(main_frame, 
                                    text="Generar Contenido", 
                                    command=self.generar_contenido)
        self.btn_generar.pack(pady=10)
        
        # Área de texto con scroll
        self.txt_resultado = scrolledtext.ScrolledText(main_frame, 
                                                      wrap=tk.WORD,
                                                      width=80, 
                                                      height=20)
        self.txt_resultado.pack(fill=tk.BOTH, expand=True)
        self.txt_resultado.config(state=tk.DISABLED)
        
        # Botón de guardado
        self.btn_guardar = ttk.Button(main_frame,
                                     text="Guardar en Archivo",
                                     command=self.guardar_contenido,
                                     state=tk.DISABLED)
        self.btn_guardar.pack(pady=10)
        
        # Etiqueta de estado
        self.lbl_estado = ttk.Label(main_frame, text="")
        self.lbl_estado.pack()
    
    def generar_contenido(self):
        tema = self.entrada_tema.get().strip()
        if not tema:
            messagebox.showerror("Error", "Por favor introduce un tema válido")
            return
            
        self.btn_generar.config(state=tk.DISABLED)
        self.lbl_estado.config(text="Generando contenido...")
        
        try:
            client = openai.OpenAI(api_key="API_KEY_OPENAI")
            respuesta = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{
                    "role": "user", 
                    "content": f"Genera 5 ideas de blogs sobre: {tema}. Incluye un resumen de 3 líneas para cada una."
                }],
                temperature=0.7,
                max_tokens=500
            )
            
            contenido = respuesta.choices[0].message.content.strip()
            self.contenido_generado = contenido
            
            # Actualizar el área de texto
            self.txt_resultado.config(state=tk.NORMAL)
            self.txt_resultado.delete(1.0, tk.END)
            self.txt_resultado.insert(tk.END, contenido)
            self.txt_resultado.config(state=tk.DISABLED)
            
            self.btn_guardar.config(state=tk.NORMAL)
            self.lbl_estado.config(text="Contenido generado con éxito!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar contenido: {str(e)}")
            self.lbl_estado.config(text="Error en la generación")
        finally:
            self.btn_generar.config(state=tk.NORMAL)
    
    def guardar_contenido(self):
        if not self.contenido_generado:
            return
            
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"blog_ideas_{timestamp}.txt"
        
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                archivo.write(self.contenido_generado)
            
            self.lbl_estado.config(text=f"Archivo guardado como: {nombre_archivo}")
            messagebox.showinfo("Éxito", f"Contenido guardado en {nombre_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar archivo: {str(e)}")

if __name__ == "__main__":
    app = BlogApp()
    app.mainloop()