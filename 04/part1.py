#!/usr/bin/python3

import re
import sys
from enum import Enum
from datetime import datetime, timedelta
from pprint import pprint


class EventType(Enum):
    SHIFT = 0
    WAKEUP = 1
    GOTOSLEEP = 2


class Event:
    LINE_REGEX = re.compile(r'^\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2})\]\s(?P<message>.+)$')
    SHIFT_REGEX = re.compile(r'^Guard #(?P<ID>\d+) begins shift$')

    def __init__(self, timestamp, event, _id=None):
        self.timestamp = timestamp
        self.event = event
        self._id = _id

    @classmethod
    def from_line(cls, line):
        m = cls.LINE_REGEX.search(line)
        if not m:
            raise RuntimeError(f'invalid data: {line}')

        timestamp = datetime.strptime(m.group('timestamp'), '%Y-%m-%d %H:%M')
        msg = m.group('message')

        _id = None
        m = cls.SHIFT_REGEX.search(msg)
        if m:
            event = EventType.SHIFT
            _id = int(m.group('ID'))
        elif msg == 'wakes up':
            event = EventType.WAKEUP
        elif msg == 'falls asleep':
            event = EventType.GOTOSLEEP
        else:
            raise RuntimeError(f'invalid data: {msg}')

        return cls(timestamp, event, _id)

    def __repr__(self):
        return f'{self.timestamp} - #{self._id}: {self.event.name}'


class Shift:

    def __init__(self, _id, events):
        self._id = _id
        self.asleep = self._convert_to_asleep_matrix(events)

    @staticmethod
    def _convert_to_asleep_matrix(events):
        matrix = []

        asleep_at = None
        for event in events:
            if event.event == EventType.GOTOSLEEP:
                asleep_at = event.timestamp
            elif event.event == EventType.WAKEUP:
                matrix.append((asleep_at, event.timestamp))

        return matrix

    def __add__(self, other):
        if self._id != other._id:
            raise RuntimeError('geht ned!')

        self.asleep += other.asleep
        return self

    @property
    def time_asleep(self):
        _sum = timedelta()
        for e in self.asleep:
            _sum += (e[1] - e[0])
        return _sum

    @property
    def laziest_minute(self):
        res = [0 for i in range(0, 60)]
        for e in self.asleep:
            a = e[0].minute
            b = e[1].minute

            if b < a:
                a, b = b, a

            for i in range(a, b):
                res[i] += 1

        return res.index(max(res))

    def __repr__(self):
        return f'#{self._id}: asleept for {self.time_asleep}'


def main():
    events = []
    shifts = {}

    # Parse input data
    for line in sys.stdin:
        event = Event.from_line(line)
        events.append(event)

    events = sorted(events, key=lambda x: x.timestamp)

    # Fill in IDs in the events and parse shifts.
    last_shift = 0
    last_id = None
    cur_id = None
    for i, event in enumerate(events):
        # New guard.
        if event.event == EventType.SHIFT:
            cur_id = event._id
            if last_id:
                if last_id in shifts:
                    shifts[last_id] += Shift(last_id, events[last_shift:i])
                else:
                    shifts[last_id] = Shift(last_id, events[last_shift:i])
            last_shift = i
            last_id = cur_id
        if event._id is None:
            event._id = cur_id

    m = max(shifts, key=lambda x: shifts[x].time_asleep)
    print(shifts[m]._id, shifts[m].laziest_minute)
    print(shifts[m]._id * shifts[m].laziest_minute)

    # part 2


    pprint(shifts)


if __name__ == '__main__':
    main()
