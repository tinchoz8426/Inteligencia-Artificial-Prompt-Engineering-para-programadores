import csv
from faker import Faker

# Crear una instancia de Faker
fake = Faker()

# Datos que se escribirán en el CSV
datos = []

# Generar 10 filas de datos ficticios
for i in range(1, 11):
    datos.append([
        i,  # ID
        fake.first_name(),  # Nombre
        fake.last_name(),  # Apellido
        fake.random_int(min=20, max=60),  # Edad
        fake.job()  # Departamento (usando 'job' como ejemplo)
    ])

# Escribir los datos en un archivo CSV
with open('datos_generados.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Escribir la cabecera
    writer.writerow(['ID', 'Nombre', 'Apellido', 'Edad', 'Departamento'])
    # Escribir las filas de datos
    writer.writerows(datos)

print("Archivo CSV generado exitosamente.")