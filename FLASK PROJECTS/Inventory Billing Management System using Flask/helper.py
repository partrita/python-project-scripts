import random
import string


def random_id(N):
    res = ''.join(random.choices(string.ascii_lowercase +
                             string.ascii_uppercase, k=N))
    return res

def handle_catch(caller, on_exception):
    try:
         return caller()
    except Exception:  # noqa: BLE001
         return on_exception