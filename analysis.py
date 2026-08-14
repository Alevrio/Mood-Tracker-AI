def count_moods(df):
    return df['mood'].value_counts()

def most_common_mood(df):
    mood_counts = count_moods(df)
    if mood_counts.empty:
            return None
    
    highest_count = mood_counts.max()
    highest_mood = mood_counts[mood_counts == highest_count]
                                
    return highest_mood.index.tolist(), int(highest_count)

def total_entries(df):
    return len(df)

def mood_percentages(df):
    mood_count = count_moods(df)
    mood_percentage = (mood_count / mood_count.sum()) * 100
    
    return mood_percentage.round(2)