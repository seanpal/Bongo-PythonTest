def print_depth(data, depth=1):
    for key, value in data.items():
        print(key, depth)
        if isinstance(value, dict):
            print_depth(value, depth=depth+1)

data = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}
print_depth(data)