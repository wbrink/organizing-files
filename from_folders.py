import os
import shutil

print("Enter start path")
start_dir = input() # takes path
print("Enter destination path")
destination = input()


walk = os.walk(start_dir)


# renaming files incase they are in destination
for root, dirs, files in walk:
    for file in files:
        path = os.path.join(root,file)
        if file not in os.listdir(destination): 
            shutil.copy2(path, destination)
            print("copied ----", file)
        else:
            for i in range(1000):
                if file in os.listdir(destination):
                    ext = os.path.splitext(file)[1] # returns tuple (root,ext) grabs ext
                    root_file = os.path.splitext(file)[0]
                    print("")
                    print("file:", file, "exists in destination")
                    file = "{0}(({1})){2}".format(root_file, str(i), ext)
                    new_path = os.path.join(root,file) 
                    continue
                else:
                    os.rename(path, new_path)
                    shutil.copy2(new_path,destination)
                    print("copied ----", file)
                    print("\n")
                    break

