def sorting_func(value):
    return sorted(value, key=lambda l: (l[0], l[int(1)], l[int(2)], l[int(3)]))

if __name__ == '__main__':
    value = [
        ("Tom", "19", "167", "54"),
        ("Jony", "24", "180", "69"),
        ("Json", "21", "185", "75"),
        ("John", "27", "190", "87"),
        ("Jony", "24", "191", "98"),
    ]
    print sorting_func(value)
