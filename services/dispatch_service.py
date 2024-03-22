from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime, timedelta


class AlertType(Enum):
    SIMPLE_COUNT = 1
    TUMBLING_WINDOW = 2
    SLIDING_WINDOW = 3


class DispatchStrategy(ABC):
    @abstractmethod
    def dispatch(self, message: str) -> None:
        pass


class ConsoleDispatch(DispatchStrategy):

    def __init__(self, message: str = "Alert triggered!"):
        self.message = message

    def dispatch(self, message: str) -> None:
        print(f"[WARN] Alert: {message}")


class EmailDispatch(DispatchStrategy):

    def dispatch(self, message: str) -> None:
        # TODO Implement logic for sending email
        pass
