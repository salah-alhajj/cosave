
import yaml
import os

def save_commands(commands_file: str,commands):
    print("Saving commands to file...")
    """Saves commands to the YAML file atomically."""
    temp_file = commands_file + ".tmp"
    with open(temp_file, "w") as f:
        yaml.dump(commands, f, indent=2)
    os.replace(temp_file, commands_file)