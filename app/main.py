import os


def move_file(comand: str) -> None:
    try:
        parameters = comand.split()
        if parameters[0] != "mv" or len(parameters) != 3:
            raise Exception("Command error")
        com, m_file, dest = parameters
        if "/" not in dest:
            if dest == m_file:
                raise Exception("Same file")
            final_d = dest
        else:
            if dest[-1] == "/":
                dest += m_file
            folders = dest.split("/")
            final_d = ""
            for i in range(len(folders) - 1):
                path_check = final_d + folders[i]
                try:
                    os.mkdir(path_check)
                except Exception:
                    pass
                final_d += f"{folders[i]}/"
            final_d += folders[-1]
            print(final_d)

        with open(m_file, "r") as file_in, open(final_d, "w") as file_out:
            file_out.write(file_in.read())
        os.remove(m_file)
    except Exception as e:
        print(e)
