import os
import stat

# Your target path
path = os.path.join(
    "C:/Users/baran/OneDrive/Belgeler/My-Documents/Infotech/training-projects/os-module-project-1/src")

# Changing directory to the target path
os.chdir(path)

# Listing files in the target path
file_list = os.listdir()

# Making directories from its extension and moving files to these directories
for file in file_list:
    file_path_extension_list = os.path.splitext(path + f"/{file}")
    file_path, file_extension = file_path_extension_list[0], file_path_extension_list[1]
    dir_name = file_extension.replace(".", "_")
    if not os.path.exists(path + "/" + dir_name):
        os.mkdir(f"{dir_name}")
        os.rename(f"{file}", f"{dir_name}/{file}")
    elif file.startswith("_"):
        break
    else:
        os.chmod(path + "/" + dir_name + "/" + file, stat.S_IWRITE)
        os.replace(f"{file}", f"{dir_name}/{file}")