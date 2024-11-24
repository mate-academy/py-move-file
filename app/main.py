import os


def move_file(command: str) -> None:
    command_split = command.split()
    source_file_name = command_split[1]
    directory = "/".join(command_split[2].split("/")[:-1])
    destination_file_name = command_split[2].split("/")[-1]

    print(source_file_name)
    print(directory)
    print(destination_file_name)

    if directory:
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(source_file_name, "r") as file, open(directory + "/" + destination_file_name, "w") as d_file:
            d_file.write(file.read())
        os.remove(source_file_name)

    else:
        os.rename(source_file_name, destination_file_name)
