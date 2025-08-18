import time
from plyer import notification
import requests
from datetime import datetime, timedelta

# --- Pushover Credentials ---
# Replace with actual keys.
user_key = 'ADD YOUR USER KEY FROM PUSHOVER APP' # to add another user just add it within the user list with a comma
api_token = 'ADD YOUR API TOKEN FROM PUSHOVER WEBSITE' # Your personal api token only, do not share with anyone.

# To change any subjects or time, just replace the subject names or time below. 
# To add another subject, just add it exactly how it was added in the previous ones.

# --- Subject Timetable ---
# Times are in 24-hour format.
schedule = {
    'Monday': {
        'AP Research': '08:00',
        'Maths': '09:25',
        'Science': '10:35',
        'Homeroom or Clubs': '11:45',
        'Social Studies': '12:50',
    },
    'Tuesday': {
        'CSP': '08:00',
        'Music': '09:25',
        'Maths': '10:35',
        'Homeroom or Clubs': '11:45',
        'Social Studies': '12:50',
    },
    'Wednesday': {
        'Social Studies': '08:00',
        'AP Research': '09:25',
        'Maths': '10:35',
        'Homeroom or Clubs': '11:45',
        'Science': '12:50',
    },
    'Thursday': {
        'Maths': '08:00',
        'CSP': '09:25',
        'Science': '10:35',
        'Homeroom or Clubs': '11:45',
        'AP Research': '12:50',
    },
    'Friday': {
        'Music': '08:00',
        'Science': '09:25',
        'AP Research': '10:35',
        'Homeroom or Clubs': '11:45',
        'Social Studies': '12:50',
    }
}

def send_notification(subject):
    """Sends a Pushover notification to the phone and a desktop notification to the laptop."""
    message = f"Reminder: Your next class is {subject} starting in 15 minutes."
    title = "Upcoming Class Reminder"

    # Send to phone via Pushover
    payload = {
        'token': api_token,
        'user': user_key,
        'message': message,
        'title': title,
    }
    
    try:
        response = requests.post("https://api.pushover.net/1/messages.json", data=payload)
        response.raise_for_status()
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Phone notification sent for '{subject}'.")
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error sending phone notification: {e}")

    # Send to laptop via plyer
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="Schedule Notifier",
            timeout=10  # Notification will disappear after 10 seconds
        )
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Laptop notification sent for '{subject}'.")
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error sending laptop notification: {e}")

def main():
    """Main loop to check the schedule and send notifications."""
    print("--------------------------------------------------")
    print("Schedule Notifier Command-Line Script Started")
    print("Press Ctrl+C to stop the script.")
    print("--------------------------------------------------")
    
    if not user_key or not api_token:
        print("ERROR: Pushover user key or API token is missing. Please update the script.")
        return

    sent_notifications_today = set()
    last_day_checked = datetime.now().weekday()

    while True:
        try:
            now = datetime.now()
            current_day = now.strftime('%A')
            
            if now.weekday() != last_day_checked:
                sent_notifications_today.clear()
                print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] New day ({current_day}). Notification history cleared.")
                last_day_checked = now.weekday()
            
            if current_day in schedule:
                todays_schedule = schedule[current_day]
                
                for subject, subject_time_str in todays_schedule.items():
                    try:
                        subject_time = datetime.strptime(subject_time_str, '%H:%M').time()
                        subject_datetime = datetime.combine(now.date(), subject_time)
                    except ValueError:
                        print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Invalid time format for '{subject}' on {current_day}: '{subject_time_str}'. Skipping.")
                        continue
                    
                    reminder_time = subject_datetime - timedelta(minutes=15)
                    
                    if reminder_time <= now < reminder_time + timedelta(minutes=1) and subject not in sent_notifications_today:
                        send_notification(subject)
                        sent_notifications_today.add(subject)
            
            time.sleep(60)
        
        except KeyboardInterrupt:
            print("\nScript stopped by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Restarting in 60 seconds...")
            time.sleep(60)

if __name__ == "__main__":
    main()
