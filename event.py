from datetime import datetime, timedelta


class Event:
    """
    Базовый класс для всех мероприятий
    """

    def __init__(self, start: datetime = None, end: datetime = None, movable: bool = True):
        self._start = start
        self._end = end
        self._movable = movable

    @property
    def start(self) -> datetime:
        return self._start

    @start.setter
    def start(self, value: datetime):
        if self.end is None or value < self.end:
            self._start = value
        else:
            raise ValueError(f"Start date ({value}) must be less then the end date ({self.end})")

    @property
    def end(self) -> datetime:
        return self._end

    @end.setter
    def end(self, value: datetime):
        if self.start is None or self.start < value:
            self._end = value
        else:
            raise ValueError(f"End date ({value}) must be greater the start date ({self.start})")

    @property
    def movable(self) -> bool:
        return self._movable

    @movable.setter
    def movable(self, value: bool):
        self._movable = value

    @property
    def duration(self) -> timedelta:
        return self.end - self.start

    def __repr__(self) -> str:
        return f"start = {self.start}, end = {self.end}, movable = {self.movable}"
