import time
import threading

def stopwatch():
    print("Stopwatch started. Press Enter to stop.")
    start_time = time.time()
    input()
    elapsed = time.time() - start_time
    print(f"Elapsed time: {elapsed:.2f} seconds")

def timer(seconds):
    print(f"Timer started for {seconds} seconds.")
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = f'{mins:02d}:{secs:02d}'
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!            ")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Stopwatch")
        print("2. Timer")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            stopwatch()
        elif choice == '2':
            try:
                t = int(input("Enter time in seconds: "))
                timer(t)
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            
            print("Invalid choice. Try again.")
            

if __name__ == "__main__":
    main()



