import subprocess


def run_command(*args):
    return subprocess.run(
        [
            '/usr/bin/ntfy',
            *args,
        ],
        capture_output=True,
        text=True
    )
    pass
