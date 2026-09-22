import pandas as pd

data=pd.read_csv("nato_phonetic_alphabet.csv")

new_dict ={new_key:new_value for (new_key,new_value) in data.iterrows()}
forget = pd.DataFrame(new_dict)
forget.to_csv("")
print(new_dict)