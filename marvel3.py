from datetime import datetime
from urllib import response
import requests
from keys import PUBLIC_KEY, PRIVATE_KEY
import pandas as pd
import hashlib


timestamp = datetime.now()
public_key: PUBLIC_KEY
private_key: PRIVATE_KEY

def to_dataframe(nameStartsWith, apikey = None, hash = None):
    global df_flat
    if apikey and hash:
        request_url = "https://gateway.marvel.com/v1/public/characters"
        params = {'ts':timestamp, 'apikey': apikey, 'hash': hash, 'nameStartsWith': nameStartsWith, 'limit':100}
        response = requests.get(request_url, params= params)
         
        print(response.json())
        data= response.json()
        df_flat= pd.json_normalize(data, record_path=['data','results'])
        
        df1 = df_flat[['id','name','comics.available','stories.available','series.available','events.available']]
        return df1
    else:
        raise Exception("Missing apikey or hash")




hash_md5= hashlib.md5()
hash_md5.update(f'{timestamp}{PRIVATE_KEY}{PUBLIC_KEY}'.encode('utf-8'))
hashed_params = hash_md5.hexdigest()

df = to_dataframe(nameStartsWith='x', apikey= PUBLIC_KEY, hash= hashed_params)
print(df.head())