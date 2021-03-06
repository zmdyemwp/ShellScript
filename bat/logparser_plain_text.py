#!/usr/bin/python

import sys
import os
from os import listdir
from os.path import isfile, join
import zipfile
import os.path
import gzip
import datetime


class bcolors:
    # HEADER = '\033[95m'
    # OKBLUE = '\033[94m'
    # OKGREEN = '\033[92m'
    # WARNING = '\033[93m'
    # FAIL = '\033[91m'
    # ENDC = '\033[0m'
    # BOLD = '\033[1m'
    # UNDERLINE = '\033[4m'
    # DIM = '\033[2m'
    # WHITE = '\033[1m\033[37m'
    HEADER = ''
    OKBLUE = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''
    BOLD = ''
    UNDERLINE = ''
    DIM = ''
    WHITE = ''


def fnTimeStr(tt):
    ms = sec = mm = hh = dd = 0
    ms = tt % 1000
    timestr = "%d ms" % (ms)
    if tt >= 1000:
        sec = (tt / 1000) % 60
        timestr = "%d Sec, %d ms" % (sec, ms)
    if tt >= 60000:
        mm = (tt / 60000) % 60
        timestr = "%d Mins, %d Sec, %d ms" % (mm, sec, ms)
    if tt >= 3600000:
        hh = (tt / 3600000) % 24
        timestr = "%d H, %d Mins, %d Sec, %d ms" % (hh, mm, sec, ms)
    if tt >= 24 * 3600000:
        dd = tt / (24 * 3600000)
        timestr = "%d Day, %d H, %d Mins, %d Sec, %d ms" % (
            dd, hh, mm, sec, ms)
    return timestr


def fnUnZip(source_filename, dest_dir):
    try:
        outfilename = source_filename.rstrip(".gz")
        inF = gzip.open(source_filename, 'rb')
        open(outfilename, 'w').write(inF.read())
        inF.close()
    except :
        print "I/O error: {0}".format( source_filename)


def fnFindAllzipArchAndUzip(flist, path):
    zipArch = ['.gz', '.zip', '.rar', '.7z']
    for target_file in flist:
        for j in zipArch:
            if j in target_file:
                fnUnZip(path + "/" + target_file, path)
                break


def fnOpenAndReadFirstLine(fileName):
    with open(fileName, 'r') as inf:
        line = inf.readline().rstrip()
        line = line.lstrip('Process:')
    return line


def fnGenTimeTable(fname):
    time = fname
    if fname.endswith("txt"):
        for p in errorPattern:
            if p in fname:
                time = fname.lstrip(p + '@')
                time = time.rstrip('.txt')
                dictTimeTable[time] = p
                break


def fnFilterCriticalCheckPoint(fname):
    result = 0
    if fname.endswith("txt"):
        for p in errorPattern:
            if p in fname:
                result = 1
                break
    return result


def fnFilterSystemServerCrash(fname):
    result = 0
    if fname.endswith("txt"):
        if 'system_server_crash' in fname:
            result = 1
    return result


def fnFilterSystemTombstone(fname):
    result = 0
    if fname.endswith("txt"):
        if 'SYSTEM_TOMBSTONE' in fname:
            result = 1
    return result

def fnFilterSystemNativeCrash(fname):
    result = 0
    if fname.endswith("txt"):
        if 'system_app_native_crash' in fname:
            result = 1
    return result

def fnFilterSystemAppWtf(fname):
    result = 0
    if fname.endswith("txt"):
        if 'system_app_wtf' in fname:
            result = 1
    return result


def fnFilterSystemServerWtf(fname):
    result = 0
    if fname.endswith("txt"):
        if 'system_server_wtf' in fname:
            result = 1
    return result


def fnFilterSystemCrash(fname):
    result = 0
    if fname.endswith("txt"):
        if 'system_app_crash' in fname:
            result = 1
    return result


def fnFilterSystemAnr(fname):
    result = 0
    if fname.endswith("txt"):
        if 'system_app_anr' in fname:
            result = 1
    return result

def fnFilterDataAnr(fname):
    result = 0
    if fname.endswith("txt"):
        if 'data_app_anr' in fname:
            result = 1
    return result


def fnAddToDict(inDic, itemName):
    if itemName in inDic:
        inDic[itemName] += 1
    else:
        inDic[itemName] = 1


def fnGetTombstoneName(fpath):
    with open(fpath, 'r') as fp:
        for line in fp:
            if '>>>' and '<<<' in line:
                start = line.find('>>>', 0, len(line))
                end = line.find('<<<', 0, len(line))
                return line[start + 4:end - 1]

def fnGetNativeCrashName(fpath):
    with open(fpath, 'r') as fp:
        for line in fp:
            if "Package:" in line:
                return line.split('Package:')[1].rstrip()

