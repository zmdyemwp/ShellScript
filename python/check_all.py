from subprocess import Popen
from subprocess import check_output
from threading import Timer
import subprocess



# class bcolors:
    # HEADER =    '\033[95m'
    # OKBLUE =    '\033[94m'
    # OKGREEN =   '\033[92m'
    # WARNING =   '\033[93m'
    # FAIL =      '\033[91m'
    # ENDC =      '\033[0m'
    # BOLD =      '\033[1m'
    # UNDERLINE = '\033[4m'
class bcolors:
    HEADER =    ''
    OKBLUE =    ''
    OKGREEN =   ''
    WARNING =   ''
    FAIL =      ''
    ENDC =      ''
    BOLD =      ''
    UNDERLINE = ''


result = check_output(['adb', 'devices'])
list = result.split()
dev_index = [i for i, x in enumerate(list) if x == 'device']
#print(dev_index)
sn_index = [x-1 for x, x in enumerate(dev_index) if x > 0]
#print(sn_index)

for sn in sn_index:
    print(bcolors.HEADER + 'Check All @' + list[sn] + bcolors.ENDC)


    cmd = 'adb -s ' + list[sn] + ' shell \"dumpsys battery | grep level\"'
    # cmd = ['adb', '-s', '' + list[sn], 'shell', '\"dumpsys battery | grep level\"']
    #subprocess.call(cmd.split(), shell=False)
    try:
        result = check_output(cmd)
        print(bcolors.BOLD + bcolors.FAIL + result + bcolors.ENDC + bcolors.ENDC)
    except subprocess.CalledProcessError as e:
        print e.output


    cmd = 'adb -s ' + list[sn] + ' shell \"ps | grep monkey\"'
    # cmd = ['adb', '-s', '' + list[sn], 'shell', '\"ps | grep monkey\"']
    #subprocess.call(cmd.split(), shell=False)
    try:
        result = check_output(cmd)
        print('\t\t' + bcolors.OKBLUE + result + bcolors.ENDC)
    except subprocess.CalledProcessError as e:
        print '\t\tNo Monkey'
        print e.output


    cmd = 'adb -s ' + list[sn] + ' shell uptime'
    #subprocess.call(cmd.split(), shell=False)
    try:
        result = check_output(cmd.split())
        print('\t\t\t\t' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKGREEN + result + bcolors.ENDC + bcolors.ENDC + bcolors.ENDC + '\n\n')
    except subprocess.CalledProcessError as e:
        print e.output