import os

IGNORE_DIRS = {"env", "__pycache__", ".git", ".venv", "node_modules"}

def list_structure(start_path=".", indent=0):
    for item in os.listdir(start_path):
        if item in IGNORE_DIRS:
            continue
        path = os.path.join(start_path, item)
        print(" " * indent + "|-- " + item)
        if os.path.isdir(path):
            list_structure(path, indent + 4)

if __name__ == "__main__":
    print("Project Directory Structure:\n")
    list_structure(".")