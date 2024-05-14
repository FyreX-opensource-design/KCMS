import os

print("Installing")
with open("klipper/.gitignore", "w") as file:
    file.writelines(["out", "*.so", "*.pyc", ".config", ".config.old", "klippy/.version", ".history/", ".DS_Store", "ci_build/", "ci_cache/", "_test_.*", "klippy/plugins/*", "!klippy/plugins/__init__.py", ".vscode", "klipper/config"])
os.system("rm /klipper/config/*")
os.system("rm /klipper/klippy/kinematics/*")
os.system("cd /klipper/klippy/kinematics && wget https://raw.githubusercontent.com/Klipper3d/klipper/master/klippy/kinematics/__init__.py && cd ~")
