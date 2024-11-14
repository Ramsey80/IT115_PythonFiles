# Import the Json class library
import json

# Creating a dictionary array
data1 = {
    'name':'Ramsey Mell',
    'age':'23',
    'city':'Seattle, SE',
    'interests':['Hiking','Walking','Videogames','Movies','Hanging Out'],
    'isStudent': False

}

# With conditional that opens the data into a file
with open('data1.json','w') as json_file:
    json.dump(data1, json_file, indent=4)

# Confirmation that code works
print("You have successfully written to data1.json")

# loads the data from the file we created
with open('data1.json', 'r') as json_file:

    loaded_data = json.load(json_file)

# Confirmation that the loaded data works
print("Successfully able to read data1.json")
# lets us read the loaded data information
print(loaded_data)

# Allows you to change the value of each data type
loaded_data['age'] = 24

# Allows you to change the value of an array
loaded_data['interests'].append('Traveling')

# Allows you to remove values within the array
#loaded_data['interests'].remove('Traveling')

# Refreshes the data1.json to add traveling onto the array 
with open('data1.json', 'w') as json_file:

    json.dump(loaded_data, json_file, indent=4)

# Confirms that traveling is added into the loaded data file
print('Modified data has been re-written to data1.json')