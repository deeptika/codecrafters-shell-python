import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    # Wait for user input
    command = input()
    while command:
        print(f"{command}: command not found")
        command = input()


if __name__ == "__main__":
    main()
