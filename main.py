import platform

print('\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m LOADING')

# Check architecture
bit = platform.architecture()[0]
print(f'\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m {bit} DETECTED')

# Import the appropriate module based on architecture
if bit == '64bit':
    import main  # Your file is main.cpython-313-aarch64-linux-android.so
    # You can also rename it to main_64 and use:
    # import main_64 as encryption_module
elif bit == '32bit':
    print('\033[0;1m[\033[1;31m✗\033[0;1m]\033[0;1m 32BIT NOT SUPPORTED (only 64bit .so file available)')
    # import main_32  # if you had a 32-bit version
else:
    print('\033[0;1m[\033[1;31m✗\033[0;1m]\033[0;1m UNSUPPORTED ARCHITECTURE')

# Now use the module
# result = encryption_module.your_function()
