from services.alert_config import AlertConfig
from services.dispatch_service import DispatchStrategy, ConsoleDispatch


class MonitoringService:
    def __init__(self, client: str, event_type: str, alert_config: AlertConfig, dispatch_strategies: list[DispatchStrategy]):
        self.client = client
        self.event_type = event_type
        self.alert_config = alert_config
        self.dispatch_strategies = dispatch_strategies

    def track_event(self) -> None:
        print(f"[INFO] MonitoringService: Client {self.client} {self.event_type} {self.alert_config.__class__.__name__} starts")
        self.alert_config.event_count += 1
        if self.alert_config.check_and_reset(self.alert_config.event_count):
            self.dispatch_alert()

        print(f"[INFO] MonitoringService: Client {self.client} {self.event_type} {self.alert_config.__class__.__name__} ends")

    def dispatch_alert(self) -> None:
        alert_message = self.get_alert_message()
        for strategy in self.dispatch_strategies:
            print(f"[INFO] AlertingService: Dispatching to {strategy.__class__.__name__}")
            strategy.dispatch(alert_message)

    def get_alert_message(self) -> str:
        for strategy in self.dispatch_strategies:
            if isinstance(strategy, ConsoleDispatch):
                return strategy.message
        return "Alert triggered!"