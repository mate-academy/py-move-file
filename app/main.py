import shutil
import os


def move_file(command: str) -> None:
    mv_token = command.split()
    if len(mv_token) == 3 and mv_token[0] == "mv":
        path_f = mv_token[2]
        if path_f.endswith(("/", "\\")):
            path_f = os.path.join(path_f, mv_token[1])
            path_f = os.path.normpath(path_f)
        else:
            path_f = os.path.normpath(mv_token[2])
        path = path_f.split(os.sep)
        path_start = ""
        for part in path[:-1]:
            try:
                os.mkdir(os.path.join(path_start, part))
            except FileExistsError:
                pass
            finally:
                path_start = os.path.join(path_start, part)
        path_start = os.path.join(path_start, path[-1])
        shutil.copy2(mv_token[1], path_start)
        os.remove(mv_token[1])
