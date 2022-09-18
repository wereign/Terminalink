class Group:
    def __init__(self):
        self.size = 0
        self.links = {}

    def __str__(self):

        """ 
            Operator Overloading to create a function to display all the links with name
        """
        
        string = f"\nCOUNT: {self.size}\n"
        string += f"LINKS \n"
        for link in self.links:
            string += f"{link}: {self.links[link]}\n"
        
        return string
        
    def add(self,link_name:str,link:str):
        """ 
            Add a link with a name to this group
        """
        self.size += 1
        self.links[link_name] = link
        return f"Successfully Added Link {link} to Group"

    def remove(self,link_name):
        """
            Remove a link by name from this group

        """
        self.size -= 1
        if link_name in self.links:
            del self.links[link_name]
            print("Successfully Deleted Link")
        else:
            print("Link not in Group")
        

        
    def clear(self):
        """
            Clear the group
        """
        self.size = 0
        self.links = {}

        return "Group cleared"
    
    


if __name__ == "__main__":
    group1 = Group()
    group1.add("Ironman","Ironman")
    group1.add("Cap","America")
    group1.add("Dead","Pool")
    print(group1)
    group1.remove("Ironman")
    print(group1)
