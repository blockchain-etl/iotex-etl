import base64

def base64_string(val):
    if val is None:
        return val
    return base64.b64encode(val).decode('utf-8')