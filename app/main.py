import os


def move_file(command):
    command_slit = command.split()
    main_file = command_slit[1]
    copy_way = command_slit[2]
    copy_way_split = copy_way.split('/')
    copy_file = copy_way_split[-1]
    with open(main_file, "r") as file_in:
        text = file_in.read()
        os.remove(main_file)
        for directory in copy_way_split[:-1]:
            os.mkdir(directory)
        with open(copy_file, "w") as file_out:
            file_out.write(text)
