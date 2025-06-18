import os
import shutil

try :
    source_path = "C:/Users/Farhan/Downloads"    #source where we inspect files and that is source of files
    file_list = os.listdir(source_path)
    destination_path = input("Enter destination path: ")
except FileNotFoundError:
    print("Enter valid path: ")

for file in file_list:
    src_path = os.path.join(source_path, file)

    #this condition for folders.
    if os.path.isdir(src_path):
        continue

    #this condition for pdfs and docs files.
    elif file.lower().endswith('.pdf') or file.endswith('.docx'):
        dst_path = os.path.join(destination_path, 'Document')
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        shutil.move(src_path, dst_path)
        print(f"{file} moved to 'Documents' folder.")

    #this condition for .jpg or .png files means images
    elif file.lower().endswith('.jpg') or file.endswith('.png'):
        dst_path = os.path.join(destination_path, 'Images')
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        shutil.move(src_path, dst_path)
        print(f"{file} moved to 'Images' folder.")

    #this condition for .mp4 or .mkv files means images
    elif file.lower().endswith('.mp4') or file.endswith('.mkv'):
        dst_path = os.path.join(destination_path, 'Videos')
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        shutil.move(src_path, dst_path)
        print(f"{file} moved to 'Videos' folder.")

    #this condition for .exe or .msi files means images
    elif file.lower().endswith('.exe') or file.endswith('.msi'):
        dst_path = os.path.join(destination_path, 'Setups')
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        shutil.move(src_path, dst_path)
        print(f"{file} moved to 'Setups' folder.")

    else :
        dst_path = os.path.join(destination_path, "Others")
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        shutil.move(src_path, dst_path)
        print(f"{file} moved to 'Others' folder.")

print(f"{source_path} all files moved from this location.")









# destination_folder = os.path.join("C:/Users/Farhan/Downloads", "PDFS")
#
# if not os.path.exists(destination_folder):
#     os.mkdir(destination_folder)
#
# for file in file_list:
#     if file.endswith('.pdf'):
#         src_path = os.path.join("C:/Users/Farhan/Downloads", file)
#         dst_path = os.path.join(destination_folder, file)
#         shutil.move(src_path, dst_path)
#         print(f"{file} moved.")