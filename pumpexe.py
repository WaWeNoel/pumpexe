import random
import os

def add_random_files(exe_file, file_size):
    try:
        if file_size[-2:].lower() == 'kb':
            file_size_bytes = int(file_size[:-2]) * 1024
        elif file_size[-2:].lower() == 'mb':
            file_size_bytes = int(file_size[:-2]) * 1024 * 1024
        elif file_size[-2:].lower() == 'gb':
            file_size_bytes = int(file_size[:-2]) * 1024 * 1024 * 1024
        else:
            raise ValueError("Invalid file size format. Please use 'KB', 'MB', or 'GB'.")
        
        with open(exe_file, 'ab') as f:
            while os.path.getsize(exe_file) < file_size_bytes:
                file_content = bytes(random.getrandbits(8) for _ in range(file_size_bytes))
                f.write(file_content)
    except Exception as e:
        print(f"An error occurred while adding files to {exe_file}: {e}")

def print_logo():
    print("""
                                 
    ___ _ _ _____ ___ ___ _ _ ___ 
   | . | | |     | . | -_|_'_| -_|
   |  _|___|_|_|_|  _|___|_,_|___|
   |_|           |_|              
           
  Welcome to EXE file size pumper!
""")

print_logo()

exe_file = input("Enter the name of the .exe file or the path: ")
file_size = input("Enter the size of the files (e.g., '100KB', '5MB', '2GB'): ")

add_random_files(exe_file, file_size)
