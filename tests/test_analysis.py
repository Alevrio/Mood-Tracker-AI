import pandas as pd
from analysis import (
    total_entries, 
    count_moods, 
    most_common_mood, 
    mood_percentages, 
    add_time_features, 
    monthly_mood_distribution, 
    monthly_mood_insights
)

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

def test_add_time_features_single():
    df = pd.DataFrame({
    "mood": ["Happy"],
    "date": ["2026-08-01"]
    })
    
    result = add_time_features(df)
    assert result.loc[0,"year"] == 2026
    assert result.loc[0,"month"] == 8
    assert result.loc[0,"weekday"] == "Saturday"
    assert pd.api.types.is_datetime64_any_dtype(result["date"])

def test_add_time_features_multiple():
    df = pd.DataFrame({
    "mood": ["Happy", "Sad", "Neutral"],
    "date": [
        "2026-01-05",
        "2026-08-21",
        "2027-12-25"
    ]
    })
    
    result = add_time_features(df)
    assert result.loc[2,"year"] == 2027
    assert result.loc[2,"month"] == 12
    assert result.loc[2,"weekday"] == "Saturday"
    assert pd.api.types.is_datetime64_any_dtype(result["date"])

def test_add_time_features_original():
    original_df = pd.DataFrame({
    "mood": ["Happy"],
    "date": ["2026-08-01"]
    })

    result = add_time_features(original_df)
    assert "year" not in original_df
    assert "month" not in original_df
    assert "weekday" not in original_df
    assert original_df.loc[0, "date"] == "2026-08-01"

def test_add_time_features_empty():
    empty_df = pd.DataFrame()
    
    result = add_time_features(empty_df)
    assert result.empty
    
def test_monthly_mood_distributions_multiple():
    df = pd.DataFrame({
    "mood": [
        "Happy",
        "Happy",
        "Sad",
        "Sad",
        "Sad",
        "Neutral"
    ],
    "date": [
        "2026-08-01",
        "2026-08-02",
        "2026-08-03",
        "2026-09-01",
        "2026-09-02",
        "2026-09-03"
    ]
    })
    
    result = monthly_mood_distribution(df)
    assert result.loc[0, "Happy"] == 2
    assert result.loc[1, "Sad"] == 2

def test_monthly_mood_distributions_different_years():
    df = pd.DataFrame({
    "mood": ["Happy", "Happy", "Sad"],
    "date": [
        "2026-08-01",
        "2026-08-02",
        "2027-08-01"
    ]
    })
    result = monthly_mood_distribution(df)
    assert result.loc[0, "Happy"] == 2
    assert result.loc[1, "Sad"] == 1
    assert result.loc[0, "year"] == 2026
    assert result.loc[1, "year"] == 2027
    
def test_monthly_mood_distributions_empty():
    empty_df = pd.DataFrame()

    result = monthly_mood_distribution(empty_df)
    assert result.empty
    assert "year" in result.columns
    assert "month" in result.columns
    
def test_monthly_mood_insights_multiple():
    df = pd.DataFrame({
    "mood": [
        "Happy",
        "Happy",
        "Sad",
        "Sad",
        "Sad",
        "Neutral"
    ],
    "date": [
        "2026-08-01",
        "2026-08-02",
        "2026-08-03",
        "2026-09-01",
        "2026-09-02",
        "2026-09-03"
    ]
    })
    
    result = monthly_mood_insights(df)
    assert result.loc[0, "year"] == 2026
    assert result.loc[0, "month"] == 8
    assert result.loc[0, "most_common_moods"]== ["Happy"]
    assert result.loc[0, "count"] == 2

def test_monthly_mood_insights_tie():
    df = pd.DataFrame({
        "mood": [
            "Happy",
            "Sad",
            "Happy",
            "Sad",
            "Neutral"
        ],
        "date": [
            "2026-08-01",
            "2026-08-02",
            "2026-08-03",
            "2026-08-04",
            "2026-08-05"
        ]
    })
    
    result = monthly_mood_insights(df)
    assert result.loc[0, "year"] == 2026
    assert result.loc[0, "month"] == 8
    assert set(result.loc[0, "most_common_moods"]) == {"Happy", "Sad"}
    assert result.loc[0, "count"] == 2
    
def test_monthly_mood_insights_empty():
    empty_df = pd.DataFrame()
    
    result = monthly_mood_insights(empty_df)
    
    assert result.empty
    assert "year" in result.columns
    assert "month" in result.columns
    assert "most_common_moods" in result.columns
    assert "count" in result.columns