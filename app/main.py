import os


def move_file(command: str):
    command = command.split()
    main_file = command[1]
    move_main_file = command[2]

    with open(main_file, 'r') as file:
        data = file.read()

    if '/' in move_main_file:
        new_path_list = move_main_file.split('/')
        index = 0

        for f in range(len(new_path_list) - 1):

            path_to_file = \
                move_main_file[:move_main_file.index(
                    '/', index, len(move_main_file)
                )]

            if not os.path.exists(path_to_file):
                os.mkdir(path_to_file)

            index += len(new_path_list[f]) + 1
        os.remove(main_file)

        with open(move_main_file, 'w') as new_file:
            new_file.write(data)

    else:
        with open(move_main_file, 'w') as new_file:
            new_file.write(data)
            os.remove(main_file)


if __name__ == "__main__":
    move_file("mv file1.txt first_dir/second_dir/third_dir/fourth/file1.txt")
