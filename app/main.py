import os


def validate(command: str) -> None:
    if not isinstance(command, str):
        raise TypeError("Command should be str type")
    var_list = command.split()
    if len(var_list) != 3:
        raise ValueError("Invalid command line.")
    if var_list[0] != "mv":
        raise ValueError(f"Invalid command {var_list[0]} != mv")
    if var_list[1] == var_list[2]:
        raise ValueError(f"Invalid new file name, "
                         f"{var_list[1]} should not equal {var_list[2]}")


def move_file(command: str) -> None:
    validate(command)
    cmd, old_file_name, directory_file = command.split()
    if "/" not in directory_file:
        os.rename(old_file_name, directory_file)
    else:
        path, file_name = os.path.split(directory_file)
        os.makedirs(path, exist_ok=True)
        try:
            with (
                open(old_file_name) as old_file,
                open(os.path.join(path, file_name), "w") as new_file
            ):
                new_file.write(old_file.read())
        except FileNotFoundError:
            print(f"{old_file_name} not found")
        finally:
            print("Thank you for choosing our company's services)))")
