import minecraft_launcher_lib
import os
import subprocess

user_windows = os.environ['USERNAME']
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher"

def install_forge():
    forge_ver = '1.18.2'
    forfe = minecraft_launcher_lib.forge.find_forge_version(forge_ver)
    print(forfe)
    minecraft_launcher_lib.forge.install_forge_version(
        forfe, minecraft_directory)
    print(f'Instalado Forge {forfe}')
    try:
        # Reemplaza 'otro_script.py' con el nombre de tu archivo Python
        subprocess.run(['python', '_internal/Minecraft_start.py'])
    except Exception as e:
        print(f"Error al abrir el script: {e}")

if __name__ == '__main__':
    install_forge()