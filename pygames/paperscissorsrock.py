
import random
import time


# clear terminal
import os
os.system('cls')

import signal

class TimeoutException(Exception):
    pass

def input_with_timeout(prompt, timeout):
    def timeout_handler(signum, frame):
        raise TimeoutException()

    # Set the signal handler to raise a TimeoutException
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)  # Set the alarm to go off after `timeout` seconds

    try:
        # Wait for input from the user
        user_input = input(prompt)
        signal.alarm(0)  # Cancel the alarm
        return user_input
    except TimeoutException:
        print("Timeout expired.")
        return None

# Call the input_with_timeout function with a timeout of 5 seconds
user_input = input_with_timeout("Enter some input: ", 5)
if user_input is not None:
    print(f"You entered: {user_input}")


rps_map = {
    'r':'Rock',
    'p':'Paper',
    's':'Scissors'
}


def main():
    while True:
        print('for paper scissors rock type p, s, r and press enter at the right time')
        time.sleep(2)
        print('Paper....')
        time.sleep(1)
        print('Scissors....')
        time.sleep(1)
        print('Rock!!')
        
        
        # Call the input_with_timeout function with a timeout of 5 seconds
        user_input = input_with_timeout(" ", 5)
        if user_input is not None:
            print(f"You entered: {user_input}")




main()