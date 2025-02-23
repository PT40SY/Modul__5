def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."

    return inner

contacts = {}

@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_contact(args):
    name = args[0]
    return f"{name}: {contacts[name]}"

@input_error
def get_all_contacts(args):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def handler(command, args):
    commands = {
        "add": add_contact,
        "phone": get_contact,
        "all": get_all_contacts
    }
    if command in commands:
        return commands[command](args)
    else:
        return "Unknown command."

def main():
    while True:
        command = input("Enter a command: ").strip()
        if command == "exit":
            break
        args = input("Enter the argument for the command: ").strip().split()
        print(handler(command, args))

if __name__ == "__main__":
    main()
