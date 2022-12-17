import os

def purgeFolder(pt:str) -> None:
    for root, dirs, files in os.walk(pt, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))