from storage import input_mood_entry, show_all_entries, load_data
from analysis import (
    count_moods,
    most_common_mood,
    total_entries,
    mood_percentages,
    monthly_mood_insights,
)

from visualization import plot_monthly_mood_distribution
import matplotlib.pyplot as plt


def choices(choice):
    match choice: 
        case 1:  
            return input_mood_entry()
        case 2:
            return analysis_menu()
        case 3:
            return show_all_entries()
        case _:
            print("Please input a correct choice")

def analysis_menu():
    while True:
        print("\nANALYSIS MENU")
        print("1) Overall Mood Summary")
        print("2) Monthly Mood Insights")
        print("3) Monthly Mood Chart")
        print("4) Back")
        
        choice = get_menu_choice(1,4)
                
        if choice == 4:
            return
        
        match choice: 
            case 1:  
                show_overall_analysis()
            case 2:
                show_monthly_insights()
            case 3:
                show_monthly_chart()
            case _:
                print("Please input a correct choice")

              
def show_overall_analysis():
    df = load_data()
    if df.empty:
        print("There are no data. Please input first!")
        return
    
    print("\n=== Mood Analysis ===")
    
    print("\nMood Counts: ")
    mood_counts = count_moods(df)
    for mood, count in mood_counts.items():
        print(f"{mood}: {count}")
    
    common_mood, count = most_common_mood(df)

    print(f"\nMost Common Mood(s): {', '.join(common_mood)}")
    print(f"Count: {count}")
    
    print("\nTotal Entries:", total_entries(df))
    
    print("\nMood Percentages:")
    percentages = mood_percentages(df)
    for mood, percentage in percentages.items():
        print(f"{mood}: {percentage}%") 
    
def show_monthly_insights():
    df = load_data()
    
    if df.empty:
        print("There are no data. Please input first!")
        return

    print("\n=== Monthly Insights ===")
    monthly_insights = monthly_mood_insights(df)
    for _, row in monthly_insights.iterrows():
        print(f"\n{row["year"]}-{row["month"]:02d}")
        print(f"Most Common Mood(s): {', '.join(row["most_common_moods"])}")
        print("Count: ",row["count"])

def show_monthly_chart():
    df = load_data()

    if df.empty:
        print("There are no data. Please input first!")
        return
    
    fig, ax = plot_monthly_mood_distribution(df)
    plt.show()
    
def get_menu_choice(minimum, maximum):
    while True:
        user_input = input("What's your choice: ").strip()
        
        if not user_input or not user_input.isdigit():
            print("Not a valid option (Choose selectively within the menu).")
            continue
        
        choice = int(user_input)
        
        if choice < minimum or choice > maximum:
            print("Not a valid option (Choose selectively within the menu).")
            continue
        
        return choice

def main():
    while True:
        print("1. Input Mood and Note")
        print("2. Show Analysis")
        print("3. Show all entries.")
        print("4. Exit")
        
        choice = get_menu_choice(1,4)
        
        if choice == 4:
            return

        choices(choice)
        
        
if __name__ == "__main__":
    main()