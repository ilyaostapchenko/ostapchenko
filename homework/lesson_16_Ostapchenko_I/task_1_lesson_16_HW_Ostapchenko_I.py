"""Returns a compact view"""
import pprint

def print_result(*args) -> None:
    """Returns result"""
    for element in args:
        pprint.pprint(element, width=1)
        input("Press to continue...")


def add_basketball_player(first_name: str, last_name: str, middle_name: str, growth: int) -> dict:
    """Returns a new basketball player"""
    global BASKETBALLERS
    basketballer = {
        'First name': first_name,
        'Middle name': middle_name,
        'Surname': last_name,
        'Basketballer\'s height': growth,
    }
    BASKETBALLERS.append(basketballer)
    return basketballer


def del_basketballer(surname: str) -> dict:
    """Removes a basketball player by surname"""
    del_basketball_player = {}
    for index, basketballer in enumerate(BASKETBALLERS):
        if basketballer["Surname"] == surname:
            del_basketball_player.update(basketballer)
            del(BASKETBALLERS[index])
            return del_basketball_player


def find_basketballer(surname: str) -> dict:
    """Returns search result"""
    for basketballer in BASKETBALLERS:
        if basketballer['Surname'] == surname:
            return basketballer
        return f"Basketballer {surname} doesn't exist."


def update_basketballer(surname: str) -> dict:
    """Returns updated information about the basketball player"""
    for basketballer in BASKETBALLERS:
        if basketballer['Surname'] == surname:
            first_name = basketballer["First name"]
            middle_name = basketballer["Middle name"]
            surname = basketballer["Surname"]
            new_first_name = input(f"Enter first name ({first_name} - default): ")
            new_middle_name = input(f"Enter middle name ({middle_name} - default): ")
            new_last_name = input(f"Enter a new surname ({surname} - default): ")
            if new_first_name:
                basketballer["First name"] = new_first_name
            if new_middle_name:
                basketballer["Middle name"] = new_middle_name
            if new_last_name:
                basketballer["Surname"] = new_last_name
                return basketballer


if __name__ == '__main__':
    ADD_BASKETBALL_PLAYER = 'add'
    REMOVE_BASKETBALL_PLAYER = 'del'
    FIND_BASKETBALL_PLAYER = 'find'
    UPDATE_BASKETBALL_PLAYER = 'update'
    EXIT = "q"
    BASKETBALLERS = []
    while True:
        print(f"""Choices:
    ADD BASKETBALL PLAYER -> {ADD_BASKETBALL_PLAYER}
    REMOVE BASKETBALL PLAYER -> {REMOVE_BASKETBALL_PLAYER}
    FIND BASKETBALL PLAYER -> {FIND_BASKETBALL_PLAYER}
    UPDATE BASKETBALL PLAYER -> {UPDATE_BASKETBALL_PLAYER}
    EXIT -> {EXIT}
______________________________________
    """)

        choice = input("Enter your choice: ")
        if choice == EXIT:
            print("THE PROGRAM IS OVER.")
            break

        elif choice == ADD_BASKETBALL_PLAYER:
            basketballer = add_basketball_player(
                first_name=input("First name: "),
                middle_name=input("Middle name: "),
                last_name=input("Surname: "),
                growth=int(input(f'Basketballer\'s height: '))
            )
            print_result(basketballer)

        elif choice == REMOVE_BASKETBALL_PLAYER:
            del_player = del_basketballer(surname=input("Enter surname: "))
            print_result(del_player)

        elif choice == FIND_BASKETBALL_PLAYER:
            surname = input("Enter surname: ")
            search_basketballer = find_basketballer(surname)
            print_result(search_basketballer)

        elif choice == UPDATE_BASKETBALL_PLAYER:
            update_basketball_player = update_basketballer(
                surname=input("Surname: ")
            )
            print_result(update_basketball_player)
