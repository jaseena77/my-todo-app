#glob - returns every list of all filepaths in a dir .
#csv - to work with csv files
#shutil - to copy file paths,create zip files extract files,etc
#webbrowser - webbrowser .open()-search anything on google through python
FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    """read  a text files and return list
    of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
