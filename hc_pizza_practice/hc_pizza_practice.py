#####################################################################
# reader

'''
5 1 2 1
3 onion pepper olive
3 mushroom tomato basil
3 chicken mushroom pepper
3 tomato mushroom basil
2 chicken basil

5 pizzas, 1 team of two, 2 teams of three, and 1 team of four 
Pizza 0 has the given 3 ingredients
Pizza 1 has the given 3 ingredients
Pizza 2 has the given 3 ingredients
Pizza 3 has the given 3 ingredients
Pizza 4 has the given 2 ingredients
'''

def read_dataset(file_name):
    f = open(file_name)
    
    lines = f.readlines()
    
    l1 = lines[0].strip().split(" ")
    pizza_count = l1[0]
    
    # indexes are team sizes - 2
    # values are team counts
    team_head_count = [int(x.strip()) for x in l1[1:]]
    
    pizzas = []
    for p in lines[1:]:
      pizzas.append(p.strip().split(" ")[1:])
    return pizzas, team_head_count
# reader
#####################################################################

#####################################################################
# solver

def get_pizzas(pizza_indexes, pizzas, head_count):
  if head_count <= len(pizza_indexes):
    result = [head_count] 
    
    for i in range(head_count):
        pizza_index = pizza_indexes.pop()
        result.append(pizza_index)

  else:
    result = []

  return result

def solver(pizzas, team_head_count):
    pizzas_by_teams = []
    sorted_pizza_indexes = list(range(len(pizzas)))
    sorted_pizza_indexes.sort(key=lambda pi : len(set(pizzas[pi])))

    team_cluster_indexes = list(range(len(team_head_count)))

    while len(team_cluster_indexes) :
      team_cluster_index = team_cluster_indexes.pop()
      for team_index in range(team_head_count[team_cluster_index]) :
        head_count = team_cluster_index + 2
        pizzas_for_team = get_pizzas(sorted_pizza_indexes, pizzas, head_count)
        if len(pizzas_for_team):
            pizzas_by_teams.append(pizzas_for_team) 
    
        if not len(pizzas) :
            break
    
      if not len(pizzas) :
          break
    return pizzas_by_teams

def score(pizzas_by_teams, pizzas):
    res = 0
    for pt in pizzas_by_teams:
        unique_ingredients = set(sum([pizzas[pi] for pi in pt[1:]], []))       # check itertools.chain
        res += (len(unique_ingredients)) ** 2

    return res

# solver
#####################################################################


#####################################################################
# writer

def write_solution(file_name, pizzas_by_teams):
    '''
    2       #Pizzas are delivered to 2 teams
    2 1 4   #A 2-person team will receive Pizza 1 and Pizza 4
    3 0 2 3 #A 3-person team will receive Pizza 0, Pizza 2 and Pizza 3
    '''
    
    f1 = open(file_name, "w")
    
    f1.write("{0}\n".format(len(pizzas_by_teams)))
    
    for pt in pizzas_by_teams:
      f1.write("{0}\n".format(" ".join([str(x) for x in pt])))
    
    f1.close()

# writer
#####################################################################

PATH = "/content/pizza/"
OUT_PATH = "/content/pizza/out/"        # makes submissions easier
file_names = ["a_example.in", "e_many_teams.in","c_many_ingredients.in","d_many_pizzas.in","b_little_bit_of_everything.in"]


import time
start = time.time()

for file_name in file_names:
    print("Processing " + file_name)
    pizzas, team_head_count = read_dataset(PATH + file_name)
    pizzas_by_teams  = solver(pizzas, team_head_count)

    write_solution(OUT_PATH + file_name + ".out", pizzas_by_teams)

    print("Done. Score = " + str(score(pizzas_by_teams, pizzas)))

end = time.time()
print("Elapsed time: " + str(end - start))
