import os


def move_file(command: str) -> None:
    linc = command.split()

    if len(linc) == 3 and linc[0] == "mv" and not linc[2].count("/") == 0:
        pathway = linc[2].split("/")[:-1]
        name_file = linc[2].split("/")[-1]
        linc_file = "/".join(pathway)
        if os.path.isdir(linc_file):
            with (open(linc[1], "r") as file_in,
                  open(f"{linc_file}/{name_file}", "w") as file_out):
                file_out.write(file_in.read())
                os.remove(linc[1])
        else:
            os.makedirs(linc_file)
            with (open(linc[1], "r") as file_in,
                  open(f"{linc_file}/{name_file}", "w") as file_out):
                file_out.write(file_in.read())
                os.remove(linc[1])

    if len(linc) == 3 and linc[0] == "mv" and linc[2].count("/") == 0:
        os.rename(linc[1], linc[2])
