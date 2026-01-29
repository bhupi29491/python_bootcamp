## Modifying a List in a Function ##

# Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'drone frame', 'custom keychain']
completed_models = []

# Simulate printing each design until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

print("==========================================================")


def print_models(unprinted_designs_1, completed_models_1):
    """
    Simulate printing each design until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs_1:
        curr_design = unprinted_designs_1.pop()
        print(f"Printing model: {curr_design}")
        completed_models_1.append(curr_design)


def show_completed_models(completed_models_1):
    """Display all completed models."""
    print("\nThe following models have been printed:")
    for completed_model_1 in completed_models_1:
        print(completed_model_1)


unprinted_designs_1 = ['phone case', 'robot pendant', 'dodecahedron']
completed_models_1 = []

print_models(unprinted_designs_1, completed_models_1)
show_completed_models(completed_models_1)
