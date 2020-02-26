import random as rd

attributes = {
    1: "class_name",
    2: "handicapped_infants",
    3: "water_project_cost_sharing",
    4: "adoption_of_the_budget_resolution",
    5: "physician_fee_freeze",
    6: "el_salvador_aid",
    7: "religious_groups_in_schools",
    8: "anti_satellite_test_ban",
    9: "aid_to_nicaraguan_contras",
    10: "mx_missile",
    11: "immigration",
    12: "synfuels_corporation_cutback",
    13: "education_spending",
    14: "superfund_right_to_sue",
    15: "crime",
    16: "duty_free_exports",
    17: "export_administration_act_south_africa"
}

attributeValues = {
    "class_name": ["democrat", "republican"],
    "handicapped_infants": ["y", "n", "?"],
    "water_project_cost_sharing": ["y", "n", "?"],
    "adoption_of_the_budget_resolution": ["y", "n", "?"],
    "physician_fee_freeze": ["y", "n", "?"],
    "el_salvador_aid": ["y", "n", "?"],
    "religious_groups_in_schools": ["y", "n", "?"],
    "anti_satellite_test_ban": ["y", "n", "?"],
    "aid_to_nicaraguan_contras": ["y", "n", "?"],
    "mx_missile": ["y", "n", "?"],
    "immigration": ["y", "n", "?"],
    "synfuels_corporation_cutback": ["y", "n", "?"],
    "education_spending": ["y", "n", "?"],
    "superfund_right_to_sue": ["y", "n", "?"],
    "crime": ["y", "n", "?"],
    "duty_free_exports": ["y", "n", "?"],
    "export_administration_act_south_africa": ["y", "n", "?"]
}


def get_random_conditions():
    rd.seed()
    number_of_conditions = rd.randint(1, 17)

    conditions = {}
    for _ in range(number_of_conditions):
        condition_index = rd.randint(1, 17)
        condition_name = attributes[condition_index]

        possible_values = attributeValues[condition_name]
        value_index = rd.randint(0, (len(possible_values) - 1))
        value = possible_values[value_index]

        conditions[condition_name] = value

    return conditions


def generate_query():
    query = "SELECT * FROM voting_records WHERE "
    condtions = get_random_conditions()

    i = 0
    for name in condtions:
        query = query + name + "='" + condtions[name] + "'"

        if i < len(condtions) - 1:
            query = query + " AND "

        i = i+1

    return query
