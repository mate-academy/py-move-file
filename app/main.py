import os
import shutil


def move_file(command: str) -> None:
    _, file, new_file = command.split()
    if file != new_file:
        if "/" not in new_file:
            try:
                shutil.move(file, new_file)
            except FileNotFoundError:
                print(f"{file} does not exist")
            finally:
                return
        os.makedirs(*os.path.split(new_file)[:-1], exist_ok=True)
        try:
            shutil.move(file, new_file)
        except FileNotFoundError:
            print(f"{file} does not exists")
