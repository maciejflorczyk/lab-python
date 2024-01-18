from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon name",["Pikaczu","Squirtle","Charmander"])
table.add_column("Country",["Electric","Water","Fire"])
table.align = "l"
table.border = True
print(table)