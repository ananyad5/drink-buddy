# drink-buddy
This is a python program that reminds you to drink water every 40 mins! Gotta be hydrated!

# Features
- Sends a reminder every 40 minutes (customizable).
- Uses the plyer library for cross-platform notifications (Windows, macOS, Linux).
- Lightweight, simple, and easy to use.

# Setup and Usage

1. Install some requirements:
   
   Install the required Python library using pip:
   
   ```` pip install plyer ````

3. Clone or download the repository:
   
   ```` git clone git@github.com:ananyad5/drink-buddy.git ````
   ```` cd drink-buddy ````
4. Run the program:
   
   ```` python3 main.py ````
6. Customize the intervals (if needed):
   
    Edit the interval and reminders variables in main.py: 
    1. interval: Time between reminders in seconds (default: 40 * 60 for 40 minutes).
    2. reminders: Total number of reminders (default: 16).

8. Troubleshooting:
   
   macOS: Ensure your terminal/IDE has permission to send notifications. Go to your notification settings and enable notifications for your IDE.


