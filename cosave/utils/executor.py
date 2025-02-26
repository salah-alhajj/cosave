
from cosave.utils.loader import load_commands
import re
import subprocess
import yaml


def execute_command(commands_file:str, name, variables, show_output=True):
    """Executes a stored command, replacing variables."""
    command_store = load_commands(commands_file)

    if name not in command_store:
        print(f"Error: Command '{name}' not found.")
        return False

    command_str = command_store[name]
    variable_placeholders = re.findall(r'\[([^\]]+)\]', command_str)

    missing_variables = [var for var in variable_placeholders if var not in variables]
    if missing_variables:
        print(f"Error: Missing required variables: {', '.join(missing_variables)}")
        print(f"Usage: cosave {name} {' '.join([f'--{var} <value>' for var in missing_variables])}")
        return False

    for var, value in variables.items():
        command_str = command_str.replace(f"[{var}]", value)

    print(f"Executing: {command_str}")
    try:
        process = subprocess.Popen(
            command_str,
            shell=True,
            executable='/bin/bash',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        while True:
            stdout_line = process.stdout.readline()
            if stdout_line == '' and process.poll() is not None:
                break
            if stdout_line and show_output: # Conditionally print output
                print(stdout_line.strip())

        return_code = process.poll()

        if return_code != 0:
            stderr = process.stderr.read()
            print(f"Command failed with exit code: {return_code}")
            if stderr:
                print(stderr)
            return False

        return True

    except Exception as e:
        print(f"Error occurred: {e}") # More generic error message
        return False