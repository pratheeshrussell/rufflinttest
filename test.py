def make_three_adders():
    result = []
    for i in [10, 20, 30]:
        def add(x):
            return x + i
        result.append(add)
    return result

for adder in make_three_adders():
    print(adder(7))  # noqa