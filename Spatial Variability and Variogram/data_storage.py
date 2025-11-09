datasets = {
    "Set_1": [2, 3, 3, 9, 7, 7, 7, 9, 7],
    "Set_2": [2, 4, 6, 16, 18, 12, 10, 20, 14],
    "Set_3": [1, 5, 5, 6, 6, 8, 10, 11, 11]
}

def list_datasets():
    """Lists all available data sets."""
    print('\nCurrent data sets:')

    for i, name in enumerate(datasets.keys(), 1):
        print(f"{i}, {name}")

    print()

def get_dataset(name):
    """Return the data set with name."""
    return datasets.get(name, None)