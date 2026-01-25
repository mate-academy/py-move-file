import os
from pathlib import Path


def move_file(comand: str) -> None:
    try:
        parameters = comand.split(" ")
        if parameters[0] != "mv" or len(parameters) != 3:
            raise Exception("Command error")
        m_file = parameters[1]
        dest = parameters[2].split("/")
        if "." not in m_file or "." not in dest[-1]:
            raise Exception("File name error")
        if len(dest) == 1:
            if m_file == dest[0]:
                raise Exception("Same file")
            final_d = dest[0]
        else:
            final_d = ""
            for i in range(len(dest) - 1):
                path_check = final_d + dest[i]
                if not (Path.cwd() / path_check).is_dir():
                    os.mkdir(path_check)
                final_d += f"{dest[i]}/"
            final_d += dest[-1]
        with open(m_file, "r") as file_in, open(final_d, "w") as file_out:
            file_out.write(file_in.read())
        os.remove(m_file)
    except Exception as e:
        print(e)
