from re import M
from unicodedata import name
from Group import Group

class Groups:

    def __init__(self):
        self.groups = {}

    def __str__(self):
        
        string = "List of Groups\n"

        for group in self.groups:

            string += f"{group}\n"
            # print("LINKS: ", self.groups[group].__str__())
            string += self.groups[group].__str__()
            string += '\n'

        return string

    def add(self,name_group):
        
        """ 
            Adds new groups to the list of groups
        """

        unique = True

        for group in self.groups:
            if group == name_group:
                unique = False
                print("Group Already Exists. Please select the group to make changes to it.")
                break
        
        if unique:
            self.groups[name_group] = Group()
            print(f"Successfully Added Group {name_group}")
    
    def remove(self,name_group):
        """
            Removes an existing group from the list of groups
        """

        deleted = False

        for group in self.groups:
            if group == name_group:
                del self.groups[group]
                deleted = True
                break
        if deleted:
            print(f"Deleted {name_group}")
        else:
            print("Group does not exist.")
        


if __name__ == "__main__":
    m = Groups()
    m.add("Marvel")
    m.groups["Marvel"].add("Ironman","Robot")
    m.groups["Marvel"].add("Captain America","Robot")
    m.groups["Marvel"].add("DeadPool","Robot")
    m.groups["Marvel"].add("Robot","Robot")
    m.add("DC")
    m.groups["DC"].add("Batman","Batman")
    m.groups["DC"].add("Batman1","Batman")
    m.groups["DC"].add("Batman2","Batman")
    m.groups["DC"].add("Batman3","Batman")

    print(m)   
    m.groups["Marvel"].remove("Robot")
    m.groups["DC"].remove("Batman")
    print(m)
