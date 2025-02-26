import shutil



def backup_commands(commands_file, backup_path):
    """Backs up the commands file to the specified backup path."""
    try:
        shutil.copy2(commands_file, backup_path)
        print(f"Commands backed up to '{backup_path}' successfully.")
        return True
    except FileNotFoundError:
        print(f"Error: Commands file '{commands_file}' not found for backup.")
        return False
    except Exception as e:
        print(f"Error during backup: {e}")
        return False

