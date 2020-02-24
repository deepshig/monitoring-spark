import random as rd

attributes = {
    1: "Class Name",
    2: "handicapped-infants",
    3: "water-project-cost-sharing",
    4: "adoption-of-the-budget-resolution",
    5: "physician-fee-freeze",
    6: "el-salvador-aid",
    7: "religious-groups-in-schools",
    8: "anti-satellite-test-ban",
    9: "aid-to-nicaraguan-contras",
    10: "mx-missile",
    11: "immigration",
    12: "synfuels-corporation-cutback",
    13: "education-spending",
    14: "superfund-right-to-sue",
    15: "crime",
    16: "duty-free-exports",
    17: "export-administration-act-south-africa"
}

attributeValues = {
    "Class Name": ["democrat", "republican"],
    "handicapped-infants": ["y", "n", "?"],
    "water-project-cost-sharing": ["y", "n", "?"],
    "adoption-of-the-budget-resolution": ["y", "n", "?"],
    "physician-fee-freeze": ["y", "n", "?"],
    "el-salvador-aid": ["y", "n", "?"],
    "religious-groups-in-schools": ["y", "n", "?"],
    "anti-satellite-test-ban": ["y", "n", "?"],
    "aid-to-nicaraguan-contras": ["y", "n", "?"],
    "mx-missile": ["y", "n", "?"],
    "immigration": ["y", "n", "?"],
    "synfuels-corporation-cutback": ["y", "n", "?"],
    "education-spending": ["y", "n", "?"],
    "superfund-right-to-sue": ["y", "n", "?"],
    "crime": ["y", "n", "?"],
    "duty-free-exports": ["y", "n", "?"],
    "export-administration-act-south-africa": ["y", "n", "?"]
}

rd.seed()
number_of_conditions = rd.randint(1, 17)

for _ in range(number_of_conditions):
    condition_index = rd.randint(1, 17)
    condition_name = attributes[condition_index]
    possible_values = attributeValues[condition_name]
    print(possible_values)
    value_index = rd.randint(0, (len(possible_values) + 1))
    value = possible_values[value_index]
    print("name : ", condition_name, "value : ", value)
