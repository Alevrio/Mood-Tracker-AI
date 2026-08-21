import pandas as pd
from analysis import total_entries, count_moods, most_common_mood, mood_percentages

def test_total_entries_empty():
    df = pd.DataFrame()
    
    result = total_entries(df)
    
    assert result == 0
    
def test_total_entries_single_entry():
    df = pd.DataFrame({
        "Mood" : ["Happy"],
        "Note" : ["Because I'm happy"],
        "Data" : ["08-12-23"] 
        })
    
    result = total_entries(df)
    
    assert result == 1

def test_total_entries_multiple_entry():
    df = pd.DataFrame({
    "date": [
        "2023-08-12",
        "2023-08-13",
        "2023-08-14",
        "2023-08-15",
        "2023-08-16"
    ]
    })

    result = total_entries(df)
    
    assert result == 5
    
def test_count_moods_single():
    single_mood_df = pd.DataFrame({
    "mood": ["Happy"]
    })
    
    result = count_moods(single_mood_df)
    
    assert result["Happy"] == 1
    assert len(result) == 1
    
def test_count_moods_multiple():
    multiple_moods_df = pd.DataFrame({
    "mood": [
        "Happy",
        "Sad",
        "Happy",
        "Neutral",
        "Happy",
        "Sad"
    ]
    })

    result = count_moods(multiple_moods_df)
    
    assert result["Happy"] == 3
    assert result["Sad"] == 2
    assert result["Neutral"] == 1
    assert len(result) == 3
    
def test_count_moods_empty():
    empty_mood_df = pd.DataFrame({
    "mood": []
    })
    
    result = count_moods(empty_mood_df)

    assert result.empty
    
def test_most_common_mood_winner():
    winner_df = pd.DataFrame({
    "mood": ["Happy", "Happy", "Sad", "Neutral"]
    })
    
    mood, count = most_common_mood(winner_df)
    assert mood == ["Happy"] 
    assert count == 2

def test_most_common_mood_tie():
    tie_df = pd.DataFrame({
    "mood": ["Happy", "Sad", "Happy", "Sad", "Neutral"]
    })
    
    mood, count = most_common_mood(tie_df)
    assert mood == ["Happy", "Sad"]
    assert count == 2
    
def test_most_common_mood_empty():
    empty_df = pd.DataFrame({
    "mood": []
    })

    result = most_common_mood(empty_df)
    assert result is None

def test_mood_percentages_single():
    single_df = pd.DataFrame({
    "mood": ["Happy"]
    })
    
    result = mood_percentages(single_df)
    assert result["Happy"] == 100
    
def test_mood_percentages_multiple():
    multiple_df = pd.DataFrame({
    "mood": ["Happy", "Happy", "Sad", "Neutral"]
    })
    
    result = mood_percentages(multiple_df)
    assert result["Happy"] == 50
    assert result["Sad"] == 25
    assert result["Neutral"] == 25
    
    
def test_mood_percentages_rounding():
    rounding_df = pd.DataFrame({
    "mood": ["Happy", "Happy", "Sad"]
    })
    
    result = mood_percentages(rounding_df)
    assert result["Happy"] == 66.67
    assert result["Sad"] == 33.33

def test_mood_percentages_empty():
    empty_df = pd.DataFrame({
        "mood": []
    })

    result = mood_percentages(empty_df)
    assert result.empty