def fnGetDropboxDirList(rootpath):
    dirs = [iti[0] for iti in os.walk(rootpath)]
    return [dropboxdir for dropboxdir in dirs if ("dropbox" in dropboxdir or "Dropbox" in dropboxdir)]


def fnGetMonkeyDirList(rootpath):
    dirs = [iti[0] for iti in os.walk(rootpath)]
    return [dropboxdir for dropboxdir in dirs if ("MKY_LOG".lower() in dropboxdir.lower())]


def fnGetMonkeyResult(fpath):
    with open(fpath, 'r') as fp:
        for line in fp:
            if 'Monkey finished' in line:
                return True
    return False


def fnPrintMonkeyStatus(fpath):
    lastTime = ''
    events = ''
    with open(fpath, 'r') as fp:
        for line in fp:
            if 'calendar_time' in line:
                lastTime = line.lstrip('//')
            if 'Sending event' in line:
                events = line.lstrip('//')
    uptime = lastTime.split('system_uptime:')[1].split(']')[0]
    eventcount = events.split('#')[1]
    print eventcount
    speed = int(uptime) /int(eventcount) 
    print bcolors.WARNING + "    Stop at:"
    print lastTime + events + bcolors.ENDC
    print 'Speed: ' +str(speed)+'ms/events'


def fnParsMonkey(mkfolder):
    filelist = [f for f in listdir(
        mkfolder) if isfile(join(mkfolder, f))]
    for mk in filelist:
        if "mky_event".lower() in mk.lower():
            print bcolors.WHITE + "\n=== Monkey Result of : " + mkfolder + bcolors.ENDC
            if fnGetMonkeyResult(mkfolder + "/" + mk):
                print bcolors.OKBLUE + "    Monkey Finished" + bcolors.ENDC
            else:
                print bcolors.FAIL + "    Monkey Fail" + bcolors.ENDC
                fnPrintMonkeyStatus(mkfolder + "/" + mk)
            # Check if Monkey Finish


