"""

DEBUG.PY

Used for code debugging.
Contains the following classes:
[** = not yet implemented]
    Log:
        error(String)           : returns self
        sucess(String)          : returns self
        warn(String)            : returns self
        info(String)            : returns self
        color(Color, String)    : returns self
        split(Color)            : returns self
        **critical(String)      : returns self
    
    IntegrityTest:
        isValidProcess(Process, String)      : returns True/False
        isCameraConnected(Boolean)           : returns True/False
        canLocateFile(String, String)        : returns True/False
        canLocateDir(String, String)         : returns True/False
        **isNone(Object, String)             : returns self
        **performInitialChecks()             : returns self
        hasInternetConnection() [not tested] : returns self

        

Requires installation of colorama: [ pip install colorama ]

Note: 
    -- Not designed to be Thread safe.
    -- Debug doesnt work yet

@Created by Padawan Alexandre

"""
try:
    from colorama import init as _color_init
    from colorama import Fore, Back, Style
    _color_init()

    FONT_COLOR_RED = Fore.RESET+Fore.RED
    FONT_COLOR_GREEN = Fore.RESET+Fore.GREEN
    FONT_COLOR_RESET = Fore.RESET
    FONT_COLOR_YELLOW = Fore.RESET+Fore.YELLOW

    """
    Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    Style: DIM, NORMAL, BRIGHT, RESET_ALL
    """
except:
    FONT_COLOR_RED = ''
    FONT_COLOR_GREEN = ''
    FONT_COLOR_RESET = ''
    FONT_COLOR_YELOW = ''

#Debug Levels
LOG_SHOW_EVERYTHING = 2
LOG_SHOW_IMPORTANT_ONLY = 0
LOG_SHOW_INFO = 1
LOG_SHOW_NOTHING = -1

class Log():
    def __init__(self, debug_level=0):
        """
        
        """
        self._debug_level = debug_level

    def error(self,str):
        """
        Prints an error message on the console. [Error] colored RED
        """
        if self._debug_level == 0:
            self.__print(FONT_COLOR_RED + '[ Erro ]: ' + FONT_COLOR_RESET + str)
        return self

    
    def sucess(self,str):
        """
        Prints a sucess message on the console. [Sucess] colored Green
        """
        if self._debug_level == 0:
            self.__print(FONT_COLOR_GREEN + '[Sucess]: ' + FONT_COLOR_RESET + str)
        return self

    def info(self,str):
        """
        Prints an info message on the console. [Info] colored WHITE
        """
        if self._debug_level == 0:
            self.__print('[ Info ]: ' + str)
        return self

    def warn(self,str):
        """
        Prints an Warning message on the console. [Warn] colored WHITE
        """
        if self._debug_level == 0:
            self.__print(FONT_COLOR_YELLOW + '[ Warn ]: ' + FONT_COLOR_RESET + str)
        return self

    def color(self,col="", str=''):
        """
        Prints a colored message on the console. The entire string colored @param col
        """
        if self._debug_level == 0:
            self.__print(col + str + FONT_COLOR_RESET)
        return self

    def split(self,col=""):
        """
        Draws a line on the console.
        """
        if self._debug_level == 0:
            self.color(col,"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        return self

    def __print(self, str):
        """
        Prints a message on the console.
        """
        print(str)


log = Log()

import ctypes

def PopUp(header, text):
    """
    @Created by Padawan Alexandre

    Generates a PopUp Window on Windows based Systems
    @param: header    - Is the title on the Window
    @param: text    - Is the text content displayed inside the Window
    """
    try:
        ctypes.windll.user32.MessageBoxW(0, text, header, 0)
    except:
        log.warn('PopUp method not found. Ignore this message if you\'re not using Windows')
            
try:
    import httplib
except:
    import http.client as httplib
import pathlib
import os

class IntegrityTest():
    def __init__(self):
        pass

    def canLocateDir(self,path, createIfNotFound=False, hint=''):
        """
            Check if the path in the parameter { path } is a directory.
            @param createIfNotFound: is set to True, and the path does not point to
            a directory, the directory will be created.
        """
        found = self.__locator(path, os.path.isdir(path),hint)
        if not found and createIfNotFound:
            pathlib.Path(path).mkdir(parents=True, exist_ok=True)
        return found
            

    def canLocateFile(self,file, hint=''):
        """
        Check if the path in the parameter { file } is a file.
        """
        return self.__locator(file, os.path.isfile(file),hint)

    def isCameraConected(self, PopUpOn=False):
        """
        As the name suggest, checks if the camera is connected by trying to access the camera
        and by capturing any exceptions. If everything works fine, the camera is release and
        can be accessed normally.
        """
        import cv2
        try:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cap.release()
            log.sucess('Camera found')
            return True
        except:
            if PopUpOn:
                PopUp('Error',"Could not find a Camera. Please make sure it is connected and avaiable")
            log.error('Camera not found.')
            return False

    
    def isValidProcess(self,th, name=''):
        """
        Check if a given Process [th] is a valid(not null) Process variable
        returns if not. Then try to start the Process.
        @param th   : The Process variable
        @param name : The local name for the variable
        """
        if th == None:
            if len(name) > 0:
                log.error(name + ' is not a valid Process')
            return
        if len(name) > 0:
            log.sucess('['+ name + '] is a valid Process')
            pass
        try:
            th.start()
            log.split().sucess(name+ ' sucessfully started.')
        except TypeError as te:
            log.error(name+' failed to start. TypeError').split()
            log.color(FONT_COLOR_RED,'['+name+'] ' + str(te))
        except EOFError as eof:
            log.split().error(name+ 'failed to start. EOFError')
        except OSError as ae:
            log.split().error(name+' failed to start. OSError')

    def hasInternetConnection(self):
        """
        Check there's an internet connection
        """
        if self.__have_internet():
            log.sucess('Internet Connection found')
            return True
        else:
            log.error('No Internet Connection')
            return False

    def performInitialChecks(self):
        """
        Perfoms initial checks.
        [NOT YET IMPLEMENTED]
        """
        self.checkInternetConnection()

    def __have_internet(self):
        """
        Checks if it is possible to connect to [www.google.com]
        """
        conn = httplib.HTTPConnection("www.google.com", timeout=5)
        try:
            conn.request("HEAD", "/")
            conn.close()
            return True
        except:
            conn.close()
            return False
    
    def __locator(self, path, found, hint):
        """
        Prints a message if a path points to something.
        """
        if found:
            log.sucess('[ {} ] found'.format(path))
            return True
        else:
            if not hint == '':
                log.error('[ {} ] not found\nHINT: {}'.format(path,hint))
            else:
                log.error('[ {} ] not found'.format(path))
            return False