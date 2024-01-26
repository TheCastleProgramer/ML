import flet as ft
from flet import Container, ImageFit, FilledButton, Control
import os, sys
import subprocess

class MyControl(Control):
    def _get_control_name(self):
        return "MyControl"

def Minecraft_install_and_run(_=None):
    try:
        # Reemplaza 'otro_script.py' con el nombre de tu archivo Python
        subprocess.run(['python', '_internal/Minecraft_install.py'])
    
    except Exception as e:
        print(f"Error al abrir el script: {e}")




def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.title = 'Minecraft Launcher'
    page.padding = 0

    page.add(
        Container(
            image_src='_internal/assets/1.16.5.png',
            image_fit=ImageFit.COVER,
            expand=True
        )
    )

    page.horizontal_alignment = "center"
    page.vertical_alignment = ""
    jugar_button = FilledButton(text="Jugar", width=150, height=50, on_click=Minecraft_install_and_run)
    #cambiar_nombre = FilledButton(text="Cambiar nombre", width=150, height=50, on_click=Minecraft_install_and_run)
    page.add(jugar_button)

ft.app(main)
