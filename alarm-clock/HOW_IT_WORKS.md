# ⏰ How the Alarm Clock Works

## 1️⃣ User Interface Setup

When you run the program, a small window opens.

It shows:

📝 A label telling you to enter the alarm time in HH:MM:SS format.

⌨️ A text box where you type the time (default is 00:00:00).

▶️ A Set Alarm button to start the alarm.

⏹️ A Stop Alarm button (initially disabled).

📢 A status label that shows messages like “Alarm set for ...” or “Alarm ringing!”.

## 2️⃣ Setting the Alarm

⌨️ Type a time like 14:30:00 (2:30 PM) in the text box.

🖱️ Click Set Alarm.

👉 The program then checks:

❌ If the time format is wrong → shows an error popup.

✅ If the time format is valid:

💾 Saves the alarm time.

🔒 Disables the text box and Set Alarm button (so you can’t change while running).

🔓 Enables the Stop Alarm button.

🟢 Updates the status label → “Alarm set for ...”.

⏱️ Starts checking the current time every second.

## 3️⃣ Checking the Alarm

The program uses a function called check_alarm that runs every second.

⏲️ Each second it:

Gets the current time (hours, minutes, seconds).

Compares it with the alarm time you set.

👉 If the times match:

📢 Status label → “Alarm ringing!”

🔔 Popup → “Time’s up!”

✅ Alarm automatically stops (re-enables input & buttons).

👉 If the times don’t match yet:

🔄 Waits 1 second, checks again.

## 4️⃣ Stopping the Alarm

You can also stop the alarm manually anytime by clicking Stop Alarm.

This will:

🛑 Stop checking the time.

🟡 Update the status label → “Alarm stopped.”

🔓 Re-enable the text box & Set Alarm button.

🔒 Disable the Stop Alarm button again.

## 📝 Summary

⏰ Program waits for you to set a time.

🔄 Keeps checking the clock every second.

🔔 Rings exactly at your set time.

🛑 Can be stopped manually or it stops automatically after ringing.
