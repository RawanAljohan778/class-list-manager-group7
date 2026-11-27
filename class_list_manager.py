# # Class List Manager - Group 7
# MIS 211 Bonus Assignment (GitHub Teamwork)
names = ["Rawan", "Ghaidafares", "Norah", "Reema", "Mashael"]

# ===== Each student adds her function BELOW this line =====

def count_names(names_list):
    return len(names_list)
#Written by: Ghaida 
def search_name(names, name):
    for n in names:
        if n == name:
            return True
    return False        
# Written by: Mashael (Task 5)
def names_starting_with(names, letter):
    result = []
    for name in names:
        if name.startswith(letter):
            result.append(name)
    return result


def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    # Each student calls her function here, for example:
    print("Number of names:", count_names(names))
    print("Search Reema:", search_name(names, "Reema"))
    print("Search Sara:", search_name(names, "Sara"))
    print("Names starting with R:", names_starting_with(names, "R"))
main()
