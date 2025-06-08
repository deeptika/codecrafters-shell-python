import os
import shlex
import subprocess as sp
import sys

BUILTINS = ["echo", "exit", "type", "pwd", "cd"]
PATH = os.environ.get('PATH')
HOME = os.environ.get('HOME')


def find_path(cmd):
    for path in PATH.split(":"):
        full_path = os.path.join(path, cmd)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path
    return None


def process_command(input_txt):
    return shlex.split(input_txt)


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        try:
            command_line = input()
        except EOFError:
            break
        if not command_line.strip():
            continue
        tokens = shlex.split(command_line)
        command = tokens[0]
        args = tokens[1:]

        if command == 'exit':
            code = int(args[0]) if args else 0
            sys.exit(code)

        if command == 'echo':
            print(" ".join(args))

        elif command == 'pwd':
            print(os.getcwd())

        elif command == 'cd':
            try:
                if not args or args[0] == '~':
                    os.chdir(HOME)
                else:
                    os.chdir(args[0])
            except FileNotFoundError:
                print(f"{command}: {args[0] if args else ''}: No such file or directory")

        elif command == 'type':
            cmd = args[0]
            if cmd in BUILTINS:
                print(f"{cmd} is a shell builtin")
            elif find_path(cmd):
                print(f"{cmd} is {find_path(cmd)}")
            else:
                print(f"{cmd}: not found")

        else:
            cmd_path = find_path(command)
            if cmd_path:
                try:
                    sp.run([command] + args)
                except Exception as e:
                    print(f"Error running command: {e}")
            else:
                print(f"{command}: command not found")



if __name__ == "__main__":
    main()
