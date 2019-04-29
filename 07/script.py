#!/usr/bin/python3

import re
import sys


class Node:
    LINEREGEX = re.compile(r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.')

    def __init__(self, task, deps=[]):
        self.task = task
        self.deps = deps
        self.finished = False

    @classmethod
    def from_line(cls, line):
        m = cls.LINEREGEX.search(line)
        if m:
            return cls(m.group(2), [m.group(1)])
        raise RuntimeError('data is garbage')

    def merge(self, node):
        if self.task != node.task:
            raise KeyError

        for dep in node.deps:
            if dep not in self.deps:
                self.deps.append(dep)
        self.deps.sort()

    def __repr__(self):
        return f'TASK {self.task}; DEPS: {self.deps}; FINISHED: {self.finished}'


class Graph:

    def __init__(self, data):
        self.data = data

    @classmethod
    def from_lines(cls, lines):
        nodes = {}
        for line in lines:
            n = Node.from_line(line)
            if n.task in nodes:
                nodes[n.task].merge(n)
            else:
                nodes[n.task] = n

        # Add missed tasks because they have no dependency.
        for key in list(nodes.keys()):
            for dep in nodes[key].deps:
                n = Node(dep)
                if n.task not in nodes:
                    nodes[n.task] = n

        return cls(nodes)

    def task_can_be_completed(self, key):
        task = self.data[key]
        if len(task.deps) == 0:
            return True

        for dep in task.deps:
            if not self.data[dep].finished:
                return False

        return True

    def get_next_tasks(self):
        for task in self.data:
            if self.data[task].finished is False and self.task_can_be_completed(task):
                if task not in self.next_tasks:
                    self.next_tasks.append(task)
        self.next_tasks.sort(reverse=True)

    def traverse1(self):
        finished = []
        self.next_tasks = []

        while True:
            self.get_next_tasks()

            try:
                task = self.next_tasks.pop()
            except IndexError:
                break

            self.data[task].finished = True
            finished.append(task)

        print(''.join(finished))

    def __repr__(self):
        r = []
        for task in self.data:
            r.append(str(self.data[task]))
        return '\n'.join(r)


graph = Graph.from_lines(sys.stdin.readlines())
graph.traverse1()
