def monitor(func):
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        # Handle generator results
        if x := list(result) if hasattr(result, '__iter__') else result:
            print("Processing Completed")
            return x
    return wrapper

def signal_shutdown(power):
    if power <= 0:
        return 0
    print(f"Current signal strength: {power}")
    return 1 + signal_shutdown(power - 1)

def play_count_stream(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i ** 2