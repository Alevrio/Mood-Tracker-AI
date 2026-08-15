import matplotlib.pyplot as plt

def plot_mood_counts(mood_counts):
    fig, ax = plt.subplots()
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