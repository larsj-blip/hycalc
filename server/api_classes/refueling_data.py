from dataclasses import dataclass
import json


@dataclass
class RefuelingData:
    type: str
    number_of_refuels: int
    percent_left_in_tank: int
    minutes_spent_refueling: int

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {
            "type": self.type,
            "number_of_refuels": self.number_of_refuels,
            "percent_left_in_tank": self.percent_left_in_tank,
            "minutes_spent_refueling": self.minutes_spent_refueling

        }
