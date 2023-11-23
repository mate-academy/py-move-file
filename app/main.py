import os


def move_file(command: str) -> None:
    list_files = command.split()
    if len(list_files) == 3 and list_files[0] == "mv":
        depth = list_files[2].split("/")
        path = ""
        for n in range(len(depth) - 1):
            path += f"{depth[n]}{os.sep}"
            try:
                os.mkdir(f".{os.sep}{path}")
            except:
                pass
        with (open(list_files[1], "r") as file_in,
              open(list_files[2], "w") as file_out):
            lines = file_in.readlines()
            for line in lines:
                file_out.write(line)
        os.remove(list_files[1])
