from services.alert_config import TumblingWindowConfig, SlidingWindowConfig
from services.dispatch_service import ConsoleDispatch, EmailDispatch
from services.monitoring_service import MonitoringService


def main():
    alert_config_1 = TumblingWindowConfig(count=10, window_size_secs=3600)
    alert_config_2 = SlidingWindowConfig(count=5, window_size_secs=60)
    dispatch_strategies = [ConsoleDispatch(), EmailDispatch()]

    # Simulate events
    monitoring_service_1 = MonitoringService("X", "PAYMENT_EXCEPTION", alert_config_1, dispatch_strategies)
    monitoring_service_2 = MonitoringService("X", "USERSERVICE_EXCEPTION", alert_config_2, dispatch_strategies[0:1])
    for _ in range(15):
        monitoring_service_1.track_event()
        monitoring_service_2.track_event()


if __name__ == "__main__":
    main()
