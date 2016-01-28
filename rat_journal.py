import time
import re

class TracePoint:
    def __repr__(self):
        return "TP<t=" + str(self.time) + ";r=" + self.room + ";e="+ str(self.events) + ">"
    def __str__(self):
        return __repr__()

def parse_trace(tr):
    arr_re = re.compile("->")
    statements = arr_re.split(tr)
    trace = []
    for s in statements:
        time_num_re = re.compile("(\+?)(\d+):(\d+)+\((\w)\)")
        m = time_num_re.match(s)
        time = int(m.group(2)) * 60 + int(m.group(3))
        if m.group(1) == '+':
            time = time + trace[-1].time

        room = m.group(4)

        events_str = s[m.span()[1]:]
        event_re = re.compile("\[(\w+)\]")
        events = event_re.findall(events_str)
        tp = TracePoint()
        tp.time = time
        tp.room = room
        tp.events = events
        trace.append(tp)
    print(tr, "parsed as " ,trace)
    return trace

class Measure:
    def __repr__(self):
        return "M<date=" + time.strftime("%Y-%m-%d", self.date) + ";cage=" + str(self.cage) + ";rat="+ str(self.rat) + ";trace="+ str(self.trace) + ">"
    def __str__(self):
        return self.__repr__()

class Journal:
    cur_date = None
    cur_cage = None
    measures = []

    def add_measure(self, m):
        self.measures.append(m)

    def __init__(self, rat_id):
        self.rat_id = rat_id

    def trace(self, tr):
        m = Measure()
        m.date = self.cur_date
        m.cage = self.cur_cage
        m.rat = self.rat_id
        m.trace = parse_trace(tr)

        self.add_measure(m)

def date(date_str):
    Journal.cur_date = time.strptime(date_str, "%Y-%m-%d")

def cage(n):
    Journal.cur_cage = n

def rat(n):
    return Journal(n)

def print_full_journal():
    print("*** Journal:")
    for m in Journal.measures:
        print(m)
