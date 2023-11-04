def input_error (func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Enter user name")
            print('___________________')
            func(*args, **kwargs)
        except ValueError:
            print("Give me name and phone please")
            print('___________________')
            func(*args, **kwargs)
        except IndexError:
            print("Try again")
            print('___________________')
            func(*args, **kwargs)
        except TypeError:
            print("Give me name and phone please")
            print('___________________')
            func(*args, **kwargs)
    return inner

phone_dict = {}

@input_error
def start_program():
    return "How can I help you?"

@input_error
def add_phone (name, phone):      #функція для 'add'та 'change'
    new_person = phone_dict[name] = phone
    return new_person

@input_error
def show_number(name):            #функція, що повертає номер телефону
    return phone_dict[name]

@input_error
def show_all(args):
    return phone_dict

operations = {
    "hello": start_program,
    "add": add_phone,
    "change": add_phone,
    "phone": show_number,
    "show": show_all,
}

@input_error
def main():
    while True:
        users_text = input()
        if users_text.lower() == "good bye" or users_text.lower() == "close" or users_text.lower() == "exit" or users_text.lower() == ".":
            print("Good bye!")
            break
        else:
            perser_users_text = users_text.split(' ')
            operation = perser_users_text[0].lower()
            f = operations[operation]
            if len(perser_users_text) == 3:
                print(f(perser_users_text[1], perser_users_text[2]))
                print('___________________')
                continue
            elif len(perser_users_text) == 2:
                print(f(perser_users_text[1]))
                print('___________________')
                continue
            else:
                print(f())
                print('___________________')
                continue


if __name__ == '__main__':
    main()
