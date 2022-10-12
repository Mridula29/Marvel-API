from marvel import Marvel
from keys import PUBLIC_KEY, PRIVATE_KEY


marvel = Marvel(PUBLIC_KEY=PUBLIC_KEY,
                PRIVATE_KEY=PRIVATE_KEY)

characters = marvel.characters


all_characters= characters.all()

print(len(all_characters))

my_char = characters.all(limit= 100)["data"]["results"]
len(my_char)



starts_with = ['s','m','r','i','c']
for i in range(5):
    
    res = characters.all(nameStartsWith = starts_with[0],limit = 100)["data"]["results"]
    my_char = my_char + res

print(len(my_char))

import pandas as pd
data = pd.DataFrame(my_char)
print(data)




pd.io.json
import json

json_struct= json.loads(data.to_json(orient="records"))
df_flat= pd.json_normalize(json_struct)

df_flat= df_flat[['id','name','comics.available','stories.available','series.available','events.available']]

print(df_flat.head())
