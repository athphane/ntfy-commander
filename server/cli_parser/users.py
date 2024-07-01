from cli_parser.executor import run_command
import re


def get_users():
    # Define the regex pattern
    pattern = r"user (\w+|[*]) \(role: (\w+), tier: (\w+)\)"

    result = run_command('user', 'list')

    # Find all matches
    matches = re.findall(pattern, result.stderr)
    return matches
