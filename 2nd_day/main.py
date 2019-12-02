import json


def get_value(index, offset):
    target = opcodes[index + offset]
    return opcodes[target]


def add(index):
    value1 = get_value(index, 1)
    value2 = get_value(index, 2)
    sum_target = opcodes[index + 3]
    opcodes[sum_target] = value1 + value2
    return True


def multiply(index):
    value1 = get_value(index, 1)
    value2 = get_value(index, 2)
    multiply_target = opcodes[index + 3]
    opcodes[multiply_target] = value1 * value2
    return True


def end(index):
    return None


def prepare_data():
    opcodes[1] = 12
    opcodes[2] = 2


def first_exercise():
    for index, code in enumerate(opcodes):
        if index % 4 == 0:
            operation = CODE_OPERATIONS.get(code, None)
            if operation is None:
                break
            result = operation(index)
            if result is None:
                break


def second_exercise():
    global opcodes
    for _noun in range(100):
        for _verb in range(100):
            opcodes = INITIAL_OPCODES.copy()
            opcodes[1] = _noun
            opcodes[2] = _verb
            first_exercise()
            if SECOND_EXERCISE_TARGET_RESULT == opcodes[0]:
                return _noun, _verb


def save_data():
    with open("output_data.json", "w") as fout:
        json.dump({
            "First Exercise": first_exercise_result,
            "Second Exercise": int(f"{noun}{verb}")
        }, fout)


if __name__ == '__main__':
    with open("input_data.txt", "r") as fin:
        line = fin.read()
        INITIAL_OPCODES = list(map(lambda x: int(x), line.split(",")))
    opcodes = INITIAL_OPCODES.copy()
    CODE_OPERATIONS = {
        1: add,
        2: multiply,
        99: end
    }
    prepare_data()
    first_exercise()
    first_exercise_result = opcodes[0]
    print(first_exercise_result)
    SECOND_EXERCISE_TARGET_RESULT = 19690720
    noun, verb = second_exercise()
    print(f"noun: {noun}, verb: {verb}")
    save_data()
