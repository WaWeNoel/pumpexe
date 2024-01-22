import random
import os

class TextColors:
    YELLOW_BLACK = '\033[43m\033[30m'
    ORANGE = '\033[33m'
    ENDC = '\033[0m'
    RED = '\033[31m'
    BACKGROUND_GREEN = '\033[42m'
    BACKGROUND_RED = '\033[41m'

def validate_file_path(exe_file):
    if not os.path.exists(exe_file):
        raise FileNotFoundError(f"{TextColors.YELLOW_BLACK}Error: The specified file or path '{exe_file}' does not exist.{TextColors.ENDC}")
    if not exe_file.endswith('.exe'):
        raise ValueError(f"{TextColors.YELLOW_BLACK}Error: The file '{exe_file}' is not an executable (.exe) file.{TextColors.ENDC}")

def validate_file_size(file_size):
    if file_size[-2:].lower() not in ['kb', 'mb', 'gb']:
        raise ValueError(f"{TextColors.RED}Error: Invalid file size format.{TextColors.ORANGE} Please use 'KB', 'MB', or 'GB'.{TextColors.ENDC}")
    if not file_size[:-2].isdigit():
        raise ValueError(f"{TextColors.RED}Error: Invalid file size value. {TextColors.ORANGE}Please provide a valid numerical value.{TextColors.ENDC}")

def add_random_files(exe_file, file_size):
    try:
        validate_file_path(exe_file)
        validate_file_size(file_size)
        
        if file_size[-2:].lower() == 'kb':
            file_size_bytes = int(file_size[:-2]) * 1024
        elif file_size[-2:].lower() == 'mb':
            file_size_bytes = int(file_size[:-2]) * 1024 * 1024
        elif file_size[-2:].lower() == 'gb':
            file_size_bytes = int(file_size[:-2]) * 1024 * 1024 * 1024
        
        with open(exe_file, 'ab') as f:
            while os.path.getsize(exe_file) < file_size_bytes:
                file_content = bytes(random.getrandbits(8) for _ in range(file_size_bytes))
                f.write(file_content)

                print(f"{TextColors.BACKGROUND_GREEN}File pumped successful!{TextColors.ENDC}")
    except Exception as e:
        print(f"{TextColors.BACKGROUND_RED}An error occurred: {e}{TextColors.ENDC}")

def print_logo():
    print("""
    ___ _ _ _____ ___ ___ _ _ ___ 
   | . | | |     | . | -_|_'_| -_|
   |  _|___|_|_|_|  _|___|_,_|___|
   |_|           |_|              
           
  Welcome to EXE file size pumper!
""")

print_logo()

try:
    exe_file = input("Enter the name of the .exe file or the path: ")
    validate_file_path(exe_file)
    
    file_size = input("Enter the size of the files (e.g., '100KB', '5MB', '2GB'): ")
    validate_file_size(file_size)

    add_random_files(exe_file, file_size)
except Exception as e:
    print(e)
