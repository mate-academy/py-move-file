import os


def move_file(command: str) -> None:
    elements = command.split()

    if len(elements) == 3:
        mv_command, file, new_file = elements
        print(f"mv_command {mv_command}, file {file}, new_file {new_file}")
    else:
        raise ValueError("We must have 3 elements!x")

    if mv_command != "mv":
        raise ValueError("We need only command 'mv'!")
    if "/" not in new_file:
        os.rename(file, new_file)
        return None

    if "." in new_file.split("/")[-1]:
        name_of_new_file = new_file.split("/")[-1]
        directory_to_file = new_file[:new_file.rfind("/")]
    elif "." not in new_file:
        name_of_new_file = file

    os.makedirs(directory_to_file, exist_ok=True)

    name_of_new_file = os.path.join(directory_to_file, name_of_new_file)

    with open(file, "r") as file_in, open(name_of_new_file, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(file)
