# -*- mode: python -*-

block_cipher = None

MAIN_FILE = 'main'
"""
[DONT EDIT THIS]
Name of your main script file
"""

project_path = 'C:\\Users\\tijuk\\Projects\\smile\\'
"""
Path to your Project. This sould contain your MAIN_FILE
"""

env_path = 'C:\\Users\\tijuk\\Envs\\smile\\'
"""
Path to your Python environment.
"""

data_dir_name = 'data'
"""
Relative path to your data dir [ where all the data used in your program is (it should be) stored ] with your,
path relative to your MAIN_FILE
"""

root = '..\\..\\src\\'
"""
Path to your root directory [ where your MAIN_FILE is ]
"""

data_dir = root + '{}\\'.format(data_dir_name)
"""
[ DONT EDIT THIS ]
Path to your data directory [ where all the data used by your program will be stored ]
"""

dest_data_dir = '.\\{}\\'.format(data_dir_name)
"""
[ DONT EDIT THIS ]
Path to your data folder inside the dist directory.
It should be the same relative path of your original data dir to the main.py
Example:
if main.py is on root and data is inside some subfolder inside root. for example: root\\subdir1\\subdir2\\data
dest_data_dir should contain all those subfolders, like such: .\\subdir1\\subdir2\\data
"""

logo_icon = 'C:\\Users\\tijuk\\Projects\\Icons\\LogoIcon.ico'
"""
[ OPTIONAL ]
Path your Icon file
"""

include_data = [
    (data_dir + 'checkpoints\\epoch_75.hdf5',dest_data_dir + 'checkpoints'),
    (data_dir + 'haarcascade_frontalface_default.xml',dest_data_dir),
    (data_dir + 'png\\*',dest_data_dir + 'png')
    ]
"""
Paths to all the data used in your data file.
Usage should be:
( FILE , DIRECTORY )
(data_dir + 'path\\to\\file.extension', dest_data_dir + 'path\\to')
With the exception of face_recognition_model with should be copied to '.'
"""

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
print('Check your paths:')
print('Main File: {}'.format(MAIN_FILE))
print('Source Data Dir: {}'.format(data_dir))
print('Destination Data Dir: {}'.format(dest_data_dir))
print('Path to Env: {}'.format(env_path))
print('Path to Project: {}'.format(project_path))
print('Path to Icon: {}'.format(logo_icon))
print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

############### PYINSTALLER SPEC FILE

a = Analysis([root + MAIN_FILE + '.py'],
             pathex=[project_path + 'build\\pyinstaller',
             env_path + 'Lib\\site-packages\\scipy\\extra-dll',
             env_path + 'Lib\\site-packages\\scipy\\optimize'
             ],
             binaries=[],
             datas=include_data,
             hiddenimports=['scipy._lib.messagestream'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name=MAIN_FILE,
          debug=False,
          strip=False,
          upx=True,
          console=True,
          icon=logo_icon
          )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=MAIN_FILE)
