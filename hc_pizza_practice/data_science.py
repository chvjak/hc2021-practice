from hc_pizza_practice import *
import matplotlib.pyplot as plt

def analyse_file(file_name) :
    print("Processing " + file_name)
    
    pizzas, team_head_count = read_dataset(PATH + file_name)


    total_teams = sum(team_head_count)
    total_pizzas = len(pizzas)
    avg_pizza_size = sum([len(p) for p in pizzas]) / len(pizzas)

    print("total_teams=%d" % total_teams)
    print("total_pizzas=%d" % total_pizzas)
    print("avg_pizza_size=%d" % avg_pizza_size)
    print()

    # plot distribution of pizza sizes (total ingredients)
    #plot_pizza_sizes(pizzas)

    # plot distribution of various ingredients, 100k might be problematic but worth trying
    plot_ingredients(pizzas)


def plot_pizza_sizes(pizzas):
    n_bins = 20
    pizza_sizes = [len(p) for p in pizzas]
    
    plt.hist(pizza_sizes , bins=n_bins)
    plt.show()


def plot_ingredients(pizzas):
    pizzas.sort(key = lambda p:len(p))
    ingredients = []
    ingredients_x = []
    ingredients_stacked = []
    for i, p in enumerate(pizzas):
        p.sort()
        ingredients += p
        ingredients_x += [i] * len(p)
        ingredients_stacked += range(len(p))

    import matplotlib.pyplot as plt
    plt.scatter(x=ingredients_x, y=ingredients_stacked , c=ingredients)
    plt.show()

file_names = ["a_example.in", "b_little_bit_of_everything.in"]
for f in file_names:
    analyse_file(f)
