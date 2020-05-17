
# Правая разносторонняя производная
def right(y_cur, y_next, h):
    return (y_next - y_cur) / h


# Левая разносторонняя производная
def left(y_cur, y_prev, h):
    return (y_cur - y_prev) / h


# Центральная формула для левой производной (боже че я только что написала)
def center(y_next, y_prev, step):
    return (y_next - y_prev) / h


# Центральная формула для x0
def center_x0(y_0, y_1, y_2, step):
    return (-3 * y_0 + 4 * y_1 - y_2) / (2 * step)


# Так... а это для xn
def center_xn(y_n, yn_1, yn_2, step):
    return (3 * y_n - 4 * yn_1 + yn_2) / (2 * step)


# Односторонняя разносторонняя производная
def method_1(input_data, step):
    output_data = []
    for i in range(len(input_data) - 1):
        output_data.append(right(input_data[i], input_data[i + 1], h))

    output_data.append(left(data[len(input_data) - 1], data[len(input_data) - 2], h))

    return output_data


# Центральная разносторонняя производная
def method_2(input_data, step):
    output_data = []
    length = len(input_data)
    for i in range(1, length - 1):
        output_data.append(center(input_data[i - 1], input_data[i + 1], step))

    output_data.append(center_x0(input_data[0], input_data[1], input_data[2], step))
    output_data.append(center_x0(input_data[length - 1], input_data[length - 2], input_data[length - 3], step))

    return output_data


x = [1, 2, 3, 4, 5, 6]
data = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]

table = [x, data, [], [], [], [], []]

h = 1

d1 = method_1(data, h)
d2 = method_2(data, h)

print(d1)
print(d2)