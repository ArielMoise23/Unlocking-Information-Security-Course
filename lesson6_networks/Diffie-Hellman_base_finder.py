def is_generator(g, p):
    required_set = set(range(1, p))
    actual_set = set(pow(g, power, p) for power in range(1, p))
    # print(required_set)
    print(actual_set)
    return required_set == actual_set

p = 13
generators = []

for g in range(2, p):  # g must be >1 and <p
    if is_generator(g, p):
        generators.append(g)

print(generators)
