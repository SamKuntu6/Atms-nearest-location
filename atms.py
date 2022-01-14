
# Here are three functions 

# First have the user's current location 
def user_location():
    latitude = 10.34
    longitude = 39.75
    return latitude, longitude # return cordinates of the user


# Second have the atms location in a given radius area
def nearest_atms(radius=5): # 5 is default value when none is given
    atms = []

    # assumed dictionary values of map coordinates where key 2:'latitude', and key 3:'longitude'
    no_1 = {1: '50', 2: 30, 3: 70, 4: '20', 5: '20'} 
    no_2 = {1: '60', 2: 40, 3: 90, 4: '30', 5: '40'} 
    no_3 = {1: '70', 2: 23, 3: 50, 4: '50', 5: '10'} 
    no_4 = {1: '50', 2: 55, 3: 60, 4: '20', 5: '20'} 
    no_5 = {1: '60', 2: 40, 3: 35, 4: '30', 5: '40'} 
    no_6 = {1: '70', 2: 63, 3: 54, 4: '50', 5: '10'} 
    
    #select the atms in a given radius area (5kms, 10kms, 15kms, 20kms, etc)
    if radius <= radius: # (for demonstration)
       atms.append(atms) # 
    
    atms = no_1, no_2, no_3, no_4, no_5, no_6 # selected atms in the given radius
    list_latitude = []
    list_longitude = []
    
    for atm in atms:
        list_latitude.append(atm[2])
        list_longitude.append(atm[3])

    number_of_available_atms = atms.__len__()
    
    # return a tuple of - number of available atms and their respective coordinates
    return number_of_available_atms, list_latitude, list_longitude


# Then find the shortest distance between their differences to the users location
def shortest_distance():
    user = user_location()
    user_area = nearest_atms(10) # overwrite default value of 5
    iters = user_area[0]
    distance_list = []

    for i in range(iters):
        latitude_diff = user_area[1][i] - user[0]
        longitude_diff = user_area[2][i] - user[1]
        dist = latitude_diff ** 2 + longitude_diff ** 2
        distance_list.append(dist)
        distance_list.sort()
        
        if not i > 0:
            tempo_small = distance_list[0]
            shortest_dist = tempo_small
            coordinates_values = user_area[1][i], user_area[2][i], shortest_dist
        else:
            if distance_list[0] < shortest_dist:
                shortest_dist = distance_list[0]
                coordinates_values = user_area[1][i], user_area[2][i]
            else:
                pass
    return coordinates_values

x_disp = shortest_distance()
print(x_disp)
