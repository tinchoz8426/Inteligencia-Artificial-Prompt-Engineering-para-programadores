import flet as ft

def main(page: ft.Page):
    # Configuración general de la página
    page.title = "Simulador de Préstamos"
    page.bgcolor = ft.colors.BLUE_GREY_50
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Título de la aplicación
    header = ft.Text("Simulador de Préstamos", size=32, weight="bold", color=ft.colors.BLUE_ACCENT)

    # Campos de entrada con estilo personalizado
    monto_field = ft.TextField(
        label="Monto del préstamo",
        width=300,
        border_color=ft.colors.BLUE,
        border_radius=ft.border_radius.all(8)
    )
    tasa_field = ft.TextField(
        label="Tasa de interés (%) anual",
        width=300,
        border_color=ft.colors.BLUE,
        border_radius=ft.border_radius.all(8)
    )
    plazo_field = ft.TextField(
        label="Plazo (meses)",
        width=300,
        border_color=ft.colors.BLUE,
        border_radius=ft.border_radius.all(8)
    )

    # Botón de calcular sin la propiedad shape para evitar el error
    calcular_btn = ft.ElevatedButton(
        text="Calcular",
        style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN,
            color=ft.colors.WHITE
        )
    )
    
    # Textos para mostrar los resultados
    cuota_text = ft.Text(value="", size=20, color=ft.colors.BLACK87)
    total_text = ft.Text(value="", size=20, color=ft.colors.BLACK87)
    
    # Tabla de amortización con colores personalizados
    amortizacion_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Mes", color=ft.colors.WHITE)),
            ft.DataColumn(ft.Text("Cuota", color=ft.colors.WHITE)),
            ft.DataColumn(ft.Text("Interés", color=ft.colors.WHITE)),
            ft.DataColumn(ft.Text("Amortización", color=ft.colors.WHITE)),
            ft.DataColumn(ft.Text("Saldo", color=ft.colors.WHITE))
        ],
        rows=[],
        heading_row_color=ft.colors.BLUE,
        border=ft.border.all(1, ft.colors.BLUE),
        expand=True
    )
    
    # Contenedor para los campos de entrada
    input_container = ft.Container(
        content=ft.Column(
            [
                monto_field,
                tasa_field,
                plazo_field,
                calcular_btn,
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=ft.border_radius.all(10),
        width=400,
        alignment=ft.alignment.center
    )
    
    # Contenedor para mostrar resultados y la tabla de amortización
    result_container = ft.Container(
        content=ft.Column(
            [
                cuota_text,
                total_text,
                amortizacion_table,
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=ft.border_radius.all(10),
        width=600,
        alignment=ft.alignment.center
    )
    
    def calcular_click(e):
        try:
            monto = float(monto_field.value)
            tasa = float(tasa_field.value)
            plazo = int(plazo_field.value)
        except ValueError:
            def close_dialog(e):
                page.dialog.open = False
                page.update()
            page.dialog = ft.AlertDialog(
                title=ft.Text("Error", size=20, color=ft.colors.RED),
                content=ft.Text("Ingrese valores numéricos válidos", size=16),
                actions=[ft.TextButton("Aceptar", on_click=close_dialog)]
            )
            page.dialog.open = True
            page.update()
            return

        # Convertir tasa anual a tasa mensual en formato decimal
        tasa_mensual = tasa / 100 / 12

        # Cálculo de la cuota mensual usando fórmula de amortización
        if tasa_mensual != 0:
            cuota = monto * (tasa_mensual * (1 + tasa_mensual) ** plazo) / ((1 + tasa_mensual) ** plazo - 1)
        else:
            cuota = monto / plazo

        total_a_pagar = cuota * plazo
        
        cuota_text.value = f"Cuota mensual: ${cuota:,.2f}"
        total_text.value = f"Total a pagar: ${total_a_pagar:,.2f}"

        # Generar la tabla de amortización
        amortizacion_table.rows = []
        balance = monto
        for mes in range(1, plazo + 1):
            interes = balance * tasa_mensual
            amortizacion = cuota - interes
            balance -= amortizacion
            if balance < 0:
                amortizacion += balance
                balance = 0
            amortizacion_table.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(mes))),
                    ft.DataCell(ft.Text(f"${cuota:,.2f}")),
                    ft.DataCell(ft.Text(f"${interes:,.2f}")),
                    ft.DataCell(ft.Text(f"${amortizacion:,.2f}")),
                    ft.DataCell(ft.Text(f"${balance:,.2f}")),
                ])
            )
        page.update()

    calcular_btn.on_click = calcular_click

    # Columna principal que contiene el header, inputs y resultados
    main_column = ft.Column(
        [
            header,
            input_container,
            result_container
        ],
        spacing=30,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(ft.Container(
        content=main_column,
        alignment=ft.alignment.center,
    ))

ft.app(target=main)
