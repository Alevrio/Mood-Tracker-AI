import numpy as np
from nlp import generate_embeddings, fit_note_clusters, choose_cluster_count, find_representative_notes

def test_generate_embeddings_normal():
    notes = [
        "I studied for my exam",
        "I played games with friends"
    ]

    result = generate_embeddings(notes)

    assert isinstance(result, np.ndarray)
    assert result.shape == (2, 384)

def test_generate_embeddings_empty():
    empty_note = []

    result = generate_embeddings(empty_note)

    assert isinstance(result, np.ndarray)
    assert result.shape == (0, 384)
    assert result.size == 0
    
def test_fit_note_clusters_normal():
    embeddings = np.array([
    [1.0, 1.0],
    [1.1, 1.1],
    [8.0, 8.0],
    [8.1, 8.1],
    ])
    
    clusterer, labels = fit_note_clusters(embeddings, 2)
    assert clusterer.cluster_centers_.shape == (2,2)
    assert labels[0] == labels[1]
    assert labels[2] == labels[3]
    assert labels[0] != labels[2] 

def test_fit_note_clusters_empty():
    embeddings = np.array([])

    clusterer, labels = fit_note_clusters(embeddings, 0)
    
    assert clusterer is None
    assert labels.shape == (0,)
    assert labels.size == 0
    
def test_choose_cluster_count():
    embeddings = np.array([
    # Group A
    [1.0, 1.0],
    [1.1, 1.0],
    [0.9, 1.1],

    # Group B
    [5.0, 5.0],
    [5.1, 5.0],
    [4.9, 5.1],

    # Group C
    [9.0, 1.0],
    [9.1, 1.0],
    [8.9, 1.1],
    ])
    
    result = choose_cluster_count(embeddings)
    assert result == 3 
    
def test_choose_cluster_count_not_enough_notes():
    embeddings = np.array([
    [1, 1],
    [2, 2]
    ])
    
    result = choose_cluster_count(embeddings)
    assert result is None
    
def test_find_representative_notes():
    notes = [
        "Group A first",
        "Group A center",
        "Group A third",
        "Group B first",
        "Group B center",
        "Group B third",
    ]

    embeddings = np.array([
        [0.9, 1.0],
        [1.0, 1.0],
        [1.1, 1.0],

        [7.9, 8.0],
        [8.0, 8.0],
        [8.1, 8.0],
    ])

    clusterer, labels = fit_note_clusters(embeddings, 2)

    representatives = find_representative_notes(notes, embeddings, labels, clusterer)
    
    assert set(representatives.values()) == {
        "Group A center",
        "Group B center",
    }
    
    assert len(representatives) == 2