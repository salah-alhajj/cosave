import argparse
import sys
import os
from cosave.commands import add_command, list_commands, delete_command, update_command,backup_commands,restore_commands
from cosave.utils import parse_variables, execute_command, load_commands, save_commands

DEFAULT_COMMANDS_FILE = "commands.yaml"

def main():
    parser = argparse.ArgumentParser(
        description="Command Saver and Executor (cosave)",
        epilog="Examples:\n"
               "  Add a command:    cosave --add dj-init \"django-admin startproject [name] .; python manage.py runserver [port]\"\n"
               "  Update a command: cosave --update dj-init \"new command string\"\n"
               "  Execute command:   cosave dj-init [--output <y/n>] [--var1 value1 ...] \n"
               "  Execute command without vars: cosave testcmd\n"
               "  List commands:    cosave --list\n"
               "  Delete command:   cosave --delete dj-init\n"
               "  Backup commands:  cosave --backup-path backup.yaml\n"
               "  Restore commands (override): cosave --restore-path backup.yaml --override\n"
               "  Restore commands (merge):   cosave --restore-path backup.yaml",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('--commands-file-path', default=DEFAULT_COMMANDS_FILE, help=f"Path to the commands YAML file (default: '{DEFAULT_COMMANDS_FILE}')")


    group = parser.add_mutually_exclusive_group()
    group.add_argument('--add', metavar='NAME', help='Add a new command with the given name')
    group.add_argument('--update', metavar='NAME', help='Update an existing command with the given name')
    group.add_argument('--list', action='store_true', help='List all saved commands')
    group.add_argument('--delete', metavar='NAME', help='Delete a saved command')
    group.add_argument('--backup-path', metavar='PATH', help='Backup commands to the specified file path')
    group.add_argument('--restore-path', metavar='PATH', help='Restore commands from the specified backup file path')
    group.add_argument('--version', action='version', version='cosave 0.9.1') 

    parser.add_argument('--override', action='store_true', help='Override current commands when restoring from backup (default: merge)')
    parser.add_argument('execute_command_name', nargs='?', help='Command to execute') 
    parser.add_argument('--output', type=str, nargs='?', const='y', choices=['y','n'], help='Show command output logs (default: y if flag present, n if flag not present)') # Modified --output


    args, unknown = parser.parse_known_args()
    commands_file_path = args.commands_file_path
    show_output = True
    if args.output == 'n':
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')

    if args.output is not None: # Check if --output is provided
        show_output = args.output.lower() == 'y'
    else:
        show_output = True # default if --output is not given

    if args.backup_path:
        backup_commands(commands_file_path, args.backup_path)

    elif args.restore_path:
        restore_commands(args.restore_path, commands_file_path, args.override)

    elif args.add:
        command_name = args.add
        if not command_name:
            print("Error: Command name required with --add.")
            parser.print_help()
            return 1
        # Command string is everything after '--add <name>' in sys.argv
        try:
            add_index = sys.argv.index('--add')
            command_string_start_index = add_index + 2 # +1 for --add, +1 for name
            if command_string_start_index >= len(sys.argv):
                print("Error: Command string required with --add.")
                parser.print_help()
                return 1
            command_string_parts = sys.argv[command_string_start_index:]
            command_string = " ".join(command_string_parts)
        except ValueError: # Should not happen if argparse works correctly, but for safety
            print("Error parsing command line for --add")
            return 1

        print(f"DEBUG: commands_file_path: {commands_file_path}")
        print(f"DEBUG: command_name: {command_name}")
        print(f"DEBUG: command_string: {command_string}")
        if not add_command(commands_file_path, command_name, command_string): # Check if add_command returns False (error)
            return 1 # Exit with error code

    elif args.update:
        command_name = args.update
        if not command_name:
            print("Error: Command name required with --update.")
            parser.print_help()
            return 1
        # Command string is everything after '--update <name>' in sys.argv
        try:
            update_index = sys.argv.index('--update')
            command_string_start_index = update_index + 2 # +1 for --update, +1 for name
            if command_string_start_index >= len(sys.argv):
                print("Error: Command string required with --update.")
                parser.print_help()
                return 1
            command_string_parts = sys.argv[command_string_start_index:]
            command_string = " ".join(command_string_parts)
        except ValueError: # Should not happen if argparse works correctly, but for safety
            print("Error parsing command line for --update")
            return 1

        update_command(commands_file_path, command_name, command_string, update=True)

    elif args.list:
        list_commands(commands_file_path)

    elif args.delete:
        delete_command(commands_file_path, name=args.delete)

    elif args.execute_command_name: # Execute command if execute_command_name is provided (positional)
        unknown_args_for_execute = unknown[:] # Copy unknown to avoid modifying it
        output_value = args.output # get output value from args

        variables = parse_variables(unknown_args_for_execute)
        if variables is not None:
            execute_command(commands_file_path, args.execute_command_name, variables=variables, show_output=show_output) # Pass show_output
        else:
            return 1

    else: # No command provided, just print help if no other action is taken
        parser.print_help()

    return 0


if __name__ == "__main__":
    sys.exit(main())