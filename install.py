import os
import shlex
import shutil
import subprocess

repos = {
    "https://github.com/vinceliuice/Colloid-icon-theme": ['icons', './install.sh'],
    "https://github.com/vinceliuice/Colloid-gtk-theme": ["theme", "./install.sh --tweaks rimless normal"]
}


def install_dependencies() -> None:
    subprocess.call(shlex.split("./dependencies.sh"))


def install_themes() -> None:
    directory = '/tmp'
    for repo, orders in repos.items():
        command = "git clone " + repo + f" {os.path.join(directory, orders[0])}"
        installer = os.path.join(directory, orders[0], orders[1])
        command = shlex.split(command)
        installer = shlex.split(installer)
        subprocess.call(command, stdout=subprocess.PIPE)
        subprocess.call(installer, stdout=subprocess.PIPE)


def copy_dotfiles() -> None:
    config_dir = os.path.join(os.path.expanduser('~'), '.config')
    configs = [os.path.join(os.getcwd(), x) for x in os.listdir(os.getcwd()) if ".git" not in x] 
    for i in configs: 
        if os.path.isdir(i):
            print("Copiando --> ", i)
            shutil.copytree(i, config_dir)




if __name__ == "__main__":
    copy_dotfiles()
    install_dependencies()
    install_themes()
