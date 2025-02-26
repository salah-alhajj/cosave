
def parse_variables(args):
    """Parse variable arguments in the format --name value."""
    variables = {}
    i = 0

    while i < len(args):
        if args[i].startswith('--'):
            var_name = args[i][2:]

            if i + 1 < len(args):
                var_value = args[i + 1]
                variables[var_name] = var_value
                i += 2
            else:
                print(f"Error: Missing value for variable '{var_name}'")
                return None
        else:
            print(f"Error: Invalid argument format: '{args[i]}'")
            print("Variable arguments must be in the format: --variable value")
            return None

    return variables