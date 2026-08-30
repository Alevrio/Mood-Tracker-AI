import pandas as pd

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
    mood_counts = count_moods(df)
    mood_percentage = (mood_counts / mood_counts.sum()) * 100
    
    return mood_percentage.round(2)

def add_time_features(df):
    df = df.copy()
    if df.empty: 
        return df
    
    df['date'] = pd.to_datetime(df['date'], format = "%Y-%m-%d")
    
    df['year'], df['month'], df['weekday'] = (
        df['date'].dt.year, 
        df['date'].dt.month, 
        df['date'].dt.day_name()
        )
    
    return df

def monthly_mood_insights(df):
    result = add_time_features(df)
    
    if result.empty:
        return pd.DataFrame(columns= ["year","month","most_common_moods", "count"])
        
    grouped = result.groupby(["year", "month"])
    monthly_results = []
    
    for (year, month), monthly_data in grouped:
        common_moods, count = most_common_mood(monthly_data)
        new_row = {"year": year, "month": month, "most_common_moods": common_moods, "count" :count}
        monthly_results.append(new_row)
        
    summary_df = pd.DataFrame(monthly_results)
    return summary_df

def monthly_mood_distribution(df):
    result = add_time_features(df)
    
    if result.empty:
        return pd.DataFrame(columns= ["year","month"])

    grouped = result.groupby(["year", "month"])
    
    monthly_results = []
    
    for (year, month), monthly_data in grouped:
        moods = count_moods(monthly_data)
        new_row = {"year": year, "month": month}
        new_row.update(moods)
        monthly_results.append(new_row)
        
        
    summary_df = pd.DataFrame(monthly_results)
    summary_df = summary_df.fillna(0)
    mood_columns = summary_df.columns.difference(["year","month"])
    summary_df[mood_columns] = summary_df[mood_columns].astype(int)
    
    return summary_df

def mood_distribution_by_cluster(df, cluster_labels):
    cluster_df = df.copy()
    cluster_df["cluster"] = cluster_labels
    
    grouped_cluster_df = cluster_df.groupby(["cluster", "mood"]).size().reset_index(name="count")
    grouped_cluster_df["cluster_total"] = grouped_cluster_df.groupby("cluster")["count"].transform("sum")
    grouped_cluster_df["percentage"] = ((grouped_cluster_df["count"] / grouped_cluster_df["cluster_total"]) * 100).round(2)
  
    return grouped_cluster_df

def monthly_cluster_distribution(df, cluster_labels):
    cluster_df = add_time_features(df)
    
    if cluster_df.empty:
        return pd.DataFrame(columns = ["year", "month", "cluster", "count"]) 
    
    cluster_df["cluster"] = cluster_labels
    monthly_clusters = cluster_df.groupby(["year", "month", "cluster"]).size().reset_index(name = "count")
    
    return monthly_clusters
    