from datetime import datetime
import pandas as pd
import os

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
        entry = f"{mood}|{note}|{date}\n"
        
        with open ("MoodNoteFileData.txt", "a") as file:
            file.write(entry)

        check = False
   
def showAllEntries():
    if not os.path.exists("MoodNoteFileData.txt"):
        print("File does not exist, Maybe start adding a mood first.")
        return
    
    i = 1
    with open ("MoodNoteFileData.txt", "r") as file:
        for line in file: 
            parts = line.strip().split("|")
            if len(parts) == 3:
                mood, note, date = parts
                print("\nEntry #" + str(i))
                print("Date: " + date)
                print("Mood: "+ mood)
                print("Note: " + note)
                i = i + 1

def load_data():
    if not os.path.exists("MoodNoteFileData.txt"):
        df = pd.DataFrame(columns=["mood", "note","date"])
      
    else:
        df = pd.read_csv(
            "MoodNoteFileData.txt", 
            sep = "|", 
            names = ["mood", "note", "date"], 
            skip_blank_lines = True)
    
    df['date'] = pd.to_datetime(df['date'])
    return df

   