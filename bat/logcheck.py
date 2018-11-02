#!/usr/bin/python
from __future__ import division
import sys
import os
from os import listdir
from os.path import isfile, join
import os.path

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DIM = '\033[2m'
    WHITE = '\033[1m\033[37m'

class LogElement:
    def __init__(self, priority, tag, count = 1):
        self.priority = priority
        self.tag = tag
        self.count = count

def fnGetLogDirs(currentPath):
    dirList = []
    for ppp in os.walk(currentPath):
        if ('main_log' in ppp[2]) or ('alog' in ppp[2]):
            dirList.append(ppp[0])
    return dirList

def fnCountLogTags(dirPath):
    filelist = [f for f in listdir(dirPath) if isfile(join(dirPath, f))]
    # print 'File List:', filelist
    for logfile in filelist:
        #print logfile
        if ("main_log" in logfile) or ("alog" in logfile) or ("sys_log" in logfile) or ("events_log" in logfile):
        # if ("alog" in logfile) or ("alog_system" in logfile) or ("alog_events" in logfile):
            fnParseOneFile(dirPath + "/" + logfile)
    pass

def fnParseOneFile(fname):
    #print "parse: "+fname
    with open(fname, 'r') as fp:
        for line in fp:
            logLine = line.split()
            if len(logLine) >= 6:
                logToken = LogElement(logLine[4], logLine[5])
                fnAddToLogDict(logDict, logToken)
    pass

def fnAddToLogDict(inDic, logItem):
    name = logItem.tag+logItem.priority
    if name in inDic:
        inDic[name].count += 1
    else:
        inDic[name] = logItem
    pass

logDict = dict()
currentdir = os.path.dirname(os.path.abspath(__file__))
pathRoot = str(sys.argv[1])
logDirPathes = fnGetLogDirs(pathRoot)

# parse each file ...
for d in logDirPathes:
    fnCountLogTags(d)

total = 0
for it in logDict:
    total += logDict[it].count

i = 0
print "\n{0:<40}  {1:<2}  {2:<8}  {3:4}".format("Log Tag"," ","Count", "Count/total")

for item in sorted(logDict, key=lambda item: logDict[item].count, reverse=True):
    i = i + 1
    if logDict[item].count/total < 0.01:
        if i > 20:
            break
    print "{0:<40}  {1:<2}  {2:<8}  {3:.2%}".format(logDict[item].tag,logDict[item].priority,logDict[item].count, logDict[item].count/total)
    pass
