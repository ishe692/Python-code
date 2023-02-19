import threading

class TimeoutException(Exception):
    pass

def input_with_timeout(prompt, timeout):
    # Define a function that runs the input function in a separate thread
    def input_thread():
        nonlocal user_input
        user_input = input(prompt)

    # Create a Timer that will raise a TimeoutException if it expires
    timer = threading.Timer(timeout, lambda: setattr(user_input, 'value', TimeoutException()))

    # Start the Timer and the input thread
    user_input = threading.local()
    timer.start()
    input_thread = threading.Thread(target=input_thread)
    input_thread.start()

    # Wait for the input thread to complete or the Timer to expire
    input_thread.join()
    timer.cancel()

    # Return the user input, or raise a TimeoutException if the Timer expired
    if isinstance(user_input.value, TimeoutException):
        print("Timeout expired.")
        return None
    else:
        return user_input.value

# Call the input_with_timeout function with a timeout of 5 seconds
user_input = input_with_timeout("Enter some input: ", 5)
if user_input is not None:
    print(f"You entered: {user_input}")
