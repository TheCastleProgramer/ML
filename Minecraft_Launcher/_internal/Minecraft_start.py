import minecraft_launcher_lib
import os
import subprocess


user_windows = os.environ['USERNAME']
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher"






def ejecuta_mine(mine_user):
    forts = minecraft_launcher_lib.utils.get_installed_versions(
        minecraft_directory)
    for fort in forts:
        print(fort['id'])
    version = '1.18.2-forge-40.2.17'
    options = {
        'username': mine_user,
        'uuid': '',
        'token': '',

        "jvmArguments": ["-Xmx2G", "-Xms2G"],  # The jvmArguments
        "launcherVersion": "0.0.1",
    }

    # Ejecutar Minecraft
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
        version, minecraft_directory, options)
    subprocess.run(minecraft_command)


def menu():
    mine_user = input('Nombre: ')
    print(f'Bienvenido al Luancher Personal {mine_user}\n\n')
    ejecuta_mine(mine_user)


if __name__ == '__main__':
    menu()