from marvel3 import to_dataframe


#column = [['id','name','comics.available', 'series.available', 'stories.available', 'events.available']]

def filter_conditions(to_dataframe, column, condition,value):
    if column == 'name':
        condition = 'starts_with'
        length = len(value)
        return (to_dataframe[to_dataframe.name.str[:length] == value])
    else:
        if condition == 'equal to':
            return {to_dataframe[to_dataframe[column] == int(value)]}
        elif condition == 'greater_than':
            return {to_dataframe[to_dataframe[column] > int(value)]}
        elif condition == 'less_than':
            return {to_dataframe[to_dataframe[column] <int(value)]}
        else:
            return ("Not Available")
    


filter_conditions(to_dataframe= to_dataframe, column= 'comics.available', condition='equal to', value= 5)
print(filter_conditions)
    