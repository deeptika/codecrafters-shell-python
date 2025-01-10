import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    # Wait for user input
    command = input()
    while command:
        if command == "exit 0":
            break
        if command.split()[0] == "echo":
            print(f"{command[5:]}")
            continue
        print(f"{command}: command not found")
        main()


if __name__ == "__main__":
    main()
