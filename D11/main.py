import numpy as np
import gmpy2

with open('input.txt', 'r') as input_data:
    puzzle_input = input_data.read()
    puzzle_input = puzzle_input.split('\n\n')
    puzzle_input = [[line.strip() for line in monkey.split('\n')] for monkey in puzzle_input]


class Monkey:
    def __init__(self, mk_id, starting_items, operation, test, test_conditions):
        self.mk_id = mk_id
        self.items = starting_items
        self.operation = operation
        self.test = int(test.split()[-1])
        self.test_conditions = test_conditions
        self.inspected_items = 0
        print(f"Monkey {self.mk_id} created with: {starting_items, operation, test, test_conditions}")

    def handle_operation(self, worried):
        new_items = []
        self.inspected_items += len(self.items)

        for item in self.items:
            left = self.operation.split()[2]
            op = self.operation.split()[3]
            right = self.operation.split()[4]

            if left == 'old':
                left = item
            else:
                left = int(left)
            if right == 'old':
                right = item
            else:
                right = int(right)

            old_score = item

            item = operate(left, op, right)
            if not worried:
                item = item // 3
            else:
                item %= reducer

            new_items.append(item)
            # print(f"Mk {self.mk_id} inspected: {old_score} --> {item}")

        self.items = [item for item in new_items]

    def handle_test(self):
        for index, item in enumerate(self.items):
            throw_target = monkeys[self.test_conditions[item % self.test == 0]]
            throw_target.items.append(item)
        self.items = []

    def print_state(self):
        print(f"Monkey {self.mk_id} inspected {self.inspected_items} items")


def create_monkeys(in_data):
    monkeys = []
    for monkey in puzzle_input:
        mk_number = int(monkey[0].split()[-1].strip(':'))
        mk_start_items = [int(item) for item in monkey[1].split(': ')[1].split(', ')]
        mk_oper = monkey[2].split(': ')[1]
        mk_test = monkey[3].split(': ')[1]
        mk_conditions = {
            True: int(monkey[4].split()[-1]),
            False: int(monkey[5].split()[-1])
        }

        monkey = Monkey(mk_number, mk_start_items, mk_oper, mk_test, mk_conditions)
        monkeys.append(monkey)
    return monkeys


def add(left, right):
    return left + right


def multiply(left, right):
    return left * right


def operate(left, operator, right):
    operations = {
        '+': add,
        '*': multiply
    }

    func = operations[operator]
    return func(left, right)


def get_monkey_business(all_the_monkeyz):
    inspections = []
    for monkey in all_the_monkeyz:
        inspections.append(monkey.inspected_items)
    inspections = sorted(inspections, reverse=True)
    mk_biz = np.multiply(inspections[0], inspections[1])
    return mk_biz


monkeys = []


def go_for_rounds(is_worried, rounds):
    for i in range(rounds):

        for monkey in monkeys:
            monkey.handle_operation(is_worried)
            monkey.handle_test()
        if (i + 1) <= 20:
            print(f"round {i + 1}")
            for monkey in monkeys:
                monkey.print_state()
        elif (i + 1) % 1000 == 0:
            print(f"round {i + 1}")
            for monkey in monkeys:
                monkey.print_state()


reducer = 1


def reset_monkeys():
    global monkeys, reducer
    monkeys = None
    monkeys = create_monkeys(puzzle_input)
    for monkey in monkeys:
        reducer *= monkey.test


print(f"Supermod = {reducer}")

print(f"Part 1:")
reset_monkeys()
go_for_rounds(False, 20)
print(f"Monkey business is: {get_monkey_business(monkeys)}")

print(f"Part 2:")
reset_monkeys()
go_for_rounds(True, 10000)
print(f"Monkey business is: {get_monkey_business(monkeys)}")
