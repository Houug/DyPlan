from datetime import datetime

import event

if __name__ == "__main__":
    a = event.Event()
    b = event.Event()
    a.start = datetime(year=2022, month=5, day=1)
    a.end = datetime(year=2022, month=6, day=1)

    b.start = datetime(year=2022, month=5, day=1)
    b.end = datetime(year=2022, month=7, day=1)
    print(b.duration)
