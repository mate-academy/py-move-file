import os


def create_directory(dir_names):
    counter = 0
    path_to_file = str(dir_names[counter])
    print(len(dir_names))
    while True:
        try:
            os.mkdir(path_to_file)
        except (FileNotFoundError, FileExistsError):
            counter += 1
            if counter < len(dir_names) - 1:
                path_to_file += '/' + str(dir_names[counter])
                continue
            else:
                break


def delete_current_file(file_name):
    os.remove(file_name)


def move_file(command: str):
    command_split = command.split()
    command_with_slash = command_split[2].split('/')
    result_directory = '/'.join(command_with_slash)

    if command_split[0] == 'mv' and command_split[1] != command_split[2] and len(command_with_slash) < 2:
        try:
            os.rename(command_split[1], command_split[2])
        except FileNotFoundError:
            print(f'File not found {command_split[1]}')
            return

    elif command_split[0] == 'mv' and command_with_slash:
        create_directory(command_with_slash)

        with open(command_split[1], mode='r') as file_in:
            with open(result_directory, mode='w') as file_out:
                for line in file_in:
                    file_out.write(line)

        delete_current_file(command_split[1])


if __name__ == "__main__":
    move_file("mv file.txt some_dir1/some_dir2/some_dir3/new_file.txt")
    # move_file("mv file.txt new_file.txt")
