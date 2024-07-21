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

def include_cfg(cfg_name):
    with open("klipper/printer_data/config/printer.cfg", "a") as file:
        file.write("\n[include " + cfg_name + ".cfg]")  

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
    pull_files("https://raw.githubusercontent.com/FyreX-opensource-design/KCMS/main/kinematics/cartesian_limited.cfg", "config/kinematics")
    pull_files("https://raw.githubusercontent.com/DangerKlippers/danger-klipper/master/klippy/kinematics/limited_cartesian.py", "klippy/kinematics")
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
    include_cfg("single_z")
    folder_create(config + "kinematics/z_axis")
    pull_files("", "config/kinematiccs/z_axis")
    shutil.copy(config + "/kinematics/z_axis/single_z", printer_config)

#Steppers

def create_TMC_file():
    if os.path.exists(printer_config + "tmc.cfg") == False:
        with open("tmc.cfg", "w") as file:
            file.write("# stepper driver config")

def TMC(stepper, driver):
    if stepper and driver != None:
        create_TMC_file()
        with open(printer_config + "/tmc.cfg", "a") as file:
            file.writelines(["[TMC" + driver + " " + stepper + "]", "cs_pin: #required", "run_current:", "hold_current:", "home_current: #Danger Klipper only", "interpolate: True", "coolstep_threshold: #Danger Klipper only" ,"high_velocity_threshold: #Danger Klipper only","stealthchop_threshold: 120"])

def TMC_autotune():
    if os.path.exists("~/klipper_tmc_autotune") == False:
        os.system("wget -O - https://raw.githubusercontent.com/andrewmcgr/klipper_tmc_autotune/main/install.sh | bash")
        with open(printer_config + "moonraker.conf", "a") as file:
            file.writelines(["[update_manager klipper_tmc_autotune]","type: git_repo","channel: dev","path: ~/klipper_tmc_autotune","origin: https://github.com/andrewmcgr/klipper_tmc_autotune.git","managed_services: klipper","primary_branch: main","install_script: install.sh]"])
    else:
        print("TMC autotune already installed")

def TMC_autotune_def(stepper, motor):
    if stepper and motor != None:
        if os.path.exists("~/klipper_tmc_autotune") == True:
            create_TMC_file()
            with open(printer_config + "/tmc.cfg", "a") as file:
                file.writelines(["[autotune_tmc "+ stepper + "]","motor:" + motor])


def chopper_resonance_tuner():
    if os.path.exists("~/chopper-resonance-tuner") == False:
        os.system("cd ~ && git clone https://github.com/MRX8024/chopper-resonance-tuner && bash ~/chopper-resonance-tuner/install.sh")
        with open(printer_config + "moonraker.conf", "a") as file:
            file.writelines(["[update_manager chopper_resonace_tuner]","type: git_repo","channel: dev","path: ~/chopper-resonace-tuner","origin: https://github.com/MRX8024/chopper-resonance-tuner.git","managed_services: klipper","primary_branch: main","install_script: install.sh]"])
    else:
        print("Chopper resonace tuner already installed")

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
    elif cmd == "21":
        print("single Z motor")
    elif cmd == "411":
        print("TMC cfg")
        install(TMC(None, None))
        stepper = input("input stepper name")
        driver = input("input driver name")
        TMC(stepper, driver)
    elif cmd == "412":
        print("TMC autotune motor def")
        install(TMC_autotune_def(None, None))
        stepper = input("input stepper name")
        motor = input("input motor model")
        TMC_autotune_def(stepper, motor)
    elif cmd == "51":
        print("TMC autotune")
        install(TMC_autotune())
    elif cmd == "52":
        print("chopper resonace tuner")
        install(chopper_resonance_tuner())
