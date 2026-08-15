from analysis import total_entries, mood_percentages, count_moods
from storage import load_data
from visualization import plot_mood_counts
import matplotlib.pyplot as plt

df = load_data()
mood_counts = count_moods(df)

fig, ax = plot_mood_counts(mood_counts)

plt.show()

df = load_data()
mood_counts = count_moods(df)
fig, ax = plot_mood_counts(mood_counts)

plt.show()

    