#User Inputs - mood & note;
#Program will store data then AI will analyze patterns
#Outputs will be insights like you feel most productive on weekdays
from datetime import datetime

def inputFunc():
    date = datetime.now().strftime("%Y-%m-%d")
    print("What is your mood today?")
    print("Selection: Happy, Sad, Angry, Neutral")
    
    mood = input("Enter your mood: ")
    mood = mood.capitalize()
    note = input("Note: ")
    entry = mood + "|" + note + "|" + date + "\n"
    with open ("MoodNoteFileData.txt", "a") as file:
        file.write(entry)
   
#This is our AI
def analyzeMood():
    mood_count = {}
      
    with open("MoodNoteFileData.txt", "r") as file: 
        for line in file:
            mood, note, date = line.strip().split("|")      

            if  mood in mood_count:
                mood_count[mood] += 1
            else: 
                mood_count[mood] = 1
                
            if ("study") in note.lower():
                print("You are a nerd.")
                
            
    if mood_count:
        most_common = max(mood_count, key=mood_count.get)
        
    else:
        print("No entry yet.")
        return
        
    print ("Most common mood:", most_common)
    print("Insight:", end = " ")
    if most_common == "Happy":
        print("You are a happy bitch.")
    elif most_common == "Sad": 
        print("you need therapy sister.")
    elif most_common == "Angry":
        print("You have anger management issues or your environment are full of stressors.")
    elif most_common == "Neutral":
        print("Bland.")
    
    total = sum(mood_count.values())
    print("\nMood Distribution")
    for mood in mood_count:
        percent = (mood_count[mood] /total) * 100
        print(f"{mood}: {percent:.2f}")
    
def showAllEntries():
    i = 1
    with open ("MoodNoteFileData.txt", "r") as file:
        for line in file: 
            mood, note, date = line.strip().split("|")
            print("\nEntry #" + str(i))
            print("Date: " + date)
            print("Mood: "+ mood)
            print("Note: " + note)
            i = i + 1
            
            
    
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