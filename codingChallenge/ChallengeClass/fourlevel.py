class TrackedObject:
    def __init__(self, id):
        self.id = id
        self.counted = False

    def check_pass(self):
        if not self.counted:
            self.counted = True
            print(f"Object {self.id} counted")
        else:
            print(f"Object {self.id} already counted")

obj = TrackedObject(123)
obj.check_pass()
obj.check_pass()
