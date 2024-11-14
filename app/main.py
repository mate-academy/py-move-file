import os


class Check:
    forbidden_char = {"/", "\\", ":", "*", "?", '"', "<", ">", "|"}

    @classmethod
    def is_good_file(cls, file_name: str) -> bool:
        data = os.path.splitext(file_name)
        if not data[0] or data[1] != ".txt":
            return False
        return True

    @classmethod
    def is_good_name(cls, name: str) -> bool:
        for _chr in name:
            if _chr in cls.forbidden_char:
                return False
        return True

    @classmethod
    def check_path(cls, folders: list[str], file_current: str) -> bool:
        for folder in folders:
            if not folder or not cls.is_good_name(folder):
                return False
        if (
                not cls.is_good_name(file_current)
                or not cls.is_good_file(file_current)
        ):
            return False
        return True


def create_path(folders: list[str]) -> None:
    path = ""
    for folder in folders:
        path = folder if not path else path + "/" + folder
        if not os.path.exists(path):
            os.mkdir(path)


def move_file(command: str) -> None:
    if isinstance(command, str):
        if len(command.split(" ")) == 3:
            operator, path_old, path_new = command.split(" ")
            *folder_old, file_old = path_old.split("/")
            *folder_new, file_new = path_new.split("/")
            if (
                    operator == "mv"
                    and Check.check_path(folder_old, file_old)
                    and Check.check_path(folder_new, file_new)
            ):
                if os.path.exists(path_old) and not os.path.exists(path_new):
                    create_path(folder_new)
                    os.rename(path_old, path_new)
