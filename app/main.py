import os


# mv file.txt some_dir/new_file.txt


def move_file(command: str) -> None:
    command = command.split()

    if command[0] != "mv":
        raise NameError("The command does not exists")

    our_file = command[1]
    list_to_join = command[2].split("/")
    new_dir = "/".join(list_to_join[:-1])
    os.makedirs(new_dir)
    path_to_file = "/".join(list_to_join)

    with open(our_file, "r") as source_file, \
            open(path_to_file, "a") as result_file:
        result_file.writelines(source_file.readlines())
    os.remove(our_file)
