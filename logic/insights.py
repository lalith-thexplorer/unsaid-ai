import pandas as pd
from datetime import datetime, timedelta
import calendar
import random

def get_dummy_data():
    """
    Generates dummy mood data for demonstration purposes.
    Returns a list of dictionaries with 'timestamp' and 'moods'.
    """
    base_time = datetime.now()
    moods_list = ["Anxious", "Calm", "Sad", "Hopeful", "Tired", "Frustrated", "Grateful", "Numb"]
    
    data = []
    # Generate data for the last 5 days
    for day in range(5):
        for _ in range(random.randint(1, 4)): # 1-4 entries per day
            timestamp = base_time - timedelta(days=day, hours=random.randint(0, 23))
            selected_moods = random.sample(moods_list, k=random.randint(1, 3))
            data.append({
                "timestamp": timestamp,
                "moods": selected_moods
            })
    
    # Sort by time
    data.sort(key=lambda x: x['timestamp'])
    return data

def process_mood_data(mood_history):
    """
    Processes raw mood history into a DataFrame suitable for plotting.
    """
    if not mood_history:
        return pd.DataFrame()

    # Flatten the list: one row per mood entry
    flat_data = []
    for entry in mood_history:
        ts = entry['timestamp']
        # Round to nearest hour or day for better aggregation? 
        # For short term, maybe just Date + Part of Day
        date_str = ts.strftime("%Y-%m-%d")
        time_str = ts.strftime("%H:%M")
        
        for mood in entry['moods']:
            flat_data.append({
                "Date": date_str,
                "Time": time_str,
                "Mood": mood,
                "Count": 1
            })
            
    df = pd.DataFrame(flat_data)
    return df


def get_mood_counts(df):
    """Returns total counts per mood for a summary chart."""
    if df.empty:
        return pd.DataFrame()
    return df['Mood'].value_counts().reset_index()

# ---------------------------------------------------------
# Advanced Analytics Functions (Widgets)
# ---------------------------------------------------------

def calculate_streak(df):
    """
    Calculates the current streak of consecutive days with check-ins.
    """
    if df.empty:
        return 0
    
    # Ensure dates are datetime objects and sorted
    dates = pd.to_datetime(df['Date']).dt.date.unique()
    dates.sort()
    
    if len(dates) == 0:
        return 0

    streak = 0
    today = datetime.now().date()
    
    # Check if user checked in today or yesterday to keep streak alive
    if dates[-1] != today and dates[-1] != (today - timedelta(days=1)):
        return 0 # Streak broken
        
    current = dates[-1]
    
    # Iterate backwards to find consecutive days
    for i in range(len(dates) - 1, -1, -1):
        if dates[i] == current:
            streak += 1
            current -= timedelta(days=1)
        else:
            break
            
    return streak

def get_consistency_matrix(df):
    """
    Returns a dataframe for a 'GitHub-style' contribution graph.
    Showing last 4 weeks (28 days).
    """
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=27) # Last 28 days
    
    all_dates = pd.date_range(start=start_date, end=end_date).date
    
    # Check if date exists in data
    checkin_dates = set(pd.to_datetime(df['Date']).dt.date) if not df.empty else set()
    
    matrix_data = []
    for d in all_dates:
        status = 1 if d in checkin_dates else 0
        matrix_data.append({
            'Date': d,
            'Day': d.strftime('%a'), # Mon, Tue...
            'Week': d.strftime('%U'), # Week number
            'Status': status
        })
        
    return pd.DataFrame(matrix_data)

def get_monthly_mood_calendar(df):
    """
    Returns mood for each day in current month for Calendar View.
    """
    if df.empty:
        return {}

    current_month_str = datetime.now().strftime("%Y-%m")
    # Filter for current month
    mask = df['Date'].apply(lambda x: str(x).startswith(current_month_str))
    month_df = df[mask]
    
    calendar_map = {}
    if not month_df.empty:
        # Get dominant mood for each day
        daily_groups = month_df.groupby('Date')['Mood'].agg(lambda x: x.mode()[0])
        for date, mood in daily_groups.items():
            day_int = int(str(date).split('-')[-1]) # Extract day number
            calendar_map[day_int] = mood
            
    return calendar_map

def get_week_progress(df):
    """
    Returns check-in status for each day of the current week (M T W T F S S).
    """
    today = datetime.now().date()
    # Get start of week (Monday)
    start_of_week = today - timedelta(days=today.weekday())
    
    days = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
    checkin_dates = set(pd.to_datetime(df['Date']).dt.date) if not df.empty else set()
    
    week_data = []
    for i, day_label in enumerate(days):
        day_date = start_of_week + timedelta(days=i)
        is_active = day_date in checkin_dates
        is_today = day_date == today
        week_data.append({
            'label': day_label,
            'active': is_active,
            'is_today': is_today
        })
    
    return week_data

def get_full_calendar_grid(df):
    """
    Returns a full month calendar grid with mood colors.
    Returns list of weeks, each week is a list of day dicts.
    """
    today = datetime.now()
    year = today.year
    month = today.month
    
    # Get first day of month and number of days
    first_weekday, num_days = calendar.monthrange(year, month)
    
    # Get mood map
    mood_calendar = get_monthly_mood_calendar(df)
    
    # Build grid
    weeks = []
    current_week = [None] * first_weekday  # Pad start of month
    
    for day in range(1, num_days + 1):
        mood = mood_calendar.get(day, None)
        current_week.append({
            'day': day,
            'mood': mood,
            'is_today': day == today.day
        })
        
        if len(current_week) == 7:
            weeks.append(current_week)
            current_week = []
    
    # Pad end of month
    if current_week:
        current_week.extend([None] * (7 - len(current_week)))
        weeks.append(current_week)
    
    return weeks, calendar.month_name[month]
