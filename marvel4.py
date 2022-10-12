from marvel3 import to_dataframe


column = [['id','name','comics.available', 'series.available', 'stories.available', 'events.available']]

def filter_conditions(to_dataframe, column, condition):
    {condition:'condition'}
    if condition is True:
        return to_dataframe
    else:
        print("not available")
    


filter_conditions(to_dataframe= to_dataframe, column= 'comics.available', condition = 10)
print(filter_conditions)
    
