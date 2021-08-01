def sortNumbers(data, condition):
    for i in range(len(data)):
        least = i
        for k in range(i + 1, len(data)):
            if condition == "ASC":
                if data[k] < data[least]:
                    least = k
            elif condition == "DESC":
                if data[k] > data[least]:
                    least = k
        data[least], data[i] = data[i], data[least]
    return data


def sortData(weights, data, condition):
    if len(weights) != len(data):
        raise ValueError('Invalid input data')
    for i in range(len(weights) - 1):
        for k in range(len(weights) - i - 1):
            if condition == "ASC":
                if weights[k] > weights[k + 1]:
                    weights[k], weights[k + 1] = weights[k + 1], weights[k]
                    data[k], data[k + 1] = data[k + 1], data[k]
            elif condition == "DESC":
                if weights[k] < weights[k + 1]:
                    weights[k], weights[k + 1] = weights[k + 1], weights[k]
                    data[k], data[k + 1] = data[k + 1], data[k]

    return data
