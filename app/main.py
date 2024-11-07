import os


class CommandError(Exception):
    def __str__(self) -> str:
        return "Your command is not complete or invalid."


def move_file(command: str) -> None:
    # Validate the command structure
    try:
        copy_command, old_place, new_place = command.split(" ")
    except ValueError:
        raise CommandError("Command is invalid. It should be in the form: 'mv source destination'.")

    # Check if the command is "mv"
    if copy_command != "mv":
        raise CommandError("Invalid command. Only 'mv' is supported.")

    # Check if the source file exists
    if not os.path.isfile(old_place):
        raise FileNotFoundError(f"The source file '{old_place}' does not exist.")

    # Prepare destination path
    destination_path = ""

    if old_place != new_place:
        # If destination ends with '/', it's a directory
        if new_place.endswith('/'):
            # Make sure the destination directory exists
            os.makedirs(new_place, exist_ok=True)
            destination_path = os.path.join(new_place, os.path.basename(old_place))
        else:
            # Create intermediate directories for the destination path if they don't exist
            dir_path = os.path.dirname(new_place)
            if dir_path and not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
            destination_path = new_place

        # Perform the move (copy the file, then remove the original)
        try:
            with open(old_place, 'rb') as src_file:
                with open(destination_path, 'wb') as dest_file:
                    dest_file.write(src_file.read())
            os.remove(old_place)  # Remove the original file
            print(f"File '{old_place}' successfully moved to '{destination_path}'")
        except Exception as e:
            raise Exception(f"An error occurred while moving the file: {e}")



