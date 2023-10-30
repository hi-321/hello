import pandas as pd
import math

def entropy(class_counts):
    total_count = sum(class_counts)
    return -sum((count / total_count) * math.log2(count / total_count) for count in class_counts if count > 0)

def information_gain(attribute, target):
    total_entropy = entropy(target.value_counts())
    weighted_entropy = sum(
        (len(subset) / len(target)) * entropy(subset.value_counts())
        for subset in [target[attribute == value] for value in attribute.unique()]
    )
    return total_entropy, weighted_entropy, total_entropy - weighted_entropy

def get_root_node(data):
    root_node, max_criterion = None, -1
    for column in data.columns[:-1]:
        total_entropy, weighted_entropy, information_gain_i = information_gain(data[column], data[data.columns[-1]])
        print(f"Total Entropy = {total_entropy:.4f}")
        print(f"Attribute = {column}\n")
        for value in data[column].unique():
            subset = data[data[column] == value]
            entropy_i = entropy(subset[data.columns[-1]].value_counts())
            print(f"Entropy({value}) = {entropy_i:.4f}")
        print(f"Weighted entropy for {column} : {weighted_entropy:.5f}")
        print(f"Information gain for({column}) = {information_gain_i:.5f}\n")
        if information_gain_i > max_criterion:
            max_criterion, root_node = information_gain_i, column
    print(f"The root node is: {root_node}")
    return root_node

if __name__ == "__main__":
    data = pd.read_csv("C:/Users/VIJAY/OneDrive/Desktop/CI/Exercise 4/Buy_Computer.csv")
    root_node = get_root_node(data)
