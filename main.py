import platform
import os
import sys
import importlib.util

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
    try:
        # Add current directory to path
        sys.path.insert(0, os.path.dirname(__file__))
        
        # Import the module
        import main64
        print('\033[0;1m[\033[1;32m✓\033[0;1m]\033[0;1m MODULE LOADED SUCCESSFULLY')
        
        # NOW LET'S TRY TO RUN IT
        
        # Method 1: Check if it has a main function
        if hasattr(main64, 'main'):
            print('\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m RUNNING main()...')
            main64.main()
            
        # Method 2: Check if it has a run function
        elif hasattr(main64, 'run'):
            print('\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m RUNNING run()...')
            main64.run()
            
        # Method 3: List all available functions/attributes
        else:
            print('\033[0;1m[\033[1;33m!\033[0;1m]\033[0;1m NO MAIN FUNCTION FOUND')
            print('\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m AVAILABLE ATTRIBUTES:')
            for attr in dir(main64):
                if not attr.startswith('_'):  # Skip private attributes
                    print(f'    - {attr}')
                    
    except Exception as e:
        print(f'\033[0;1m[\033[1;31m✗\033[0;1m]\033[0;1m ERROR: {e}')
        
elif bit == '32bit':
    print('\033[0;1m[\033[1;31m✗\033[0;1m]\033[0;1m 32BIT NOT SUPPORTED (only 64bit .so file available)')
else:
    print('\033[0;1m[\033[1;31m✗\033[0;1m]\033[0;1m UNSUPPORTED ARCHITECTURE')

# Keep the window open (if on Windows)
if os.name == 'nt':
    input('\nPress Enter to exit...')
