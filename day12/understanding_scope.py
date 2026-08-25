enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
   
    return enemies + 2
    
increase_enemies()
print(f"enemies out side the function: {enemies}")
