import os
import shutil
#global vars
global path_to_send
cmd = None
#location vars
plugins = "/klipper/klippy/plugins"
extras = "/klipper/klippy/extras"
kinematics = "/klipper/klippy/kinematics"
config = "klipper/config"
printer_config = "klipper/printer_data/config"

def path_check():
    if os.path.isdir("/klipper/klippy/plugins"):
        path_to_send = plugins
    else:
        path_to_send = extras

def install(install_func):
    y_n = input("install? (y or n)")
    if y_n == "y":
        install_func()

def folder_create(name):
    try:
        os.mkdir(name)
    except:
        print("folder " + name + " already exsists, continuing")

def pull_files(files, path):
    os.system("cd klipper/" + path + " && wget " + files + " && cd ~")

def rename(file, new_name):
    os.rename(file, new_name)

#install functions
def cartesian():
    print("installing cartesian kinematics")
    folder_create("/klipper/config/kinematics")
    pull_files("https://raw.githubusercontent.com/FyreX-opensource-design/KCMS/main/kinematics/cartesian.cfg", "config/kinematics")
    pull_files("https://raw.githubusercontent.com/Klipper3d/klipper/master/klippy/kinematics/cartesian.py","klippy/kinematics")
    if os.path.exists(printer_config + "/printer.cfg") == False:
        shutil.copy("/klipper/config/kinematics/cartesian.cfg", printer_config)
        os.rename(printer_config + "/cartesian.cfg", printer_config + "/printer.cfg")

def cartesian_limited():
    print("installing limited cartesian kinematics")
    folder_create("/klipper/config/kinematics")
    pull_files("kinematics/cartesian_limited.cfg", "config/kinematics")
    if os.path.exists(printer_config + "/printer.cfg") == False:
        shutil.copy("/klipper/config/kinematics/cartesian_limited.cfg", printer_config)
        os.rename(printer_config + "/cartesian_limited.cfg", printer_config + "/printer.cfg")

def coreXY2():
    print("installing coreXY kinematics")
    folder_create("/klipper/config/kinematics")
    pull_files("kinematics/corexy2.cfg")
    shutil.copy("/klipper/config/kinematics/corexy.cfg", printer_config)

def single_Z():
    print("adding single Z to config")
    with open(printer_config + "/printer.cfg", "a") as file:
        file.writelines([])


while cmd != "q":
    cmd = input("input number for itemset or q to exit")
    #kinematics
    if cmd == "111":
        print("cartesian kinematics, used by most bedslingers")
        install(cartesian())
    elif cmd == "112":
        print("limited cartesion, has dffering x and y accels")
        install(cartesian_limited())
    elif cmd == "121":
        print("coreXY kinematics, 2WD, used on higher end machines")
        install(coreXY2())
    elif cmd == "122":
        print("coreXY kinematics AWD, used by printers like the VZbot")
    elif cmd == "123":
        print("limited coreXY, 2WD, different x and y accel version of CoreXY")
    elif cmd == "124":
        print("limited coreXY AWD, differing x and y accels for AWD") 
    elif cmd == "13":
        print("coreXZ, used by more recent bedslingers")
    elif cmd == "14":
        print("hybrid coreXY, used in bed dropping IDEX machines")
    elif cmd == "15":
        print("hybrid coreXZ, idex version of coreXZ")
    elif cmd == "16":
        print("enhanced coreXY, varient of hybrid coreXY")
    elif cmd == "17":
        print("dualing gantry")