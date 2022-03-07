# Below is the management hierarchy of a company.

class Tree:
    def __init__(self, name, designation) -> None:
        self.name = name
        self.designation  = designation
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent
        
        return level

    def print_tree(self, pattern):

        space = " " * self.get_level() * 2
        suffix = space + "|--" if self.parent else ""
        if pattern == "name":
            print(suffix, self.name)
            if self.children is not None:
                for i in self.children:
                    i.print_tree(pattern)
        elif pattern == "designation":
            print(suffix, self.designation)
            if self.children:
                for i in self.children:
                    i.print_tree(pattern)
        else:
            print(suffix,self.name + ' ('+ self.designation + ')')   
            if self.children:
                for i in self.children:
                    i.print_tree(pattern)

if __name__ == '__main__':
    ceo = Tree("Nilupul", "CEO")
    cto = Tree("Chinmay", "CTO")
    infoHead = Tree("Vishwa", "Infrastructure Head")
    appHead = Tree("Aamir", "Application Head")

    infoHead.add_child(Tree("Dhawal", "Cloud Manager"))
    infoHead.add_child(Tree("Abhijit", "App Manager"))

    gesl = Tree("gesl", "HR Head")
    gesl.add_child(Tree("Peter", "Recruitement Manager"))
    gesl.add_child(Tree("Waqas", "Policy Manager"))

    cto.add_child(infoHead)
    cto.add_child(appHead)
    ceo.add_child(cto)
    ceo.add_child(gesl)

    print("\n By Name \n")
    ceo.print_tree("name")
    print("\n Both \n")
    ceo.print_tree("both")
    print("\n Designation \n")
    ceo.print_tree("designation")