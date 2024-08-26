from os import makedirs, rename, remove, chdir, getcwd, path


def move_file(command: str) -> None:
    command_name = command.split()[0]
    source_file_name = command.split()[1]
    destination_name = command.split()[2]
    if command_name == "mv":

        if "/" in destination_name:
            with open(source_file_name) as source:
                source_text = source.read()

            init_dir = getcwd()
            destination_folders = "/".join(destination_name.split("/")[:-1])
            destination_file_name = destination_name.split("/")[-1]
            if not path.exists(destination_folders):
                makedirs(destination_folders)
            chdir(destination_folders)

            with open(destination_file_name, "w") as destination:
                destination.write(source_text)

            chdir(init_dir)
            remove(source_file_name)
        else:
            rename(source_file_name, destination_name)
