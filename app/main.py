import os


def move_file(command: str) -> None:
    mv_command, source, destination = command.split()

    if mv_command == "mv":
        name_file = destination.split("/")[-1]

        quotes = ""
        for direct in destination.split("/")[:-1]:
            os.mkdir(os.path.join(quotes, direct))
            quotes += direct + "/"

        with open(source, "r") as file_in, \
                open(os.path.join(quotes, name_file), "w") as file_out:
            file_out.write(file_in.read())
        os.remove(source)
