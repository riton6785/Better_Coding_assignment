import time
from datetime import datetime, timedelta
from alarm import Alarm


class Scheduler:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
        print("Alarm scheduler started...")

        while True:
            alarms = self.manager.load_alarms()

            now = datetime.now()

            updated_alarms = []

            for alarm in alarms:
                if alarm.trigger_at <= now:
                    self.trigger_alarm(alarm)

                    if alarm.recurring:
                        alarm.trigger_at += timedelta(
                            days=1
                        )

                        updated_alarms.append(
                            alarm
                        )
                else:
                    updated_alarms.append(
                        alarm
                    )

            self.manager.save_alarms(
                updated_alarms
            )

            time.sleep(30)

    @staticmethod
    def trigger_alarm(alarm: Alarm):
        print("\n" + "=" * 50)
        print("ALARM TRIGGERED")
        print(
            f"Time : "
            f"{alarm.trigger_at}"
        )
        print(
            f"Label: "
            f"{alarm.label}"
        )
        print("=" * 50 + "\n")
