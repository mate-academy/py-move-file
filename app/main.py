import os


def move_file(command: str) -> None:
    mv, file_name_1, file_name_2 = command.split()
    if mv == "mv" and file_name_1 != file_name_2:
        if '/' in file_name_2:
            path = file_name_2[:file_name_2.rfind('/')]
            os.makedirs(path)
        with open(file_name_1, "r") as file_out, \
                open(file_name_2, "w") as file_in:
            file_in.write(file_out.read())
        os.remove(file_name_1)
