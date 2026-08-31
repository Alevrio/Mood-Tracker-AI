from main import build_life_patterns
import main
import pandas as pd
import numpy as np 
def test_build_life_patterns_not_enough_notes():
    df = pd.DataFrame({
    "mood": ["Happy"] * 5,
    "note": ["Some note"] * 5,
    "date": ["2026-08-01"] * 5,
    })
    
    result = build_life_patterns(df)
    
    assert result == []

def test_build_life_patterns_orchestration(monkeypatch):
    df = pd.DataFrame({
        "mood": ["Happy"] * 12,
        "note": [f"Note {i}" for i in range(12)],
        "date": ["2026-08-01"] * 12,
    })

    fake_labels = np.array([
        0, 0, 0, 0, 0, 0,   # 6
        1, 1, 1, 1,       # 4
        2, 2,            # 2 -> should be filtered
    ])

    def fake_generate_embeddings(notes):
        return np.zeros((12,384))

    monkeypatch.setattr(main, "generate_embeddings", fake_generate_embeddings)
    monkeypatch.setattr(main, "choose_cluster_count", lambda embeddings : 3)
    fake_clusterer = object()
    monkeypatch.setattr(main, "fit_note_clusters", lambda embeddings, total_clusters:(fake_clusterer, fake_labels))
    monkeypatch.setattr(
        main,
        "find_representative_notes",
        lambda notes, embeddings, labels, clusterer: {
            0: "Representative A",
            1: "Representative B",
            2: "Representative C",
        }
    )

    monkeypatch.setattr(
        main,
        "extract_cluster_keywords",
        lambda notes, labels: {
            0: ["academic", "exam"],
            1: ["gaming", "valorant"],
            2: ["friends", "social"],
        }
    )
    
    fake_mood_data = pd.DataFrame({
    "cluster": [0, 1, 2],
    "mood": ["Sad", "Happy", "Neutral"],
    "count": [6, 4, 2],
    "cluster_total": [6, 4, 2],
    "percentage": [100.0, 100.0, 100.0],
    })
    
    monkeypatch.setattr(
    main,
    "mood_distribution_by_cluster",
    lambda df, labels: fake_mood_data
    )
    
    fake_time_data = pd.DataFrame({
    "year": [2026, 2026, 2026],
    "month": [8, 9, 10],
    "cluster": [0, 1, 2],
    "count": [6, 4, 2],
    })
    
    monkeypatch.setattr(
    main,
    "monthly_cluster_distribution",
    lambda df, labels: fake_time_data
    )
    
    monkeypatch.setattr(
    main,
    "generate_mood_insight",
    lambda data: "Fake mood insight"
    )

    monkeypatch.setattr(
        main,
        "generate_time_insight",
        lambda data: "Fake time insight"
    )
    
    result = main.build_life_patterns(df)
    assert len(result) == 2
    assert all(pattern["cluster"] != 2 for pattern in result)
    first_pattern = result[0]
    assert first_pattern["cluster"] == 0
    assert first_pattern["keywords"] == ["academic", "exam"]
    assert first_pattern["representative_note"] == "Representative A"
    assert first_pattern["entry_count"] == 6
    assert first_pattern["mood_insight"] == "Fake mood insight"
    assert first_pattern["time_insight"] == "Fake time insight"