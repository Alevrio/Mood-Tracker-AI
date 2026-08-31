import streamlit as st
from storage import save_mood_entry, load_data
from analysis import (
    total_entries,
    most_common_mood,
    count_moods,
    monthly_mood_distribution
)
from life_patterns import build_life_patterns
st.set_page_config(
    page_title = "Mood Tracker",
    page_icon="🌱",
    layout = "wide",
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Journal",
        "Analytics",
        "Life Patterns",
    ]
)

if page == "Home":
    st.title("🌱 Mood Tracker")
    st.write(
        "Track your mood, explore your history, "
        "and discover patterns over time."
    )
    
    mood = st.selectbox(
        "How are you feeling?",
        ["Happy", "Neutral", "Sad", "Angry"],
        index = None,
        placeholder = "Select your mood"
    )
    
    note = st.text_area("What's on your mind?")
    
    if st.button("Save Entry"):
        if mood is None:
            st.warning("Please choose a mood first.")
        else:
            save_mood_entry(mood, note)
            st.success("Mood Entry Saved!")

elif page == "Journal":
    st.title("📖 Journal")
    
    df = load_data()
    
    if df.empty:
        st.info("No mood entries yet.")
    
    else: 
        journal_df = df.copy()
        journal_df = journal_df.sort_values("date", ascending = False)
    
        for _, entry in journal_df.iterrows():
            with st.container(border = True):
                col1, col2 = st.columns([1, 3])
                
                with col1:
                    st.markdown(f"**{entry['mood']}**")
                    
                with col2:
                    st.caption(entry['date'].strftime("%B %d, %Y"))

                if entry["note"]:
                    st.write(entry["note"])
                    
                else:
                    st.caption("No note added.")
                    
elif page == "Analytics":
    st.title("📊 Analytics")
    df = load_data()
    
    if df.empty:
        st.info("Add some mood entries to see your analytics.")
    else:
        col1, col2 = st.columns(2)
        common_moods, common_count = most_common_mood(df)
        common_mood_text = ", ".join(common_moods)
        
        with col1:
            st.metric("Total Entries", total_entries(df))
        with col2:
            st.metric(
                "Most Common Mood",
                common_mood_text,
            )
        
        mood_counts = count_moods(df)
        st.subheader("Mood Distribution")
        st.bar_chart(mood_counts)
        
        monthly_data= monthly_mood_distribution(df)
        monthly_chart = monthly_data.copy()
        
        monthly_chart["period"] = (monthly_chart["year"].astype(str) + "-" + monthly_chart["month"].astype(str).str.zfill(2))
        monthly_chart = monthly_chart.set_index("period")
        monthly_chart = monthly_chart.drop(columns = ["year", "month"])
        
        st.subheader("Monthly Mood Trends")
        st.bar_chart(monthly_chart)
        
elif page == "Life Patterns":
    st.title("✨ Life Patterns")
    
    df = load_data()
    
    if df.empty:
        st.info(
            "Start logging your moods to discover Life Patterns."
        )

    elif len(df) < 12:
        st.info(
            f"Keep journaling — you have {len(df)} of 12 "
            "entries needed to unlock Life Patterns."
        )
    
        st.progress(len(df) / 12)
    
    else:
        with st.spinner("Looking for patterns in your journal"):
            patterns = build_life_patterns(df)
            
            if not patterns:
                st.info(
                    "You have enough history, but no recurring "
                    "patterns have enough evidence yet."
                )
            
            else: 
                for pattern in patterns:
                    with st.container(border = True):
                        st.subheader(
                            " • ".join(pattern["keywords"])
                        )
                        
                        st.caption(
                            f"Based on {pattern['entry_count']} entries"
                        )
                        
                        st.write(pattern["mood_insight"])
                        st.write(pattern["time_insight"])
                        
                        st.markdown("**Representative Entry**")
                        st.write(                                                       
                            f'"{pattern["representative_note"]}"'
                        )
                        
                       