def fnParsDropbox(pathDropbox):

    print bcolors.WHITE + "\n=== Summary of : " + pathDropbox + " ===" + bcolors.ENDC
    # Unzip
    filelist = [f for f in listdir(
        pathDropbox) if isfile(join(pathDropbox, f))]
    fnFindAllzipArchAndUzip(filelist, pathDropbox)
    filelist = [f for f in listdir(
        pathDropbox) if isfile(join(pathDropbox, f))]

    CriticalEvents = filter(fnFilterCriticalCheckPoint, filelist)
    for itm in CriticalEvents:
        fnGenTimeTable(itm)

    # Get log time table
    print bcolors.WHITE + "\nHistory:" + bcolors.ENDC
    prvTime = 0
    for time in sorted(dictTimeTable):
        if prvTime > 0:
            print bcolors.DIM + '    ++ ' + fnTimeStr(int(time) - prvTime) + bcolors.ENDC
        # print '  '+dictTimeTable[time], time
        print '  ' + datetime.datetime.fromtimestamp(int(time) / 1000).strftime('%x %X'), dictTimeTable[time]
        prvTime = int(time)

    # Get System server Crashs
    SystemAppServerCrashes = filter(fnFilterSystemServerCrash, filelist)
    if len(SystemAppServerCrashes) > 0:
        print bcolors.WHITE + "\nSystem Server Crash:" + bcolors.ENDC
        for item in SystemAppServerCrashes:
            fnAddToDict(dictServerCrash, fnOpenAndReadFirstLine(
                pathDropbox + "/" + item))
        for item in sorted(dictServerCrash, key=dictServerCrash.get, reverse=True):
            print '  ' + str(dictServerCrash[item]), item
        print "Total: "+str(len(SystemAppServerCrashes))

    # Get System App Tombstone Crashs
    SystemAppTombstones = filter(fnFilterSystemTombstone, filelist)
    if len(SystemAppTombstones) > 0:
        print bcolors.WHITE + "\nSystem app Tombstones:" + bcolors.ENDC
        for item in SystemAppTombstones:
            fnAddToDict(dictTombstone, fnGetTombstoneName(
                pathDropbox + "/" + item))
        for item in sorted(dictTombstone, key=dictTombstone.get, reverse=True):
            print '  ' + str(dictTombstone[item]), item
        print "Total: "+str(len(SystemAppTombstones))

    # Get System App Native Crashs
    SystemAppNativeCrashs = filter(fnFilterSystemNativeCrash, filelist)
    if len(SystemAppNativeCrashs) > 0:
        print bcolors.WHITE + "\nSystem app Native Crashes:" + bcolors.ENDC
        for item in SystemAppNativeCrashs:
            fnAddToDict(dictNativeCrash, fnGetNativeCrashName(
                pathDropbox + "/" + item))
        for item in sorted(dictNativeCrash, key=dictNativeCrash.get, reverse=True):
            print '  ' + str(dictNativeCrash[item]), item
        print "Total: "+str(len(SystemAppNativeCrashs))

    # Get System App Crashes
    SystemAppCrashes = filter(fnFilterSystemCrash, filelist)
    if len(SystemAppCrashes) > 0:
        print bcolors.WHITE + "\nSystem app crashes:" + bcolors.ENDC
        for item in SystemAppCrashes:
            fnAddToDict(dictCrash, fnOpenAndReadFirstLine(
                pathDropbox + "/" + item))

        for item in sorted(dictCrash, key=dictCrash.get, reverse=True):
            print '  ' + str(dictCrash[item]), item
        print "Total: "+str(len(SystemAppCrashes))

    # Get System App WTF
    SystemAppWTF = filter(fnFilterSystemAppWtf, filelist)
    if len(SystemAppWTF) > 0:
        print bcolors.WHITE + "\nSystem app WTF:" + bcolors.ENDC
        for item in SystemAppWTF:
            fnAddToDict(dictSysappWTF, fnOpenAndReadFirstLine(
                pathDropbox + "/" + item))
        for item in sorted(dictSysappWTF, key=dictSysappWTF.get, reverse=True):
            print '  ' + str(dictSysappWTF[item]), item

    # Get System Server WTF
    SystemServerWTF = filter(fnFilterSystemServerWtf, filelist)
    if len(SystemServerWTF) > 0:
        print bcolors.WHITE + "\nSystem Server WTF:" + bcolors.ENDC
        for item in SystemServerWTF:
            fnAddToDict(dictSysServerWTF, fnOpenAndReadFirstLine(
                pathDropbox + "/" + item))
        for item in sorted(dictSysServerWTF, key=dictSysServerWTF.get, reverse=True):
            print '  ' + str(dictSysServerWTF[item]), item
        print "Total: "+str(len(SystemServerWTF))

    # Get System App ANR
    SystemAppAnr = filter(fnFilterSystemAnr, filelist)
    if len(SystemAppAnr) > 0:
        print bcolors.WHITE + "\nSystem app ANR:" + bcolors.ENDC
        for item in SystemAppAnr:
            fnAddToDict(dictANR, fnOpenAndReadFirstLine(
                pathDropbox + "/" + item))

        for item in sorted(dictANR, key=dictANR.get, reverse=True):
            print '  ' + str(dictANR[item]), item
        print bcolors.ENDC
        print "Total: "+str(len(SystemAppAnr))

    # Get Data App ANR
    DataAppAnr = filter(fnFilterDataAnr, filelist)
    if len(DataAppAnr) > 0:
        print bcolors.WHITE + "\nData app ANR:" + bcolors.ENDC
        for item in DataAppAnr:
            fnAddToDict(dictANR, fnOpenAndReadFirstLine(
                pathDropbox + "/" + item))

        for item in sorted(dictANR, key=dictANR.get, reverse=True):
            print '  ' + str(dictANR[item]), item
        print bcolors.ENDC
        print "Total: "+str(len(DataAppAnr))


dictServerCrash = dict()
dictCrash = dict()
dictANR = dict()
dictTombstone = dict()
dictNativeCrash = dict()
dictTimeTable = dict()
dictSysappWTF = dict()
dictSysServerWTF = dict()

currentdir = os.path.dirname(os.path.abspath(__file__))
errorPattern = ['KERNEL_PANIC', 'system_server_watchdog', 'SYSTEM_LAST_KMSG', 'FRAMEWORK_REBOOT','SMPL_RESET','SYSTEM_AUDIT',"SYSTEM_FSCK",
                'SYSTEM_BOOT', 'system_server_crash', 'SYSTEM_RESTART','SYSTEM_RECOVERY_KMSG',"MDLOGGER_RESTART","memory_usage","UNKNOWN_RESET"]
#pathDropbox = str(sys.argv[1])
pathRoot = str(sys.argv[1])

# list all dropbox path
dropboxList = fnGetDropboxDirList(pathRoot)
MonkeyFolderList = fnGetMonkeyDirList(pathRoot)

for banana in MonkeyFolderList:
    fnParsMonkey(banana)
# parse each dropboxList ...
for box in dropboxList:
    dictServerCrash.clear()
    dictCrash.clear()
    dictANR.clear()
    dictTombstone.clear()
    dictNativeCrash.clear()
    dictTimeTable.clear()
    dictSysappWTF.clear()
    dictSysServerWTF.clear()
    fnParsDropbox(box)
