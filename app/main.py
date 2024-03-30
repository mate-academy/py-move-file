import os
import shutil


class Errors(BaseException):
    pass


class WrongCommandEr(Errors):
    pass


class WrongTypeEr(Errors):
    pass


class WrongCommandStructureEr(Errors):
    pass


class IsNotFileEr(Errors):
    pass


class NoSuchFile(Errors):
    pass


def is_smth_wrong_command_right(command: str) -> None:
    if not isinstance(command, str):
        raise WrongTypeEr(f"string {command} is not string")
    if command.strip()[:3] != "mv ":
        raise WrongCommandEr(f"Command {command} is not mv. "
                             f"I do not know what to do. Bay!")
    if command.strip().count(" ") < 2:
        raise WrongCommandStructureEr(f"This command:{command} "
                                      f"has strange structure. "
                                      f"I do not know how to work with it."
                                      f" Bay!")
    comanda, current_file, new_file_path, *arg = command.strip().split()
    if current_file[-4:] != ".txt":
        raise IsNotFileEr(f"{comanda + ' ' + current_file} is not file txt."
                          f" I work only with txt.")
    if (new_file_path[-4:] != ".txt"
            and os.path.split(new_file_path)[-1] != ""):
        raise IsNotFileEr(f"I work only with txt. "
                          f"I can not create {new_file_path}")
    if not os.path.isfile(current_file):
        raise IsNotFileEr(f"No such file: {current_file}")


def move_file(command: str) -> None:
    try:
        is_smth_wrong_command_right(command)
    except Errors as e:
        raise e

    _, current_file, new_file_path, *arg = command.strip().split()
    if os.path.split(new_file_path)[0] != "":
        os.makedirs(os.path.split(new_file_path)[0], exist_ok=True)
    if os.path.split(new_file_path)[-1] == "":
        new_file_path = os.path.join(new_file_path, current_file)

    shutil.move(current_file, new_file_path)
