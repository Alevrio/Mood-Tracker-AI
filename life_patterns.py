from nlp import (
    has_enough_notes,
    generate_embeddings,
    choose_cluster_count,
    fit_note_clusters,
    find_representative_notes,
    extract_cluster_keywords
)

from analysis import (
    mood_distribution_by_cluster,
    monthly_cluster_distribution,
    generate_time_insight,
    generate_mood_insight
)

import numpy as np

def build_life_patterns(df):
    notes = df["note"].tolist()
    
    if not has_enough_notes(notes):
        return []
    
    embeddings = generate_embeddings(notes)
    total_clusters = choose_cluster_count(embeddings)
    clusterer, cluster_labels = fit_note_clusters(embeddings, total_clusters)
    representatives = find_representative_notes(notes, embeddings, cluster_labels, clusterer)
    keywords = extract_cluster_keywords(notes, cluster_labels)
    mood_data = mood_distribution_by_cluster(df, cluster_labels)
    time_data = monthly_cluster_distribution(df,cluster_labels)
    patterns = []
    
    for cluster_id in np.unique(cluster_labels):
        cluster_mood_data = mood_data[mood_data["cluster"] == cluster_id]
        cluster_time_data = time_data[time_data["cluster"] == cluster_id]
        entry_count = int(cluster_mood_data["cluster_total"].iloc[0])
        
        if entry_count < 3:
            continue
        
        mood_insight = generate_mood_insight(cluster_mood_data)
        time_insight = generate_time_insight(cluster_time_data)
        pattern = {
            "cluster": int(cluster_id),
            "keywords": keywords[cluster_id],
            "representative_note": representatives[cluster_id],
            "entry_count": entry_count,
            "mood_insight": mood_insight,
            "time_insight": time_insight,
        }
        patterns.append(pattern)
    
    return patterns