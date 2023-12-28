import os


def move_file(command: str):
    splitted_command = command.split()
    if len(splitted_command) == 3:

        mv, source_file_name, destination_path_and_name = splitted_command
        print("Destination_path_and_name: ", destination_path_and_name)
        splitted_destination_path = destination_path_and_name.split("/")
        print("splitted_destination_path: ", splitted_destination_path)
        print("joined_splitted_destination_path[:-1]: ", "/".join(splitted_destination_path[:-1]))

        if not destination_path_and_name[-1] == "/":

            if len(splitted_destination_path) == 1 and os.path.exists(source_file_name):
                os.rename(source_file_name, destination_path_and_name)

            elif os.path.exists(a := "/".join(splitted_destination_path[:-1])):
                print(a)
                with (
                    open(source_file_name, "r") as initial_file,
                    open(destination_path_and_name, "w") as copied_file
                ):
                    if os.path.exists(source_file_name):
                        copied_file.write(initial_file.read())
                os.remove(source_file_name)

            else:
                for nr in range(1, len(splitted_destination_path)):
                    os.mkdir("/".join(splitted_destination_path[:nr]))

                with (
                    open(source_file_name, "r") as initial_file,
                    open(destination_path_and_name, "w") as copied_file
                ):
                    if os.path.exists(source_file_name):
                        copied_file.write(initial_file.read())

                os.remove(source_file_name)
        else:
            if os.path.exists(destination_path_and_name[:-1]):
                print(destination_path_and_name)
                with (
                    open(source_file_name, "r") as initial_file,
                    open(destination_path_and_name + source_file_name, "w") as copied_file
                ):
                    if os.path.exists(source_file_name):
                        copied_file.write(initial_file.read())
                os.remove(source_file_name)

            else:
                destination_path_and_name = destination_path_and_name + source_file_name
                print("destination_path_and_name: ", destination_path_and_name)

                for nr in range(1, len(splitted_destination_path)):
                    os.mkdir("/".join(splitted_destination_path[:nr]))

                with (
                    open(source_file_name, "r") as initial_file,
                    open(destination_path_and_name, "w") as copied_file
                ):
                    if os.path.exists(source_file_name):
                        copied_file.write(initial_file.read())

                os.remove(source_file_name)
