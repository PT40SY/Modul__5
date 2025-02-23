from typing import Callable, Dict

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Incorrect command format."
    return inner

def parse_input(user_input: str):
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

@input_error
def add_contact(args, contacts: Dict[str, str]):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_contact(args, contacts: Dict[str, str]):
    name = args[0]
    return contacts[name]

@input_error
def get_all_contacts(args, contacts: Dict[str, str]):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

@input_error
def change_contact(args, contacts: Dict[str, str]):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

def handler(command, args):
    commands = {
        "add": add_contact,
        "phone": get_contact,
        "all": get_all_contacts,
        "change": change_contact
    }
    if command in commands:
        return commands[command](args)
    else:
        return "Unknown command."

def main():
    contacts = {}
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        response = handler(command, args)
        print(response)
        if command in ["exit", "close", "goodbye"]:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

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
