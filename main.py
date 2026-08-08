#User Inputs - mood & note;
#Program will store data then AI will analyze patterns
#Outputs will be insights like you feel most productive on weekdays
from storage import inputFunc, showAllEntries
from analysis import analyzeMood

def choices(choice):
    match choice: 
        case 1:  
            return inputFunc()
        case 2:
            return analyzeMood()   
        case 3:
            return showAllEntries()
        case _:
            print("Wrong! Corner!")
               
    
def main():
    while True:
        print("1. Input Mood and Note")
        print("2. Show Analysis")
        print("3. Show all entries.")
        print("4. Exit")
       
        user_input = input("What's your choice: ").strip()
        
        if not user_input or not user_input.isdigit():
            print("Not a valid option (Choose selectively within the menu).")
            continue
        
        choice = int(user_input)
        
        if choice < 1 or choice > 4:
            print("Not a valid option (Choose selectively within the menu).")
            continue
                
        if choice == 4:
            return

        choices(choice)
        
        
if __name__ == "__main__":
    main()