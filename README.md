# Calendar App with Reminders

This is a simple Python-based calendar application with reminders, built using the Tkinter library. It allows users to view, add, edit, and delete events, as well as set reminders for each event. The app displays a monthly calendar and provides functionality to navigate between months and interact with individual dates to manage events.

## Features

- **Monthly Calendar View**: Displays a calendar for the current month, with each date clickable.
- **Add Events**: Users can add events to a specific date, including setting reminder times.
- **View Events**: Displays a list of events for the selected date.
- **Edit Events**: Allows users to modify event details such as the name and reminder time.
- **Delete Events**: Users can delete events.
- **Reminder Notifications**: The app will send reminders at specified times before events occur.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- (Optional) threading module for background reminder checking

## Installation

To run the project, ensure you have Python 3.x installed. Tkinter should be available by default, but if you're using a minimal Python installation, you may need to install it manually.

### Step 1: Clone the Repository


git clone https://github.com/your-username/calendar-app-with-reminders.git
cd calendar-app-with-reminders


### Step 2: Install Dependencies


pip install plyer


### Step 3: Run the Application

To run the application, navigate to the project directory and execute:


python calendar_app.py


The app window should appear, showing the calendar for the current month.

## Usage

### Adding Events

1. Click on any day in the calendar.
2. A dialog box will appear where you can enter the event name and set a reminder time.
3. After filling in the event details, click **Add Event** to save it.

### Viewing and Editing Events

1. Click on any date that has an event.
2. If there are events for that day, a new window will open showing the list of events for that day.
3. You can **edit** or **delete** events from this window.

### Navigating Between Months

- Use the **<** (previous month) and **>** (next month) buttons to navigate between months.

### Reminder Notifications

- If you set a reminder for an event, the app will notify you at the specified time before the event. Reminders will appear as pop-up notifications.

## Code Structure

### Main Application: `calendar_app.py`

The main Python file contains all the logic for the calendar app, including:

- **Calendar creation and display** using Tkinter.
- **Event creation** and **reminder functionality**.
- **Event viewing**, **editing**, and **deleting**.
- **Reminder notification checking** via threading.

### Key Functions:

- `create_ui()`: Initializes the user interface.
- `create_calendar()`: Generates the calendar grid for the selected month.
- `view_or_add_event(day)`: Opens a new event or views events for the selected day.
- `add_event(day)`: Allows the user to add an event on the selected day.
- `view_events(event_date)`: Displays events for a specific date.
- `edit_event(event_index)`: Edits an existing event.
- `delete_event(event_index)`: Deletes an event.

### Reminder Threading:

- The reminder functionality is handled in the background using the `threading` module. It checks every minute whether any event's reminder time has passed and displays a notification if it has.



## Future Improvements

- **Persistent Data Storage**: Add a feature to save events and reminders to a file (JSON or SQLite) so data persists between sessions.
- **Recurring Events**: Add functionality to support recurring events (e.g., daily, weekly, monthly).
- **Event Categories**: Add different categories for events (e.g., personal, work, birthday), with different colors for each category.
- **Dark Mode**: Implement a dark mode option for the interface.

## Contributing

Contributions are welcome! If you have any ideas or improvements for the project, feel free to fork the repository, make your changes, and submit a pull request.

