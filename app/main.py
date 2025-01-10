import sys

builtin_commands = ["echo", "exit", "type"]

def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")

        command = input()

        match command.split():
            case ["exit", "0"]:
                sys.exit(0)
            case ["echo", *args]:
                print(*args)
            case ["type", *args]:
                if args in builtin_commands:
                    print(f"{args} is a shell builtin")
            case _:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
