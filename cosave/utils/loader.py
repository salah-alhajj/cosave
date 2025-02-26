
import yaml

def load_commands(commands_file:str):
    """Loads commands from the YAML file."""
    try:
        with open(commands_file, "r") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        return {}