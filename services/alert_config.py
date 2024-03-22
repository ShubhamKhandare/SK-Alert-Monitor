from abc import abstractmethod, ABC
from datetime import datetime


class AlertConfig(ABC):
    @abstractmethod
    def check_and_reset(self, event_count: int) -> bool:
        pass


class SimpleCountConfig(AlertConfig):
    def __init__(self, count: int):
        self.count = count
        self.triggered = False

    def check_and_reset(self, event_count: int) -> bool:
        if event_count >= self.count:
            self.triggered = True
            return True
        return False


class TimeWindowConfig(AlertConfig, ABC):
    def __init__(self, count: int, window_size_secs: int):
        self.count = count
        self.window_size_secs = window_size_secs
        self.event_count = 0
        self.window_start = None

    @abstractmethod
    def update_window(self) -> None:
        pass


class TumblingWindowConfig(TimeWindowConfig):
    def update_window(self) -> None:
        if not self.window_start:
            self.window_start = datetime.now()
        elif (datetime.now() - self.window_start).total_seconds() > self.window_size_secs:
            self.window_start = datetime.now()
            self.event_count = 0

    def check_and_reset(self, event_count: int) -> bool:
        self.update_window()
        if event_count >= self.count:
            return True
        return False


class SlidingWindowConfig(TimeWindowConfig):
    def update_window(self) -> None:
        if not self.window_start:
            self.window_start = datetime.now()
        elapsed_time = (datetime.now() - self.window_start).total_seconds()
        if elapsed_time > self.window_size_secs:
            self.window_start = datetime.now()
            self.event_count = 0

    def check_and_reset(self, event_count: int) -> bool:
        self.event_count = max(event_count - self.event_count, 0)
        if event_count >= self.count:
            return True
        return False
