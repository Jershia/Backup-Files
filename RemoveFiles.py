import time
import os
import shutil

def main():
    deletedFolders = 0
    deletedFiles = 0
    path = "C:\Users\HP\Desktop\Whitehat jr\Backup Files\Path"
    days = 30
    seconds = time.time() - (days* 24 * 60 * 60)

    if os.path.exists(path):

        for folder , folders , files in os.walk(path):
            if seconds >= NoOfDays(folder):
                removeFolder(folder)
                deletedFolders += 1
                break
            else:
                for folderz in folders:
                    folder_path = os.path.join(folder , folderz)
                    if seconds >= NoOfDays(folder_path):
                        removeFolder(folder_path)
                        deletedFolders += 1
                for file in files:
                    file_path = os.path.join(folder, file)
                    if seconds >= NoOfDays(file_path):
                        removeFile(file_path)
                        deletedFiles += 1
        else:
            if seconds >= NoOfDays(path):
                removeFile(path)
                deletedFiles += 1
    else:
        print(f'"{path}" is not found')
        deletedFiles += 1
    print(f"Total folders deleted: {deletedFolders}")
    print(f"Total files deleted: {deletedFolders}")

def removeFolder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")

def removeFile(path): 
    if not os.remove(path):
        print(f"{path} is removed successfully")      

def NoOfDays(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == '__main__':
    main() 