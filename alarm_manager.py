import json
import os
from datetime import datetime

from alarm import Alarm

ALARM_FILE = "alarms.json"


class AlarmManager:
    def __init__(self, file_path=ALARM_FILE):
        self.file_path = file_path

    def load_alarms(self) -> list[Alarm]:
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r") as f:
            data = json.load(f)

        return [
            Alarm.from_dict(item)
            for item in data
        ]

    def save_alarms(
        self,
        alarms: list[Alarm],
    ):
        with open(self.file_path, "w") as f:
            json.dump(
                [
                    alarm.to_dict()
                    for alarm in alarms
                ],
                f,
                indent=4,
            )

    def add_alarm(
        self,
        trigger_at: str,
        label: str,
        recurring: bool = False,
    ):
        try:
            trigger_dt = datetime.strptime(
                trigger_at,
                "%Y-%m-%d %H:%M",
            )
        except ValueError:
            print(
                "Invalid datetime format. "
                "Use: YYYY-MM-DD HH:MM"
            )
            return

        alarms = self.load_alarms()

        next_id = (
            max(
                (
                    alarm.id
                    for alarm in alarms
                ),
                default=0,
            )
            + 1
        )

        alarm = Alarm(
            id=next_id,
            trigger_at=trigger_dt,
            label=label,
            recurring=recurring,
        )

        alarms.append(alarm)

        self.save_alarms(alarms)

        print(
            f"Alarm added with ID {next_id}"
        )

    def list_alarms(self):
        alarms = self.load_alarms()

        if not alarms:
            print("No alarms found.")
            return

        print("\nConfigured Alarms")
        print("-" * 80)

        for alarm in alarms:
            print(
                f"ID: {alarm.id} | "
                f"DateTime: "
                f"{alarm.trigger_at.strftime('%Y-%m-%d %H:%M')} | "
                f"Recurring: {alarm.recurring} | "
                f"Label: {alarm.label}"
            )

    def remove_alarm(
        self,
        alarm_id: int,
    ):
        alarms = self.load_alarms()

        updated = [
            alarm
            for alarm in alarms
            if alarm.id != alarm_id
        ]

        if len(updated) == len(alarms):
            print("Alarm not found.")
            return

        self.save_alarms(updated)

        print(
            f"Alarm {alarm_id} removed."
        )
