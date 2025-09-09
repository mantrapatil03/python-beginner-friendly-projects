import tkinter as tk
from tkinter import messagebox
import datetime

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Alarm Clock")
        self.root.geometry("350x180")
        self.root.resizable(False, False)

        tk.Label(root, text="Set Alarm Time (HH:MM:SS)", font=("Arial", 12)).pack(pady=10)

        self.time_entry = tk.Entry(root, width=20, font=("Arial", 14), justify='center')
        self.time_entry.pack()
        self.time_entry.insert(0, "00:00:00")

        self.set_button = tk.Button(root, text="Set Alarm", font=("Arial", 12), command=self.set_alarm)
        self.set_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Alarm", font=("Arial", 12), command=self.stop_alarm, state=tk.DISABLED)
        self.stop_button.pack()

        self.status_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
        self.status_label.pack(pady=10)

        self.alarm_time = None
        self.alarm_set = False

    def set_alarm(self):
        alarm_time_str = self.time_entry.get()
        try:
            valid_time = datetime.datetime.strptime(alarm_time_str, "%H:%M:%S").time()
            self.alarm_time = valid_time
            self.status_label.config(text=f"Alarm set for {self.alarm_time}")
            self.alarm_set = True

            self.time_entry.config(state=tk.DISABLED)
            self.set_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

            # Start checking alarm using after()
            self.check_alarm()

        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter time in HH:MM:SS format")

    def check_alarm(self):
        if not self.alarm_set:
            return  # Alarm stopped, do nothing

        now = datetime.datetime.now().time().replace(microsecond=0)
        if now == self.alarm_time:
            self.status_label.config(text="Alarm ringing!")
            messagebox.showinfo("Alarm", "Time's up!")
            self.stop_alarm()
        else:
            # Check again after 1 second (1000 ms)
            self.root.after(1000, self.check_alarm)

    def stop_alarm(self):
        self.alarm_set = False
        self.status_label.config(text="Alarm stopped.")
        self.time_entry.config(state=tk.NORMAL)
        self.set_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
