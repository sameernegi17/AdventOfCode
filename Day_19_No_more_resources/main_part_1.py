map_hash=set()

global max_genode

#Testing Code 
cost_of_ore = 2
cost_of_clay = 3
cost_obsidian = (3,8)
cost_genode = (3,12)

max_genode = -999999999
max_genode_factory = -999999999

def calculate_tree(ore,mp_ore,clay,mp_clay,ob,mp_ob,genode,mp_genode,cost_of_ore,cost_of_clay,cost_obsidian,cost_genode,counter =24):

    global max_genode

    if genode > max_genode :
        max_genode = genode

    if counter == 0:
        return

    #OPTIMIZATION 
    if (ore,mp_ore,clay,mp_clay,ob,mp_ob,genode,mp_genode,counter) in  map_hash:
        return
    
    map_hash.add((ore,mp_ore,clay,mp_clay,ob,mp_ob,genode,mp_genode,counter))
        
    #GENODE ROBOT
    if ore >= cost_genode[0] and ob>= cost_genode[1]:
        calculate_tree(ore + mp_ore - cost_genode[0] , mp_ore,clay + mp_clay,mp_clay,ob+mp_ob-cost_genode[1],mp_ob, genode+mp_genode,mp_genode+1,cost_of_ore,cost_of_clay,cost_obsidian,cost_genode,counter-1)
    
    #OBSIDIAN
    if ore >= cost_obsidian[0] and clay>= cost_obsidian[1]:
        calculate_tree(ore + mp_ore - cost_obsidian[0], mp_ore,clay + mp_clay-cost_obsidian[1],mp_clay,ob+mp_ob,mp_ob+1, genode+mp_genode,mp_genode,cost_of_ore,cost_of_clay,cost_obsidian,cost_genode,counter-1)
    #CLAY
    if ore >=cost_of_clay :
        calculate_tree(ore + mp_ore - cost_of_clay, mp_ore,clay + mp_clay,mp_clay+1,ob+mp_ob,mp_ob,genode+mp_genode,mp_genode,cost_of_ore,cost_of_clay,cost_obsidian,cost_genode, counter-1)
    #ORE
    if ore >= cost_of_ore and mp_ore <= 4:
        calculate_tree(ore + mp_ore - cost_of_ore, mp_ore+1,clay+ mp_clay,mp_clay,ob+mp_ob,mp_ob,genode+mp_genode,mp_genode,cost_of_ore,cost_of_clay,cost_obsidian,cost_genode, counter-1)

    calculate_tree(ore + mp_ore, mp_ore,clay+ mp_clay,mp_clay,ob+mp_ob,mp_ob,genode+mp_genode,mp_genode,cost_of_ore,cost_of_clay,cost_obsidian,cost_genode, counter-1)
        
       
cost_of_ore_list = [4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 4, 2, 4, 3, 4, 4, 4]
cost_of_clay_list = [4, 4, 4, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 4, 4, 4, 3, 3, 3, 4, 4, 2, 3, 3, 3, 4, 4]
cost_obsidian_list =  [(2, 7), (4, 15), (4, 18), (4, 20), (4, 8), (3, 14), (3, 11), (2, 15), (3, 17), (2, 8), (3, 18), (4, 12), (3, 17), (2, 10), (2, 16), (4, 17), (3, 18), (4, 9), (3, 18), (2, 17), (4, 19), (2, 13), (4, 5), (4, 11), (2, 7), (2, 19), (2, 12), (4, 5), (2, 11), (4, 8)]
cost_genode_list =  [(4, 13), (3, 8), (4, 9), (2, 12), (3, 7), (4, 15), (4, 7), (3, 16), (3, 10), (3, 9), (4, 8), (4, 19), (3, 13), (3, 14), (2, 18), (3, 11), (4, 16), (3, 9), (4, 19), (3, 19), (4, 7), (2, 9), (3, 12), (4, 12), (2, 14), (3, 13), (2, 10), (3, 10), (4, 8), (4, 14)]
    
total_genode_robot = 0

for i in range(0,len(cost_of_ore_list)):
    max_genode = -999999999
    map_hash=set()
    cost_of_ore = cost_of_ore_list[i]
    cost_of_clay = cost_of_clay_list[i]
    cost_obsidian = cost_obsidian_list[i]
    cost_genode = cost_genode_list[i]
    print(cost_of_ore,cost_of_clay,cost_obsidian,cost_genode)
    calculate_tree(0,1,0,0,0,0,0,0,cost_of_ore,cost_of_clay,cost_obsidian,cost_genode)
    print(max_genode)
    total_genode_robot += (i+1)*max_genode

print(total_genode_robot)

# calculate_tree(0,1,0,0,0,0,0,0,cost_of_ore,cost_of_clay,cost_obsidian,cost_genode)
# print(max_genode)




        