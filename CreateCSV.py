import pandas as pd
import numpy as np
data = {
       "Name" : ["James", "Tom", "Lara", "Jacob"],
       "Job Title" : ["Manager", "Intern", "Sr Manager", "Principle"],
       "Hired" : ["Yes", "Yes", "No", "No"],
       "Starting Date" : ["16 November", "9 December", np.nan, np.nan]
}

table = pd.DataFrame(data, index = ["Can1", "Can2", "Can3", "Can4"])
print(table)

table.to_csv("Recruitment.csv")