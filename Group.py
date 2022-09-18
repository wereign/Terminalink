class Group:
    def __init__(self,name):
        self.name = name
        self.links = {}

    def add(self,link_name:str,link:str):
        """ 
            Add a link with a name to this group
        """
        self.links[link_name] = link
        return f"Successfully Added Link {link} to Group {self.name}"

    def remove(self,link_name):
        """
            Remove a link by name from this group

        """

        if link_name in self.links:
            del self.links[link_name]
            print("Successfully Deleted Link")
        else:
            print("Link not in Group")
        

        
    def clear(self):
        """
            Clear the group
        """

        self.links = {}

        return "Group cleared"
    
    def __str__(self):

        """ 
            Operator Overloading to create a function to display all the links with name
        """
        
        string = f"GROUP: {self.name}\n\nLINKS \n"

        for link in self.links:
            string += f"{link}: {self.links[link]}\n"
        
        return string
    


if __name__ == "__main__":
    group1 = Group("Marvel")
    group1.add("Ironman","Ironman")
    group1.add("Cap","America")
    group1.add("Dead","Pool")
    print(group1)
    group1.remove("Ironman")
    print(group1)
