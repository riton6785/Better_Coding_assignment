from dataclasses import dataclass
from datetime import datetime


@dataclass
class Alarm:
    id: int
    trigger_at: datetime
    label: str
    recurring: bool = False

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "trigger_at": self.trigger_at.isoformat(),
            "label": self.label,
            "recurring": self.recurring,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Alarm":
        return cls(
            id=data["id"],
            trigger_at=datetime.fromisoformat(
                data["trigger_at"]
            ),
            label=data["label"],
            recurring=data.get(
                "recurring",
                False,
            ),
        )
