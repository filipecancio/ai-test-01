import os

def getDirectory(rel_dir):
    script_dir = os.path.dirname(__file__)
    complete_dir = script_dir + rel_dir
    return complete_dir