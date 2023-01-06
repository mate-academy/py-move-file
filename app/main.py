import os


def move_file(command: str) -> None:
    comm = command.split()
    new_dir = comm[2][:comm[2].rfind("/")]
    initial_file = comm[1]
    new_file = comm[2][comm[2].rfind("/"):]
    if comm[0] == "mv" and comm[1] != comm[2]:
        os.makedirs(new_dir)
        with (
            open(f"{initial_file}", "r") as file_in,
            open(f"{new_dir+new_file}", "w") as file_out
        ):
            file_out.write(file_in.read())
            os.remove(initial_file)
