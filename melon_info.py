"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices, melon_avg_weight, melon_flesh_color, melon_rind_color


def print_melon(name, seedless, price, rind, flesh, weight):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')
    print(f'{name}s have these qualities: {rind, flesh, weight}')

for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i], melon_flesh_color[i], melon_rind_color[i], melon_avg_weight[i])

# thought process:

# from melons import melon_names, melon_seedlessness, melon_prices
# this will import values from the dictionaries in melon_info.py

# have to add in the 3 new dicitonaries created in melons.py to print

# def print_melon_qualities(rind, flesh, weight):
#       print(f'{name}s have these qualities: {rind, flesh, weight}')
# adding this to print out the extra qualities 



# this code runs but shows the extra qualities in a list without titles for each quality

# from melons import melon_names, melon_seedlessness, melon_prices, melon_avg_weight, melon_flesh_color, melon_rind_color

# def print_melon(name, seedless, price, rind, flesh, weight):
#    """Print each melon with corresponding attribute information."""

#    have_or_have_not = 'have'
#    if seedless:
#        have_or_have_not = 'do not have'

#    print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')
#    print(f'{name}s have these qualities: {rind, flesh, weight}')              # trying to figure out how to have the name/keyword 
                                                                                # of each quality before the value
# for i in melon_names:
#    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i], melon_flesh_color[i], melon_rind_color[i], melon_avg_weight[i])
