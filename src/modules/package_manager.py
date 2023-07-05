import os, subprocess

class package_manager:


    def _install(package: str):
        """Installs a package."""

        os.system(f"pip install -q {package}")


    def _uninstall(package: str):
        """Uninstalls a package."""

        os.system(f"pip uninstall -y -q {package}")


    def check():
        """Checks if all the requirements are installed."""

        packages = ["discord.py-self==1.9.2", "discum", "asyncio", "bcrypt", "requests", "discord_rpc.py", "ua_parser"]
        installed_packages = [package.split("==")[0] for package in subprocess.getoutput("pip freeze").splitlines()]

        if "discord.py" in installed_packages:
            package_manager._uninstall("discord.py")

        print("Checking reqs...")
        for package in packages:

            if package not in installed_packages:
                
                match(package):
                    case "discum":
                        package_manager._install("--user --upgrade git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum")
                        
                    case _:
                        package_manager._install(package)

