from prettytable import PrettyTable

new_table = PrettyTable()
new_table.add_column("Country", ["Bangladesh", "England", "Zimbabwe"])
new_table.add_column("Continent", ["Asia", "Europe", "Africa"])
new_table.align = 'l'

print(new_table)