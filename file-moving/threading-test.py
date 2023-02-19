import threading
import keyboard
import time


def get_input():
    try:
        # Wait for user input with a timeout of 5 seconds
        user_input = input("Enter some input: ")
    except:
        # If the input function is interrupted, exit the program
        exit(0)
    # Do something with the user input
    print("You entered:", user_input)

# Start a separate thread to wait for user input
input_thread = threading.Thread(target=get_input)
input_thread.start()

def on_esc_pressed():
    print('esc pressed')
    input_thread.join(timeout=1)
    # If the input thread is still running after the timeout, interrupt it and exit the program
    if input_thread.is_alive():
        input_thread.cancel()
        exit(0)

def esc_listener():
    keyboard.add_hotkey('esc', on_esc_pressed)
    keyboard.wait()

listener_thread = threading.Thread(target=esc_listener, daemon=True)
listener_thread.start()

# Continue with the main program
time.sleep(5)
print("Program continues...")
x = input("what else?")
