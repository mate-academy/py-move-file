# write your code here
import os


def move_file(command: str) -> None:
    linc = command.split()
    pathway = os.path.split(linc[2])
    linc_file = os.path.join(linc[2])
    if os.path.exists(linc[1]):
        if len(linc) == 3 and linc[0] == "mv" and linc[2].count("/") == 0:
            os.rename(linc[1], linc[2])
        if len(linc) == 3 and linc[0] == "mv" and not linc[2].count("/") == 0:
            if not os.path.isdir(pathway[0]):
                os.makedirs(pathway[0])
            else:
                pass
            with (open(linc[1], "r") as file_in,
                  open(f"{linc_file}", "w") as file_out):
                file_out.write(file_in.read())
                os.remove(linc[1])
