import os


def move_file(command: str) -> None:
    cmd, our_file, new_file = command.split()

    if cmd != "mv":
        raise NameError("The command does not exists")

    if our_file != new_file:
        try:
            os.makedirs(os.path.dirname(new_file))
        except FileNotFoundError:
            print("File simply renamed")
        with open(f"{our_file}", "r") as file_in, open(f"{new_file}", "w") as file_out:
            file_out.writelines(file_in.readlines())
        os.remove(our_file)


move_file("mv file.txt file2.txt")