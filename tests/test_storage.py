import pandas as pd
from storage import load_data

def test_load_data_missing_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    
    result = load_data()
    
    assert result.empty
    assert list(result.columns) == ["mood", "note", "date"]
    
def test_load_data_existing_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    
    data_file = tmp_path / "MoodNoteFileData.txt"
    
    data_file.write_text(
    "Happy|Finished my project|2026-08-01\n"
    "Sad|Had a tiring day|2026-08-02\n"
    "Neutral|Normal day|2026-08-03\n"
    )
    
    result = load_data()
    assert len(result) == 3
    assert result.loc[0, "mood"] == "Happy"
    assert result.loc[1, "note"] == "Had a tiring day"
    assert result.loc[2, "date"] == pd.Timestamp("2026-08-03")
    assert pd.api.types.is_datetime64_any_dtype(result["date"])
    
def test_load_data_existing_empty_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    
    data_file = tmp_path / "MoodNoteFileData.txt"
    data_file.write_text("")
    
    result = load_data()
    assert result.empty
    assert list(result.columns) == ["mood", "note", "date"]