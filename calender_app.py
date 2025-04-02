import tkinter as tk
from tkinter import simpledialog, messagebox
import calendar
from datetime import datetime, timedelta
import time
import threading

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App with Reminders")
        self.root.geometry("600x500")
        
        self.current_month = datetime.now().month
        self.current_year = datetime.now().year

        self.events = {}  # Store events as {date: [event details]}
        self.reminders = []  # Store reminders as (event_time, reminder_time)

        self.create_ui()

    def create_ui(self):
        self.month_label = tk.Label(self.root, text=self.get_month_name(self.current_month), font=("Arial", 16))
        self.month_label.grid(row=0, column=1)

        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.grid(row=1, column=0, columnspan=3)

        self.create_calendar()

        self.prev_button = tk.Button(self.root, text="<", command=self.prev_month)
        self.prev_button.grid(row=0, column=0)

        self.next_button = tk.Button(self.root, text=">", command=self.next_month)
        self.next_button.grid(row=0, column=2)

    def create_calendar(self):
        # Destroy existing widgets
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        # Add the weekday headers (Mon, Tue, Wed, ...)
        weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for col, day in enumerate(weekdays):
            label = tk.Label(self.calendar_frame, text=day, font=("Arial", 10, "bold"))
            label.grid(row=0, column=col)

        # Create the month calendar (days of the month)
        cal = calendar.monthcalendar(self.current_year, self.current_month)
        for row in range(5):
            for col in range(7):
                day = cal[row][col]
                if day == 0:
                    continue
                button = tk.Button(self.calendar_frame, text=str(day), width=5, height=2,
                                   command=lambda day=day: self.view_or_add_event(day))
                button.grid(row=row+1, column=col)

    def view_or_add_event(self, day):
        event_date = datetime(self.current_year, self.current_month, day)
        if event_date in self.events and self.events[event_date]:
            self.view_events(event_date)
        else:
            self.add_event(day)

    def add_event(self, day):
        event_name = simpledialog.askstring("Event", "Enter event name:")
        if event_name:
            event_date = datetime(self.current_year, self.current_month, day)
            reminder_time = simpledialog.askinteger("Reminder", "Enter reminder time in minutes before the event:")
            if reminder_time:
                event_time = event_date
                reminder_time = event_time - timedelta(minutes=reminder_time)
                self.reminders.append((reminder_time, event_name))
                
            if event_date not in self.events:
                self.events[event_date] = []
            self.events[event_date].append({"name": event_name, "reminder_time": reminder_time})

            messagebox.showinfo("Event Added", f"Event '{event_name}' added for {event_date.strftime('%Y-%m-%d')}")

        self.create_calendar()

    def view_events(self, event_date):
        events_list = self.events[event_date]
        event_details = "\n".join([f"{i+1}. {event['name']} (Reminder at {event['reminder_time'].strftime('%H:%M')})"
                                  for i, event in enumerate(events_list)])

        def edit_event(event_index):
            event = events_list[event_index]
            new_name = simpledialog.askstring("Edit Event", f"Edit event name for {event['name']}:")
            if new_name:
                event['name'] = new_name
            new_reminder_time = simpledialog.askinteger("Edit Reminder", "Enter new reminder time (minutes before event):")
            if new_reminder_time:
                event['reminder_time'] = event_date - timedelta(minutes=new_reminder_time)

            messagebox.showinfo("Event Edited", f"Event '{new_name}' updated!")
            self.create_calendar()

        def delete_event(event_index):
            del events_list[event_index]
            messagebox.showinfo("Event Deleted", "Event has been deleted.")
            self.create_calendar()

        # Create a new window to show events and allow editing
        view_window = tk.Toplevel(self.root)
        view_window.title(f"Events for {event_date.strftime('%Y-%m-%d')}")
        events_label = tk.Label(view_window, text=f"Events on {event_date.strftime('%Y-%m-%d')}:\n\n{event_details}")
        events_label.pack()

        for i, event in enumerate(events_list):
            edit_button = tk.Button(view_window, text=f"Edit Event {i+1}", command=lambda i=i: edit_event(i))
            edit_button.pack()
            delete_button = tk.Button(view_window, text=f"Delete Event {i+1}", command=lambda i=i: delete_event(i))
            delete_button.pack()

    def prev_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.update_calendar()

    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.update_calendar()

    def update_calendar(self):
        self.month_label.config(text=self.get_month_name(self.current_month))
        self.create_calendar()

    def get_month_name(self, month):
        return calendar.month_name[month]

    def start_reminder_thread(self):
        threading.Thread(target=self.check_reminders, daemon=True).start()

    def check_reminders(self):
        while True:
            current_time = datetime.now()
            for reminder_time, event_name in self.reminders:
                if current_time >= reminder_time:
                    messagebox.showinfo("Reminder", f"Reminder for event: {event_name}")
                    self.reminders.remove((reminder_time, event_name))
            time.sleep(60)  # Check every minute

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    app.start_reminder_thread()  # Start the reminder checking in the background
    root.mainloop()
