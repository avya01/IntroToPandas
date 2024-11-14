import pandas as pd
data = {
       "Cars" : ["McLaren", "Audi", "Toyota"],
       "Colour" : ["Blue", "Black", "Royal Blue"]
}

table = pd.DataFrame(data)
print(table)

table1 = pd.DataFrame(data, index = ["Car1", "Car2", "Car3"])
print(table1)
