import flet as ft
from flet import Container, ImageFit, FilledButton, Control
import subprocess

class MyControl(Control):
    pass

def abrir_otro_script():
    # Reemplaza 'otro_script.py' con el nombre de tu archivo Python
    subprocess.run(['python', 'otro_script.py'])

def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.title = 'Hola, Flet!'
    page.window_resizable = True
    page.window_full_screen = False
    page.window_maximizable = True
    page.window_maximized = True
    page.window_always_on_top = True
    page.padding = 0

    page.add(
        Container(
            image_src='assets/1.16.5.png',
            image_fit=ImageFit.COVER,
            expand=True,
            content=MyControl()
        )
    )

    page.horizontal_alignment = "center"
    page.vertical_alignment = ""
    jugar_button = FilledButton(text="Jugar", width=150, height=50, on_click=abrir_otro_script)
    page.add(jugar_button)

ft.app(main)
