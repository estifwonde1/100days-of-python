import os
target_dir = "output/ready_to_send"
with open("input/letters/starting_letters.txt") as file:
    content = file.read()

with open("input/names/invited_names.txt") as invintee:
    names = invintee.read().splitlines()
for name in names:
    if name.strip():
        personalise = content.replace("[name]",name)

        p_letters = f"invitation_{name.replace(" ","_")}.txt"
        destination = os.path.join(target_dir,p_letters)
        with open(destination,"w") as file :
            right = file.write(personalise)
        print(f"created{destination}")

with open("input/letters/receipt_plan.txt") as file:
    content_1 = file.read()

with open("input/names/orders.txt") as inputs:
   for data in inputs:
    name,price=data.strip().split(",")
    naming = content_1.replace("[Customer]",name).replace("[Price]",price)
   

    receipt =f"ThankYou_{name.replace(" ","_")}.txt"
    destined=os.path.join(target_dir,receipt)
    with open(destined,"w") as file:
        write = file.write(naming)
        print(f"created{destined}")
       
 






