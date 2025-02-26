
from cosave.utils import load_commands, save_commands

def add_command(commands_file, name, command_str, update=False):
    """Adds a command to the store, updates if update=True."""
    if not name:
        print("Error: Command name cannot be empty.")
        return False
    if not command_str:
        print("Error: Command string cannot be empty.")
        return False

    command_store = load_commands(commands_file)
    if name in command_store and not update:
        print(f"Error: Command '{name}' already exists. Use --update '{name}' to update it.")
        return False
    elif name in command_store and update:
        command_store[name] = command_str
        save_commands(commands_file, command_store)
        print(f"Command '{name}' updated successfully.")
        return True
    else:
        command_store[name] = command_str
        save_commands(commands_file, command_store)
        print(f"Command '{name}' added successfully.")
        return True