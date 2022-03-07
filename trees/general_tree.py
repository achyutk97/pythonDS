class Tree:
    def __init__(self, data) -> None:
        self.parent = None
        self.children = []
        self.data = data

    def add_tree(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        p = self.parent
        level = 0
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree_by_level(self, level):
        comp = self.get_level()
        space = " " * comp * 2
        suffix = space + "|--" if self.parent else ""
        if comp <= level:
            print(suffix, self.data)
            if self.children:
                for child in self.children:
                    child.print_tree_by_level(level)
        else:
            if self.children:
                for child in self.children:
                    child.print_tree_by_level(level)

    def print_tree(self):
        space = " " * self.get_level() * 2
        suffix = space + "|--" if self.parent else ""
        print(suffix, self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

if __name__ == '__main__':
    root = Tree("Electronics")
    laptop = Tree("Laptop")
    laptop.add_tree(Tree("ASUS"))
    laptop.add_tree(Tree("Dell"))
    laptop.add_tree(Tree("MAC Pro"))

    mobile = Tree("MOBILE")
    mobile.add_tree(Tree("Xiomia"))
    mobile.add_tree(Tree("Samsung"))
    mobile.add_tree(Tree("Nokia"))
    mobile.add_tree(Tree("Iphone"))
    mobile.add_tree(Tree("Pixel"))

    refrigerator = Tree('Refrigerator')
    refrigerator.add_tree(Tree("LG"))
    refrigerator.add_tree(Tree("Whirpool"))
    refrigerator.add_tree(Tree("Samsung"))

    root.add_tree(laptop)
    root.add_tree(refrigerator)
    root.add_tree(mobile)

    root.print_tree("")   