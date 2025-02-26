
from cosave.utils import load_commands
import re

def list_commands(commands_file: str):
    """Lists all saved commands."""
    command_store = load_commands(commands_file=commands_file)
    if not command_store:
        print("No commands saved yet.")
        return

    print("\nSaved Commands:")
    print("-" * 60)
    for name, cmd in command_store.items():
        variables = re.findall(r'\[([^\]]+)\]', cmd)
        var_str = f" (Variables: {', '.join(variables)})" if variables else ""
        display_cmd = cmd if len(cmd) < 60 else cmd[:57] + "..."
        print(f"{name}{var_str}\n  → {display_cmd}")
    print("-" * 60)