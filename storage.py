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
            