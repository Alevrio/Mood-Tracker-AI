from datetime import datetime

def inputFunc():
    selection = ["Happy", "Sad", "Angry", "Neutral"]
    date = datetime.now().strftime("%Y-%m-%d")

    print("What is your mood today?")
    print("Selection: Happy, Sad, Angry, Neutral")
    
    check = True
    while(check):
        user_input = input("Enter your mood: ").strip()
        
        if not user_input:
            print("Not a valid option (Choose selectively within the menu).")
            continue
                
        mood = user_input.capitalize()
        
        if mood not in selection:
            print("Your input is not in our selection. Please try again.")
            continue
        
        note = input("Note: ")
        entry = mood + "|" + note + "|" + date + "\n"
        with open ("MoodNoteFileData.txt", "a") as file:
            file.write(entry)
        check = False
   
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
            