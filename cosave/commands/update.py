
from cosave.utils import load_commands, save_commands


def update_command(commands_file, name, command_str, update=True): # update is always true here
    """Updates a command in the store."""
    if not name:
        print("Error: Command name cannot be empty.")
        return False

    if not command_str:
        print("Error: Command string cannot be empty.")
        return False

    command_store = load_commands(commands_file)
    if name in command_store:
        command_store[name] = command_str
        save_commands(commands_file, command_store)
        print(f"Command '{name}' updated successfully.")
        return True
    else:
        print(f"Error: Command '{name}' not found. Use --add '{name}' to add it.")
        return False