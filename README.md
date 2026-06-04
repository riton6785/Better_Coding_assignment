# CLI Alarm Clock

A lightweight command-line alarm clock written in Python. Set one-off or recurring daily alarms and run a background scheduler that fires them at the right time.

## Requirements

- Python 3.10 or later
- No third-party dependencies — standard library only

## Usage

```bash
# Add a one-off alarm
python3 main.py add --datetime "2025-12-31 23:59" --label "New Year"

# Add a recurring daily alarm
python3 main.py add --datetime "2025-06-05 07:00" --label "Morning standup" --recurring

# List all alarms
python3 main.py list

# Remove an alarm by ID
python3 main.py remove --id 1

# Start the scheduler (keep this running in a terminal)
python3 main.py run
```

**Datetime format:** `YYYY-MM-DD HH:MM`

When an alarm fires, the scheduler prints a notification and removes it from the store. Recurring alarms are automatically rescheduled 24 hours forward.

## Project Structure

```
├── main.py           # CLI entry point (argparse subcommands)
├── alarm.py          # Alarm dataclass
├── alarm_manager.py  # Persistence — load/save/add/remove alarms
├── scheduler.py      # Background loop that checks and fires alarms
└── alarms.json       # Auto-created alarm store
```

## Design Notes

- **JSON file storage** — no database setup required; easy to inspect and sufficient for personal use.
- **30-second poll interval** — simple and robust; handles new alarms added while the scheduler is already running.
- **Separate `AlarmManager` and `Scheduler`** — keeps persistence and timing logic independently testable.

## Possible Extensions

- Audio alert via `playsound` or system `beep`
- Timezone support using `zoneinfo`
- Snooze subcommand
- Natural language time parsing via `dateparser`
