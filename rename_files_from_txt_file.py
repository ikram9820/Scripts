import os, re

def rename_files(directory_path, names_file_path):
    with open(names_file_path, 'r') as names_file:
        names = names_file.read().splitlines()

    mp4_files = [file for file in os.listdir(directory_path) if file.endswith('.mp4')]
    mp4_files = sorted(mp4_files,key= file_no)
    
    print(len(names), len(mp4_files))
    if len(names) != len(mp4_files):
        print("Error: Number of names in names.txt doesn't match the number of mp4 files.")
        return   
    
    for i in range(len(mp4_files)):
        old_file_path = os.path.join(directory_path, mp4_files[i])
        new_file_name = str(i+1)+' '+names[i] + '.mp4'
        new_file_path = os.path.join(directory_path, new_file_name)
        print(old_file_path,  new_file_path)
        
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {mp4_files[i]} to {new_file_name}")

def file_no(item):
        numeric_part = re.search(r'\d+', item)
        return int(numeric_part.group()) if numeric_part else float('inf')


dir = '/storage/emulated/0/Documents/Pydroid3/Django 1'
names_file_path = dir+'/names.txt'

rename_files(dir, names_file_path)