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
        choice = int(input("What's your choice: "))
        
        if choice == 4:
            break
        
        choices(choice)
        
if __name__ == "__main__":
    main()