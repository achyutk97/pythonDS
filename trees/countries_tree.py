
from general_tree import *


def build_location_tree():
    base = Tree("Global")

    india = Tree("India")
    gujurat = Tree("Gujurat")
    gujurat.add_tree(Tree("Ahmedabad"))
    gujurat.add_tree(Tree("Baroda"))
    
    karnataka = Tree("Karnataka")
    karnataka.add_tree(Tree("Bangaluru"))
    karnataka.add_tree(Tree("Mysore"))

    india.add_tree(gujurat)
    india.add_tree(karnataka)

    usa = Tree("USA")
    nj = Tree("New Jursey")
    nj.add_tree(Tree("pricenton"))
    nj.add_tree(Tree("Trenton"))

    cali = Tree("California")
    cali.add_tree(Tree("San Francisco"))
    cali.add_tree(Tree("Moutain View"))
    cali.add_tree(Tree("Palo Alto"))

    usa.add_tree(nj)
    usa.add_tree(cali)
    base.add_tree(india)
    base.add_tree(usa)

    return base  

if __name__ == '__main__':
    root = build_location_tree()
    root.print_tree_by_level(1)