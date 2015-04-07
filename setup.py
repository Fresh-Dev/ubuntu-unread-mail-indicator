#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 1 2015
@author: Kevin Kleinjung
"""
import os
import sys
import subprocess
import shutil
import __init__

def main():
    home = os.curdir                       
    if 'HOME' in os.environ:
        home = os.environ['HOME']
    elif os.name == 'posix':
        home = os.path.expanduser("~/")
    elif os.name == 'nt':
        if 'HOMEPATH' in os.environ and 'HOMEDRIVE' in os.environ:
            home = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
    else:
        home = os.environ['HOMEPATH']
        
    configPath = home+"/.config/unread-mail-indicator/"    
    configFilePath = configPath+"config.ini"
    
    if os.path.isfile(configPath)==False:
        os.makedirs(configPath)
        shutil.copy2('config.ini', configFilePath)
        try:
            retcode = os.system("gedit "+configFilePath)
            
        except OSError, e:
            print >>sys.stderr, "Execution failed:", e
       
        

if __name__ == "__main__":
    main()
    
