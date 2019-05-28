import os

def create_dirs_if_not_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)