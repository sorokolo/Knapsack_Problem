import numpy as np
def max_profit(objects, profits, weights, max_w):
    # Converting the lists into numpy arrays
    np_objects = np.array(objects)
    np_profits = np.array(profits)
    np_weights = np.array(weights)
    fraction = np_profits / np_weights

    # Creates a dictionary that has the the fractions and the corresponding index
    # This will help refer to the corresponding weight and objects and profits
    fraction_dict = {}
    j = 0
    for i in fraction:
        fraction_dict[i] = j
        j += 1

    # Converts the dictionary into a tuple
    fraction_tuple = sorted(fraction_dict.items())

    # The following lists are for the selected fractions, objects and and profits
    selected_fractions = []
    selected_profit = []
    selected_objects = []

    # Populate the selected lists by looping
    while (max_w > 0):
        i = len(fraction_tuple) - 1
        while (i >= 0):
            if (max_w >= np_weights[fraction_tuple[i][1]]):
                max_w -= np_weights[fraction_tuple[i][1]]
                selected_fractions.append(1)
                selected_profit.append(np_profits[fraction_tuple[i][1]])
                selected_objects.append(np_objects[fraction_tuple[i][1]])

            elif (max_w <= np_weights[fraction_tuple[i][1]]):
                temp = max_w
                max_w -= max_w
                selected_fractions.append(temp / weights[fraction_tuple[i][1]])
                selected_profit.append(np_profits[fraction_tuple[i][1]])
                selected_objects.append(np_objects[fraction_tuple[i][1]])

                break

            i -= 1

    #          Calculate the total profit
    array_total_profit = np.array(selected_fractions)*(np.array(selected_profit))
    total_profit = array_total_profit.sum()
    return selected_objects, selected_fractions, total_profit



object = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
profits = [10, 5, 20, 7, 6, 18, 3]
weights = [2, 3, 5, 7, 1, 5, 1]
max_profit(object, profits, weights, 16)

selected_objects, selected_fractions, total_profit = max_profit(object, profits, weights, 16)

print(selected_objects)
print(selected_fractions)
print(total_profit)



