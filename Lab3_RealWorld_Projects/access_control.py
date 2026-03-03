def audit_log(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

def compute_access_level(control_num, artist):
    return control_num * 3 + len(artist)

@audit_log
def validate_access(level, threshold):
    if level >= threshold:
        return "ACCESS GRANTED"
    return "ACCESS DENIED"