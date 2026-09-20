import tracker

def main():
    mgr = tracker.Tracker()

    while True:
        print("\n=================================")
        print("    DEADLINE MANAGER (CLI)")
        print("=================================")
        print("1. Add Assignment")
        print("2. View Pending (Active Tab)")
        print("3. View Completed (Archive Tab)")
        print("4. Mark Assignment as Done")
        print("5. Update Assignment (Days/Priority)")
        print("6. Delete Assignment")
        print("7. Exit")

        ch = input("Select option (1-7): ")

        if ch == "1":
            mgr.add()
        elif ch == "2":
            mgr.view(False)
        elif ch == "3":
            mgr.view(True)
        elif ch == "4":
            mgr.done()
        elif ch == "5":
            mgr.edit()
        elif ch == "6":
            mgr.delete()
        elif ch == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option, pick 1 to 7.")

main()