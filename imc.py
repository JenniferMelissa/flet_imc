import flet as ft

def interpretar_imc(imc):
    if imc < 18.5:
        return "Magreza"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade grau I"
    elif 35 <= imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"



def main(page: ft.Page):
    #evento
    def acao(e):
        calcular = float(peso.value) /(float(altura.value))**2
        resultado.value = f'O IMC é {calcular:.2f}.'

        categoria = interpretar_imc(calcular)
        resultado.value += f'\nClassificação: {categoria}'

        peso.value    = ''  #zera os valores
        altura.value  = ''  #zera os valores

        page.update()

    page.title      = 'IMC'
    page.scroll     = 'adaptive'
    page.theme_mode = ft.ThemeMode.LIGHT

    peso      = ft.TextField(label='Peso')
    altura    = ft.TextField(label='Altura')

    resultado = ft.Text(size=30)

    page.add(
        ft.Row(
            [ft.Text('Calculo do IMC',size=40,width='bold')],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [peso],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [altura],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.ElevatedButton('Calcular IMC', on_click=acao)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [resultado],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.update()

ft.app(main)