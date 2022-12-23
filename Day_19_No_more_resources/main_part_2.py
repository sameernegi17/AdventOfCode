map_hash=set()

global max_genode
global max_genode_factory
global max_ore_factory
global max_clay_factory
global max_ob_factory

#Testing Code 
cost_of_ore = 2
cost_of_clay = 3
cost_obsidian = (3,8)
cost_genode = (3,12)
max_ore_factory = max(cost_of_ore,cost_of_clay,cost_obsidian[0],cost_genode[0])
max_clay_factory = cost_obsidian[1]
max_ob_factory = cost_genode[1]

max_genode = -999999999
max_genode_factory = -999999999

def calculate_tree(ore,mp_ore,clay,mp_clay,ob,mp_ob,genode,mp_genode,cost_of_ore,cost_of_clay,cost_obsidian,cost_genode,counter =32):

    
    global max_genode
    global max_genode_factory


    if genode > max_genode :
        max_genode = genode

    if mp_genode > max_genode_factory :
        max_genode_factory = mp_genode


    if counter == 0 or mp_ore > max_ore_factory or mp_clay > max_clay_factory or  mp_ob > max_ob_factory or (ore,mp_ore,clay,mp_clay,ob,mp_ob,genode,mp_genode,counter) in  map_hash:
        return
    
    map_hash.add((ore,mp_ore,clay,mp_clay,ob,mp_ob,genode,mp_genode,counter))
        
    #GENODE ROBOT
    if ore >= cost_genode[0] and ob>= cost_genode[1]:
        calculate_tree(ore + mp_ore - cost_genode[0] , mp_ore,clay + mp_clay,mp_clay,ob+mp_ob-cost_genode[1],mp_ob, genode+mp_genode,mp_genode+1,cost_of_ore,cost_of_clay,cost_obsidian,cost_genode,counter-1)
        if mp_genode < max_genode_factory:
            return
    
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
        
    
    
    
    
cost_of_ore_list = [4, 4, 4]
cost_of_clay_list = [4, 4, 4]
cost_obsidian_list = [(2, 7), (4, 15), (4, 18)]
cost_genode_list = [(4, 13), (3, 8), (4, 9)]
    
# total_genode_robot = 0

# for i in range(0,len(cost_of_ore_list)):
#     max_genode = -999999999
#     map_hash=set()
#     cost_of_ore = cost_of_ore_list[i]
#     cost_of_clay = cost_of_clay_list[i]
#     cost_obsidian = cost_obsidian_list[i]
#     cost_genode = cost_genode_list[i]
#     max_ore_factory = max(cost_of_ore,cost_of_clay,cost_obsidian[0],cost_genode[0])
#     max_clay_factory = cost_obsidian[1]
#     max_ob_factory = cost_genode[1]
#     print(cost_of_ore,cost_of_clay,cost_obsidian,cost_genode,max_ore_factory,max_clay_factory,max_ob_factory)
#     calculate_tree(0,1,0,0,0,0,0,0,cost_of_ore,cost_of_clay,cost_obsidian,cost_genode)
#     print(max_genode)
#     total_genode_robot *= max_genode

# print(total_genode_robot)

calculate_tree(0,1,0,0,0,0,0,0,cost_of_ore,cost_of_clay,cost_obsidian,cost_genode)
print(max_genode)




        