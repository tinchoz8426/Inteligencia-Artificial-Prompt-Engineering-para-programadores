from fpdf import FPDF
from datetime import datetime

def crear_factura(nombre_cliente, dni, fecha_factura, monto):
    # Crear una instancia de FPDF
    pdf = FPDF()
    pdf.add_page()
    
    # Configurar la fuente y el tamaño
    pdf.set_font("Arial", size=12)
    
    # Agregar el título
    pdf.cell(200, 10, txt="Factura", ln=True, align="C")
    
    # Agregar los detalles del cliente
    pdf.cell(200, 10, txt=f"Nombre del cliente: {nombre_cliente}", ln=True)
    pdf.cell(200, 10, txt=f"DNI: {dni}", ln=True)
    pdf.cell(200, 10, txt=f"Fecha de la factura: {fecha_factura}", ln=True)
    pdf.cell(200, 10, txt=f"Monto a facturar: ${monto:.2f}", ln=True)
    
    # Guardar el archivo PDF
    nombre_archivo = f"factura_{nombre_cliente.replace(' ', '_')}_{fecha_factura.replace('/', '_')}.pdf"
    pdf.output(nombre_archivo)
    
    print(f"Factura generada y guardada como {nombre_archivo}")

def main():
    while True:
        # Solicitar los datos al usuario
        nombre_cliente = input("Ingrese el nombre completo del cliente (o 'salir' para terminar): ")
        
        if nombre_cliente.lower() == "salir":
            print("Saliendo del programa...")
            break
        
        dni = input("Ingrese el DNI del cliente: ")
        fecha_factura = input("Ingrese la fecha de la factura (dd/mm/aaaa): ")
        monto = float(input("Ingrese el monto a facturar: "))
        
        # Validar la fecha
        try:
            datetime.strptime(fecha_factura, "%d/%m/%Y")
        except ValueError:
            print("Formato de fecha incorrecto. Por favor, use el formato dd/mm/aaaa.")
            continue
        
        # Crear la factura
        crear_factura(nombre_cliente, dni, fecha_factura, monto)

if __name__ == "__main__":
    main()