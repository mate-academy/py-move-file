import os


def move_file(command: str):
    command_split = command.split()
    main_file = command_split[1]
    copy_way = command_split[2]
    copy_way_split = copy_way.split("/")
    copy_file = copy_way_split[-1]
    with open(main_file, "r") as file_in:
        text = file_in.read()
        os.remove(main_file)
        for directory in copy_way_split[0:len(copy_way_split) - 2]:
            os.mkdir(directory)
        with open(copy_file, "w") as file_out:
            file_out.write(text)
