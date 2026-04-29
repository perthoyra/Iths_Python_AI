from os import system, name
from time import sleep
import menu


def clear_screen() -> None:
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def main():
    thisdict = {
        1: "Select option 1.",
        2: "Select option 2.",
        0: "Exit"
        }
    
    myMenu = menu.MyMenu(thisdict)
    
    while True:
        clear_screen()
        myMenu.draw_menu()
        selected = myMenu.get_input()
        
        print(selected)
        
        match selected:
            case 0:
                print("Terminating program...")
                break
            case 1,2:
                print("\n")
                print(thisdict[selected])
                print("\n")
                sleep(2)

        # it is a bit quick, so the resulkt is not visible long enough
        _ = input()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()