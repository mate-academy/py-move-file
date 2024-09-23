import os


def move_file(command: str) -> None:
    elements = command.split()
    if len(elements) == 3:
        mv_command, file, new_file = elements
    else:
        raise ValueError("We must have 3 elements!x")
    if mv_command != "mv":
        raise ValueError("We need only command 'mv'!")
    current_place = ""
    if "/" not in new_file:
        os.rename(file, new_file)
        return None
    directory_to_file = new_file.split("/")

    if "." in directory_to_file[-1]:
        name_of_new_file = directory_to_file[-1]
        directory_to_file = directory_to_file[:-1]
    elif "." not in new_file:
        name_of_new_file = file

    for ind in range(len(directory_to_file)):
        if ind > 0:
            current_place = os.path.join(current_place, directory_to_file[ind])
        else:
            current_place = directory_to_file[ind]
        try:
            os.mkdir(current_place)
        except FileExistsError:
            pass

    name_of_new_file = os.path.join(current_place, name_of_new_file)

    with open(file, "r") as file_in, open(name_of_new_file, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(file)
