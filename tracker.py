import storage

class Tracker:
    def __init__(self):
        self.db = storage.Store()
        self.prios = ["HIGH", "MED", "LOW"]

    def add(self):
        c = input("Course: ").upper()
        t = input("Title: ")
        d = input("Days: ")
        p = input("Priority (HIGH/MED/LOW): ").upper()
        if not d.isdigit() or p not in self.prios:
            print("Invalid input.")
            return
        arr = self.db.load()
        arr.append(storage.Task(c, t, d, p, False))
        self.db.save(arr)
        print("Saved.")

    def view(self, is_done):
        arr = self.db.load()
        box = []
        for x in arr:
            if x.done == is_done:
                box.append(x)

        if len(box) == 0:
            print("\nList empty.")
            return

        print("\n" + "=" * 60)
        print(f"{'No':<5} {'Course':<10} {'Days':<16} {'Prio':<8} {'Title'}")
        print("=" * 60)

        i = 1
        for x in box:
            if x.done:
                d_msg = "Completed"
            else:
                d_msg = str(x.d) + " days"
                if int(x.d) <= 2:
                    d_msg = d_msg + " [URGENT!]"
            print(f"{i:<5} {x.c:<10} {d_msg:<16} {x.p:<8} {x.t}")
            i = i + 1
        print("=" * 60)

    def done(self):
        arr = self.db.load()
        name = input("Title done: ").lower()
        for x in arr:
            if x.t.lower() == name:
                x.done = True
                self.db.save(arr)
                print("Done.")
                return
        print("Not found.")

    def edit(self):
        arr = self.db.load()
        name = input("Title to edit: ").lower()
        for x in arr:
            if x.t.lower() == name:
                nd = input("New days (enter to skip): ")
                if nd != "":
                    if not nd.isdigit():
                        print("Invalid days. Must be a number.")
                        return
                    x.d = int(nd)

                np = input("New prio HIGH/MED/LOW (enter to skip): ").upper()
                if np != "":
                    if np not in self.prios:
                        print("Invalid priority. Choose HIGH, MED, or LOW.")
                        return
                    x.p = np

                self.db.save(arr)
                print("Updated.")
                return
        print("Not found.")

    def delete(self):
        arr = self.db.load()
        name = input("Title to delete: ").lower()
        for i in range(len(arr)):
            if arr[i].t.lower() == name:
                arr.pop(i)
                self.db.save(arr)
                print("Deleted.")
                return
        print("Not found.")
