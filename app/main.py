from os import replace, path, rename, mkdir
from app.errors import CommandError, MoveFileExistsError


def move_f(command: str, f_base: str, f_move: str) -> bool:
    if command != 'mv':
        raise CommandError(command)
    if path.exists(f_move):
        raise MoveFileExistsError(f_move)
    if path.exists(f_base):
        path_list = path.split(f_move)
        if path_list[0] == '':
            rename(f_base, f_move)
            return True
        dir_list = path_list[0].split('/')
        dir_str = ''
        for directory in dir_list:
            dir_str += f'{directory}/'
            if not path.exists(dir_str):
                mkdir(dir_str)
        replace(f_base, f_move)
        return True
    else:
        print(f"File {f_base} doesn't exist!")
        return False


def move_file(command: str) -> bool:
    com_list = command.split()
    try:
        result = move_f(com_list[0], com_list[1], com_list[2])
    except IndexError:
        print('Not all parameters are specified')
        return False
    except CommandError as e:
        print(e)
        return False
    except MoveFileExistsError as e:
        print(e)
        return False
    if result:
        print('File moved!')
        return True
    return False
