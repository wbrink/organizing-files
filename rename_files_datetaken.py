import os
from PIL import Image

print("Enter directory of files you want renamed")
directory = input() # could place path here instead of using input()
lis = os.listdir(directory)

for file in lis:
    path = os.path.join(directory, file)
    ext = os.path.splitext(file)[1]
    im = Image.open(path)
    date = im._getexif()[36868] # key for date taken getexif returns dictionary
    im.close()
    date = date.split()     # returns a list ["year:month:day", "hours:min:sec"]
    new_date = date[0].split(":")
    new_date = "_".join(new_date)
    new_file = "{0}{1}".format(new_date, ext)
    new_path = os.path.join(directory, new_file)
    if new_file not in os.listdir(directory):
        os.rename(path, new_path)
        print("rename --", new_file)
    else:
        for i in range(1000):
            if new_file in os.listdir(directory):
                print("\nname already exists")
                ext = os.path.splitext(new_file)[1]
                new_file = "{0}({1}){2}".format(new_date, str(i), ext)
                new_path = os.path.join(directory, new_file)
                continue
            else:
                os.rename(path, new_path)
                print("renamed file --", new_file)
                print("")
                break


                #(0)(1)(3)
