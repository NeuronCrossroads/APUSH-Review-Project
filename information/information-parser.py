import json
import math
from typing import List

events_lines = []
with open("events.txt","r") as f:
    events_lines = f.readlines()

events_string = "".join(events_lines)
events_raw = events_string.split("\n\n")

class Event:
    name: str
    time_sort: int
    time: str
    themes: List[str]
    coord: str
    cfw: str
    amsco: str
    overview: str
    causes: List[str]
    effects: List[str]
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    def to_string(self):
        return str([
            self.name,
            self.time_sort,
            self.time,
            self.themes,
            self.coord,
            self.cfw,
            self.amsco,
            self.overview,
            self.causes,
            self.effects
        ])

events: List[Event] = []
for event_raw in events_raw:
    events.append(Event())
    event_split = event_raw.split("\n")
    events[-1].name = event_split[0]
    events[-1].time = event_split[1]
    if "," in events[-1].time:
        events[-1].time_sort = int(events[-1].time.split(",")[0])
    elif "-" in events[-1].time:
        events[-1].time_sort = math.floor((int(events[-1].time.split("-"))+int(events[-1].time.split("-")))/2)
    elif "s" in events[-1].time:
        events[-1].time_sort = int(events[-1].time[0:-1])
    else:
        events[-1].time_sort = int(events[-1].time)
    events[-1].themes = event_split[2].split("|")
    events[-1].coord = event_split[3]
    events[-1].cfw = event_split[4]
    events[-1].amsco = event_split[5]
    events[-1].overview = event_split[6].replace("{{","<b style=\"color: purple;\">").replace("}}","</b>")
    events[-1].causes = event_split[7].split("|")
    events[-1].effects = event_split[8].split("|")

events_out = []
for event in events:
    events_out.append(event.toJSON())
events_data_finished = f"\"events\":[{','.join(events_out)}],"


trend_lines = []
with open("trends.txt","r") as f:
    trend_lines = f.readlines()

trends_string = "".join(trend_lines)
trends_raw = trends_string.split("\n\n")

class Trend:
    name: str
    time: str
    time_sort: int
    overview: str
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

trends: List[Trend] = []
for trend_raw in trends_raw:
    trend_split = trend_raw.split("\n")
    t = Trend()
    t.name = trend_split[0]
    t.time = trend_split[1]
    if "," in t.time:
        t.time_sort = int(t.time.split(",")[0])
    elif "-" in t.time:
        t.time_sort = math.floor((int(t.time.split("-")[0])+int(t.time.split("-")[1]))/2)
    elif "s" in t.time:
        t.time_sort = int(t.time[0:-1])
    else:
        t.time_sort = int(t.time)
    t.overview = trend_split[2]
    trends.append(t)

trends_out = []
for trend in trends:
    trends_out.append(trend.toJSON())
trends_data_finished = f"\"trends\":[{','.join(trends_out)}]"

out_json = "{"+events_data_finished+trends_data_finished+"}"
with open("information.json","w") as f:
    f.write(out_json)