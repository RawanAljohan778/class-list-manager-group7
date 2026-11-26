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
def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    # Each student calls her function here, for example:
    print("Number of names:", count_names(names))
    print("Search Reema:", search_name(names, "Reema"))
    print("Search Sara:", search_name(names, "Sara"))
main()
