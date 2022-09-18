from Group import Group


class Groups:

    def __init__(self):
        self.groups = {}

    def __str__(self):

        string = "List of Groups\n"

        for group in self.groups:
            print(group)
            string += f"{group}\n"
            string += self.groups[group].__str__()
            string += '\n'

        return string

    def add(self, name_group):
        """
            Adds new groups to the list of groups
        """

        unique = True

        for group in self.groups:
            if group == name_group:
                unique = False
                print(
                    "Group Already Exists. Please select the group to make changes to it.")
                break

        if unique:
            self.groups[name_group] = Group()
            # print("From class",self.groups[name_group])
            print(f"Successfully Added Group {name_group}")

    def remove(self, name_group):
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

    def add_to_group(self, group_name, link_name, link):

        if group_name in self.groups:
            self.groups[group_name].add(link_name, link)
        else:
            print("Group doesn't exist!")

    def remove_from_group(self, group_name, link_name):
        if group_name in self.groups:
            self.groups[group_name].remove(link_name)
        else:
            print("Group doesn't exist")

    def clear_group(self, group_name):
        if group_name in self.groups:
            self.groups[group_name].clear()
            print("Cleared.")
        else:
            print("Group doesn't exist")
        


if __name__ == "__main__":
    m = Groups()
    print(m)
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

    # print(m)   
    m.groups["Marvel"].remove("Robot")
    m.groups["DC"].remove("Batman")
    # print(m)

    m.add_to_group("Marvel","Virenn","Virenn")
    m.remove_from_group("DC","Batman")

    # print(m)
