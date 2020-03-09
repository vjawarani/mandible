import os

def remove(path, ext):
    removed=0
    files = os.listdir("path")
    for f in files:
        removed+=1
        if f.endswith("ext"):
            os.remove(f)

    print("Removed " + removed + "files!")