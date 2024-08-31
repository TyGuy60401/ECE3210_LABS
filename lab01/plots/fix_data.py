import pandas as pd


data = pd.read_csv('./scope_15.csv', header=1)
data['second'] = data['second'] * 1000

test_data = pd.DataFrame({
    'time':   [0, 1, 2, 3, 4, 5, 6, 7],
    'vals': [0, 1, 2, 3, 4, 5, 6, 7]
})

seven_eighths = test_data['vals'].size * 7 // 8
# remainder = test_data['vals'].size - seven_eighths
# assert seven_eighths + remainder == test_data['vals'].size, "They are not the same size :("

# print(pd.concat([test_data['vals'].iloc[seven_eighths:], test_data['vals'].iloc[:seven_eighths]]))

def swap_eighths(ser: pd.Series):
    seven_eighths = ser.size * 7 // 8

    new_series = pd.concat([ser.iloc[seven_eighths:], ser.iloc[:seven_eighths]], ignore_index=True)
    print(new_series)
    return new_series

test_data['vals'] = swap_eighths(test_data['vals'])
print(test_data)
# swap_eighths(test_data['vals'])

data['Volt'] = swap_eighths(data['Volt'])
data['Volt.1'] = swap_eighths(data['Volt.1'])
data.to_csv('./scope_15_good.csv')
