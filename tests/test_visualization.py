import matplotlib
matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt

from visualization import plot_mood_counts, plot_monthly_mood_distribution

def test_plot_mood_counts_bars():
    mood_counts = pd.Series({
        "Happy": 3,
        "Sad": 2,
        "Neutral": 1
    })
    
    fig,ax = plot_mood_counts(mood_counts)
    
    assert len(ax.patches) == 3
    assert ax.patches[0].get_height() == 3
    assert ax.patches[1].get_height() == 2
    assert ax.patches[2].get_height() == 1
    
    plt.close(fig)
    
def test_plot_mood_counts_labels():
    mood_counts = pd.Series({
            "Happy": 3,
            "Sad": 2,
            "Neutral": 1
        })
        
    fig,ax = plot_mood_counts(mood_counts)
    
    assert ax.get_title() == "Mood Counts"
    assert ax.get_xlabel() == "Mood"
    assert ax.get_ylabel() == "Counts"

    plt.close(fig)
    
def test_plot_mood_counts_empty():
    empty_counts = pd.Series(dtype= int)
    
    fig, ax = plot_mood_counts(empty_counts)
    
    assert len(ax.patches) == 0
    assert len(ax.texts) == 1
    assert ax.texts[0].get_text() == "No mood data available"
    
    plt.close(fig)

def test_plot_monthly_mood_distributions_bars():
    df = pd.DataFrame({
    "mood": [
        "Happy",
        "Sad",
        "Happy",
        "Sad"
    ],
    "date": [
        "2026-08-01",
        "2026-08-02",
        "2026-09-01",
        "2026-09-02"
    ]
    })
    
    fig, ax = plot_monthly_mood_distribution(df)
    assert len(ax.patches) == 4
    plt.close(fig)

def test_plot_monthly_mood_distributions_labels():
    df = pd.DataFrame({
    "mood": [
        "Happy",
        "Sad",
        "Happy",
        "Sad"
    ],
    "date": [
        "2026-08-01",
        "2026-08-02",
        "2026-09-01",
        "2026-09-02"
    ]
    })
    
    fig, ax = plot_monthly_mood_distribution(df)
    x_labels = [
        label.get_text()
        for label in ax.get_xticklabels()
    ]
    
    legend = ax.get_legend()
    legend_labels = [
        label.get_text()
        for label in legend.get_texts()
    ]
    assert ax.get_title() == "Monthly Mood Distribution"
    assert ax.get_xlabel() == "Months & Years"
    assert ax.get_ylabel() == "Mood Count"
    assert x_labels == ["2026-08", "2026-09"]
    assert set(legend_labels) == {"Happy", "Sad"}
    plt.close(fig)
    
def test_plot_monthly_mood_distributions_empty():
    empty_df = pd.DataFrame()
    fig, ax = plot_monthly_mood_distribution(empty_df)
    
    assert len(ax.patches) == 0
    assert len(ax.texts) == 1
    assert ax.texts[0].get_text() == "No mood data available"
    
    plt.close(fig)