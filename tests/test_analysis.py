import pandas as pd
from analysis import total_entries, count_moods

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