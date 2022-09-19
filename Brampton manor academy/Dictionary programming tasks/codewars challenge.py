def createDict(keys, values):
    dictionary = dict()
    if len(keys)-len(values) != 0:
        for i in range(len(keys)-len(values)):
            values.append(None)
    for x in range(len(keys)):
        dictionary[keys[x]] = values[x]
    return dictionary
keys=['a', 'b', 'c', 'd']
values=[1, 2, 3]
print(createDict(keys, values))
