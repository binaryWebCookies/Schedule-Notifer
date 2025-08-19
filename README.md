# Schedule Notifer
An app that automatically sends you a notification 15 minutes before your next subject starts. No need to constantly check your phone or laptop — you’ll get a timely reminder straight to your notifications so you’re always prepared. Only works if your computer is on, sleep mode also counts as on. 

## 🌟 Features
  * Customisable Schedule: Easily update your classes and times in the Python script.
  * Dual Notifications: Sends push notifications to your phone and desktop pop-up notifications to your PC.
  * Persistent: Can be configured to run automatically on your computer's startup.
  * Reliable: Uses the stable `requests` library to communicate directly with the Pushover API.

## 🚀 Getting Started
### Prerequisites
You will need the following to run this script:

Python 3: The script is written in Python 3. If you don't have it, you can download it from [python.org](https://www.python.org/downloads/).
Pushover Account: A free Pushover account is required to send notifications to your phone.
  * Create an account on [pushover.net](https://pushover.net/).
  * Install the Pushover app on your mobile device.
  * Create a new application in your Pushover dashboard to get an "API Token".
  * Find your personal "User Key" in your Pushover dashboard.
  * Required Python Libraries: You need to install the `requests` and `plyer` libraries.

### Installation
1.  Clone the Repository:

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

    (Replace `your-username` and `your-repository-name` with your actual GitHub details.)

2.  Install Dependencies: Open your terminal or command prompt and run the following command to install the required libraries:

    ```bash
    pip install requests plyer
    ```

3.  Update Credentials: Open the `schedule_notifier.py` file and replace the placeholder keys with your actual "API Token" and "User Key".

    ```python
    # --- Pushover Credentials ---
    user_key = 'YOUR_USER_KEY_HERE'
    api_token = 'YOUR_API_TOKEN_HERE'
    ```

4.  Customize Your Schedule: Modify the `schedule` dictionary to match your class timetable. Times should be in 24-hour format.

    ```python
    schedule = {
        'Monday': {
            'AP Research': '08:00',
            'Maths': '09:25',
            # Add or remove classes here
        },
        # ... and so on for other days
    }
    ```

## ▶️ How to Run

To run the script, open your terminal or command prompt, navigate to the directory where you saved the file, and run the following command:

```bash
python schedule_notifier.py
```

The script will start running and print its status to the terminal. You can close the terminal to stop the script.

### Run on Startup

To have the script run automatically every time your computer starts, you can use your operating system's built-in tools:

  * Windows: Use the "Task Scheduler" to create a basic task.
  * macOS: Use "Login Items" in System Settings.
  * Linux: Use a "cron job" with `@reboot`.

## 🛠️ Troubleshooting

  * "Error sending notification": Double-check your `user_key` and `api_token` for typos. They must be an exact match from the Pushover website.
  * Notification not appearing on desktop: Ensure you have a working graphical environment. Some minimalist Linux setups may not support desktop notifications.
  * "ModuleNotFoundError": You haven't installed all the required libraries. Run `pip install requests plyer` again to ensure they are installed correctly.

## 📜 License

This project is open-source.
