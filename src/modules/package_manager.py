import os, subprocess
from src.console.output import output

class package_manager():


    def _install(package: str):
        """Installs a package."""

        os.system(f"pip install -q {package}")


    def _uninstall(package: str):
        """Uninstalls a package."""

        os.system(f"pip uninstall -y -q {package}")


    def check():
        """Checks if all the requirements are installed."""

        packages = ["discord.py-self", "discum", "asyncio", "bcrypt", "requests", "discord_rpc.py", "ua_parser"]
        installed_packages = [package.split("==")[0] for package in subprocess.getoutput("pip freeze").splitlines()]

        if "discord.py" in installed_packages:
            output.error("Warning! You are using stock the discord.py package that is supposed to be used for bots. Vissarion uses the discord.py-self fork of it. Uninstalling discord.py...")
            package_manager._uninstall("discord.py")

        
        for package in packages:

            if package not in installed_packages:
                output.log(f"Installing {package}")
                match(package):
                    case "discum":
                        package_manager._install("--user --upgrade git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum")
                        
                    case _:
                        package_manager._install(package)

        output.log("All packages installed")
