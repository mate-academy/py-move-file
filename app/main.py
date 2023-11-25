import os


def move_file(command: str) -> None:
    try:
        mv, source, destination = command.split()
    except ValueError:
        print("Wrong argument")
    else:
        if mv != "mv":
            return
        if not os.path.exists(source):
            return

        linux = destination.count("/")
        windows = destination.count("\\")
        if linux > windows:
            dir_separator = "/"
        else:
            dir_separator = "\\"

        to_join = ""
        dirs = destination.split(dir_separator)[:-1]
        file_name = destination.split(dir_separator)[-1]

        for directory in range(len(dirs)):
            new_directory = os.path.join(to_join, dirs[directory])
            if not os.path.exists(new_directory):
                os.mkdir(new_directory)
            to_join = new_directory
        result_destination = os.path.join(to_join, file_name)

        with (open(source, "r") as file_in,
              open(result_destination, "w") as file_out):
            text_to_copy = file_in.read()
            file_out.write(text_to_copy)
        os.remove(source)
