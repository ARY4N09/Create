import platform
import os
import sys
print('\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m LOADING')
bit = platform.architecture()[0]
print(f'\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m {bit} DETECTED')
try:
    print('\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m CHECKING FOR UPDATES...')
    os.system('git pull')
    print('\033[0;1m[\033[1;32m✓\033[0;1m]\033[0;1m UPDATE CHECK COMPLETE')
except:
    print('\033[0;1m[\033[1;33m!\033[0;1m]\033[0;1m NO GIT REPOSITORY FOUND')
if bit == '64bit':
    import main
elif bit == '32bit':
    print('\033[0;1m[\033[1;31m✗\033[0;1m]\033[0;1m 32BIT NOT SUPPORTED (only 64bit .so file available)')
else:
    print('\033[0;1m[\033[1;31m✗\033[0;1m]\033[0;1m UNSUPPORTED ARCHITECTURE')
