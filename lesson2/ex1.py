my_list = [1, 2.3, (1, 2.5, -4), [5, 6], True, {1: 56, 2: "one"}, ("a", "b")]
for i, value in enumerate(my_list, 1):
    print(f"{i} {value} - {type(value)}")