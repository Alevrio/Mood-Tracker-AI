import matplotlib.pyplot as plt
import numpy as np
from analysis import monthly_mood_distribution

def plot_mood_counts(mood_counts):
    fig, ax = plt.subplots(figsize = (8, 4))
    ax.set_title("Mood Counts")
    
    if mood_counts.empty: 
        ax.text(0.5, 0.5, "No mood data available", transform=ax.transAxes, ha="center", va="center")
        ax.axis('off')
        return fig,ax
    
    x = mood_counts.index
    y = mood_counts.values
    
    ax.bar(x, y)
    ax.set_xlabel("Mood")
    ax.set_ylabel("Counts")
    
    return fig, ax

def plot_monthly_mood_distribution(df):
    fig, ax = plt.subplots(figsize = (8, 4)) 
    ax.set_title("Monthly Mood Distribution")
    
    if df.empty: 
        ax.text(0.5, 0.5, "No mood data available", transform=ax.transAxes, ha="center", va="center")
        ax.axis('off')
        return fig,ax
    
    monthly_data = monthly_mood_distribution(df)
    
    x_labels = [
        f"{year}-{month:02d}"
        for year, month, in zip(monthly_data["year"], monthly_data["month"])
    ]
    
    mood_columns = monthly_data.columns.difference(["year", "month"]) 
    num_moods = len(mood_columns)
    
    x = np.arange(len(x_labels))

    group_width = 0.8
    bar_width = group_width / num_moods
        
    for i, mood in enumerate(mood_columns):
        offset = (i - (num_moods - 1)/ 2) * bar_width
        positions = x + offset
        
        ax.bar(
            positions,
            monthly_data[mood],
            width = bar_width,
            label = mood
        )
        
    ax.set_xlabel("Months & Years")
    ax.set_ylabel("Mood Count")
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)
    ax.legend()
    
    return fig, ax