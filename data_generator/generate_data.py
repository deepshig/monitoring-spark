import random
import csv

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

file_location = open(
    "/Users/vinayakprasad/Desktop/congressional-voting-records/house-votes-84.csv", "r")
file_read = csv.reader(file_location)

new_file = open("1.csv", "a")
new_file_write = csv.writer(new_file)
new_file_write.writerow(('class_name', 'handicapped_infants', 'water_project_cost_sharing',
                         'adoption_of_the_budget_resolution', 'physician_fee_freeze',
                         'el_salvador_aid', 'religious_groups_in_schools', 'anti_satellite_test_ban', 'aid_to_nicaraguan_contras',
                         'mx_missile', 'immigration', 'synfuels_corporation_cutback', 'education_spending', 'superfund_right_to_sue',
                         'crime', 'duty_free_exports', 'export_administration_act_south_africa'))
for i in range(5000000):
    new_file_write.writerow((random.choice(["democrat", "republican"]), random.choice(['y', 'n', '?']),
                             random.choice(['y', 'n', '?']), random.choice(
                                 ['y', 'n', '?']),
                             random.choice(['y', 'n', '?']),
                             random.choice(['y', 'n', '?']),
                             random.choice(['y', 'n', '?']), random.choice(
                                 ['y', 'n', '?']),
                             random.choice(['y', 'n', '?']), random.choice(
                                 ['y', 'n', '?']),
                             random.choice(['y', 'n', '?']),
                             random.choice(['y', 'n', '?']), random.choice(
                                 ['y', 'n', '?']),
                             random.choice(['y', 'n', '?']), random.choice(
                                 ['y', 'n', '?']),
                             random.choice(['y', 'n', '?']),
                             random.choice(['y', 'n', '?'])))

file_location.close()
