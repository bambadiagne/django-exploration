import os
for directory_ in os.listdir():
    if(os.path.isdir(directory_) and directory_ in ["todolist", "users", "todolist_functions_views"]):
        os.system(
            f"autopep8 {directory_} --recursive --in-place --pep8-passes 2000 --verbose")
