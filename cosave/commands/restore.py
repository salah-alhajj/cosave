from cosave.utils import load_commands, save_commands
def restore_commands(backup_path, commands_file, override):
    """Restores commands from the backup path.
    override: If True, replace current commands. If False, merge."""
    try:
        backup_store = load_commands(backup_path)
        if not backup_store:
            print(f"Error: No commands found in backup file '{backup_path}'.")
            return False

        current_store = {}
        if not override: # Load current commands only if not overriding
            current_store = load_commands(commands_file) or {}

        merged_store = current_store.copy() # Start with current commands if merging
        merged_store.update(backup_store) # Add/override with backup commands

        save_commands(commands_file, merged_store)
        print(f"Commands restored from '{backup_path}' successfully.")
        if override:
            print("Current commands were overridden.")
        else:
            print("Commands merged with current commands.")
        return True

    except FileNotFoundError:
        print(f"Error: Backup file '{backup_path}' not found.")
        return False
    except Exception as e:
        print(f"Error during restore: {e}")
        return False
