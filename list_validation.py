def create_task_list():
    return MyList()


def add_to_list(list_task, task):
    list_task.add(task)


def size_of_list(list_task):
  return list_task.size()


def list_contains(list_task, task):
    return list_task.has_in_list(task)


def upper_task_in_tasklist(list_task):
    return list_task.to_upper()


def main():
    list_task = create_task_list()

    if not isinstance(list_task, MyList):
        print("Error: list_task is not a list")

    add_to_list(list_task, "task1")
    add_to_list(list_task, "task2")

    if size_of_list(list_task) != 2:
        print("Error: list size is not 2")

    if not list_contains(list_task, "task1"):
        print("Error: list does not contain task1")

    if not list_contains(list_task, "task2"):
        print("Error: list does not contain task2")

    task_list_upper = upper_task_in_tasklist(list_task)

    if not list_contains(task_list_upper, "TASK1"):
        print("Error: list does not contain TASK1")

    if not list_contains(task_list_upper, "TASK2"):
        print("Error: list does not contain TASK2")

    if size_of_list(task_list_upper) != 2:
        print("Error: list size is not 2")

class MyList:

    def __init__(self, list=[]):
        self.list = list

    def add(self, task):
        return self.list.append(task)

    def size(self):
        return len(self.list)

    def has_in_list(self, task):
        return task in self.list

    def to_upper(self):
        return MyList([task.upper() for task in self.list])

if __name__ == "__main__":
    main()
