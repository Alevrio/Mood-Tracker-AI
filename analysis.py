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