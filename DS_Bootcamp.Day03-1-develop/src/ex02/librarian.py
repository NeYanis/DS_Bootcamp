#!/usr/bin/env python3
import os
import subprocess
import shutil

def main():
    check_virual()
    install_libs()
    data = show_libs()
    save_file(data)
    make_zip()

def check_virual():
    if 'VIRTUAL_ENV' not in os.environ:
        raise EnvironmentError('venv not running')

def install_libs():

    packages = ['beautifulsoup4', 'pytest']
    try:
        subprocess.check_call(['pip', 'install'] + packages)

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f'library installing error: {e}')

def show_libs():
    result = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)
    print(result.stdout)
    return result.stdout

def save_file(data):
    try:
        with open('requirements.txt', 'w') as file:
            file.write(data)
    except IOError:
        raise IOError('Error write file')

def make_zip():
    folder = 'mabellec'
    if not os.path.exists(folder):
        raise FileNotFoundError(f'{folder} not found')

    try:
        shutil.make_archive('mabellec','zip',base_dir=folder)
    except Exception:
        print('Archivating error')


if __name__ == '__main__':
    main()