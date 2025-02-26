
import yaml
from cosave.utils.loader import load_commands
from cosave.utils.saver import save_commands
def delete_command(commands_file:str,name):
    """Deletes a command from the store."""
    command_store = load_commands(commands_file=commands_file)
    if name not in command_store:
        print(f"Error: Command '{name}' not found.")
        return False

    confirm = input(f"Are you sure you want to delete command '{name}'? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Deletion canceled.")
        return False

    del command_store[name]
    save_commands(commands_file,command_store)
    print(f"Command '{name}' deleted.")
    return True