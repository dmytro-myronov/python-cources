
class EventType:
    DEATH = "death"
    JAIL = "jail"
    LEVEL_UP = "level_up"
    HEALTH_DOWNGRADE = "health_downgrade"


class GameEventException(Exception):
    def __init__(self, event_type: EventType, event_data:dict[str]):
        self.event_type = event_type
        self.event_data = event_data


    def __str__(self):
        return f"{self.event_type} {self.event_data}"



game_event  = input("Go to castle. Click 1\n"
                    "Go to whorehouse. Click 2\n"
                    "Go to forest. Click 3\n")

try:
    if game_event == "1":
        print("You are in castle!")
        raise GameEventException(EventType.DEATH, dict(reason="dragon killed you"))
    elif game_event == "2":
        print("You are in whorehouse!")
        raise GameEventException(EventType.HEALTH_DOWNGRADE, dict(reason="you got some sick and lost one life"))
    elif game_event == "3":
        print("You are in the forest!")
        raise GameEventException(EventType.LEVEL_UP, dict(reason="you found elfs camp.They trainer your sword skills"))
except GameEventException as e:
    print(e)

except MemoryError:
    print("not enough memory")
except Exception as e:
    print("something went wrong")

