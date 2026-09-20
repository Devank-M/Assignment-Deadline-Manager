import os

class Task:
    def __init__(self, c, t, d, p, done=False):
        self.c = c
        self.t = t
        self.d = int(d)
        self.p = p
        self.done = done

    def to_txt(self):
        return self.c + "|" + self.t + "|" + str(self.d) + "|" + self.p + "|" + str(self.done) + "\n"

class Store:
    def __init__(self, fn="assignments.txt"):
        self.fn = fn

    def load(self):
        if not os.path.exists(self.fn):
            return []
        arr = []
        f = open(self.fn, "r")
        for line in f.readlines():
            w = line.replace("\n", "").split("|")
            if len(w) == 5:
                arr.append(Task(w[0], w[1], w[2], w[3], w[4] == "True"))
        f.close()
        return arr

    def save(self, arr):
        f = open(self.fn, "w")
        for x in arr:
            f.write(x.to_txt())
        f.close()