from rat_journal import Journal, Measure, TracePoint

def rats():
    return set(map(lambda(m): m.rat, Journal.measures))


def filter_rat_measures(rat_id):
    return filter(lambda(m): m.rat == rat_id, Journal.measures)

def filter_rat_findings(rat_id):
    return filter(lambda(m): m.rat == rat_id, Journal.cookie_findings)

def search_time(measure):
    for tp in measure.trace:
        if tp.room != "T" and measure.room_contents[int(tp.room) - 1] == 'c':
            return tp.time

