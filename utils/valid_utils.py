from datetime import datetime
from datetime import timedelta

def seconds_until_end_of_today() -> int:
    time_delta = datetime.combine(
        datetime.now().date() + timedelta(days=1), datetime.strptime("0000", "%H%M").time()
    ) - datetime.now()
    return time_delta.seconds

def len_more_then(target, maxlen: int) -> bool:
    return len(target) > maxlen

a = {"a": 222, "b": 333, "c": 444}

b = "a" in a.keys()
print(b)