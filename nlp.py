import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.feature_extraction.text import TfidfVectorizer

model = SentenceTransformer("all-MiniLM-L6-v2")

def has_enough_notes(notes, minimum_notes = 12):
    return len(notes) >= minimum_notes

def generate_embeddings(notes):
    if len(notes) == 0:
        return np.empty((0, 384))
    return model.encode(notes)

def choose_cluster_count(note_embeddings):
    number_of_notes = len(note_embeddings)
    
    maximum_k = min(5, number_of_notes-1)
    best_k = None
    best_score = float("-inf")
    
    for k in range(2, maximum_k+1):
        kmeans = KMeans(n_clusters = k, random_state = 42)
        cluster_labels = kmeans.fit_predict(note_embeddings)
        score = silhouette_score(note_embeddings, cluster_labels)
        
        if score > best_score:
            best_score = score
            best_k = k
    
    return best_k
        
def fit_note_clusters(note_embeddings, total_clusters):
    if note_embeddings.size == 0:
        return None, np.array([], dtype = int)
    
    clusterer = KMeans(n_clusters = total_clusters, random_state = 42)
    
    cluster_labels = clusterer.fit_predict(note_embeddings)
    
    return clusterer, cluster_labels

def find_representative_notes(notes, note_embeddings, cluster_labels, clusterer):
    
    representatives = {}
    
    for cluster_id in range(clusterer.n_clusters):
        cluster_embeddings = note_embeddings[cluster_labels == cluster_id]
        centroid = clusterer.cluster_centers_[cluster_id]
        distances = np.linalg.norm(cluster_embeddings - centroid, axis = 1)
        closest_index = np.argmin(distances)
        cluster_indices = np.where(cluster_labels == cluster_id)[0]
        original_index = cluster_indices[closest_index]
        representatives[cluster_id] = notes[original_index]
        
    return representatives

def extract_cluster_keywords(notes, cluster_labels, top_n = 3):
    notes = np.array(notes)
    keywords= {}
    
    for cluster_id in np.unique(cluster_labels):
        vectorizer = TfidfVectorizer(stop_words = "english")
        cluster_notes = notes[cluster_labels == cluster_id]
        tf_idf_matrix = vectorizer.fit_transform(cluster_notes)
        
        feature_keywords = np.array(vectorizer.get_feature_names_out())
        
        total_scores = np.asarray(tf_idf_matrix.sum(axis = 0)).ravel()
        
        top_indices = np.argsort(total_scores)[-top_n:][::-1]
        top_keywords = feature_keywords[top_indices].tolist()
        keywords[cluster_id] = top_keywords
        
    return keywords

