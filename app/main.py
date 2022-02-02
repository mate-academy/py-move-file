import os


def create_directory(dir_names):
    counter = 0
    path_to_file = str(dir_names[counter])

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


def copy_file(old_name, new_name):
    with open(old_name, mode='r') as file_in:
        with open(new_name, mode='w') as file_out:
            for line in file_in:
                file_out.write(line)


def move_file(command: str):
    command_split = command.split()
    command_with_slash = command_split[2].split('/')
    result_directory = '/'.join(command_with_slash)

    if command_split[0] != 'mv':
        print('This function work only for mv(move) command')
        return None

    if not os.path.exists(command_split[1]):
        print(f'File {command_split[1]} not found')
        return None

    if os.path.exists(command_split[2]):
        print(f'A file with that name {command_split[2]} already exists')
        return None

    if command_split[1] == command_split[2]:
        print(f'File {command_split[1]} have already name {command_split[2]}')
        return None

    if len(command_with_slash) < 2:
        try:
            os.rename(command_split[1], command_split[2])
        except FileNotFoundError:
            print(f'File not found {command_split[1]}')
            return

    elif len(command_with_slash) > 2:
        create_directory(command_with_slash)
        copy_file(command_split[1], result_directory)
        delete_current_file(command_split[1])


if __name__ == "__main__":
    '''Tests for this task'''
    move_file("mv new_file.txt some_dir1/some_dir2/some_dir3/new_file.txt")
    move_file("mv file.txt new_file.txt")
