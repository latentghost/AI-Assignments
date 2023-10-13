from numpy import random
random.seed(456)


locations_weather_based = {
    'Agra': {'W': 'summer', 'A': 17, 'T': 'getaway', 'B': 15000, 'R': 8.2},
    'Udaipur': {'W': 'summer', 'A': 17, 'T': 'getaway', 'B': 10000, 'R': 7.9},
    'Jaipur': {'W': 'summer', 'A': 17, 'T': 'getaway', 'B': 9000, 'R': 8.0},
    'Kerala': {'W': 'summer', 'A': 17, 'T': 'activities', 'B': 20000, 'R': 8.2},
    'Bangalore': {'W': 'summer', 'A': 17, 'T': 'activities', 'B': 15000, 'R': 7.2},
    'Delhi': {'W': 'summer', 'A': 17, 'T': 'activities', 'B': 8000, 'R': 8.0},
    'Buenos Aires': {'W': 'summer', 'A': 17, 'T': 'getaway', 'B': 88000, 'R': 8.3},
    'Bali': {'W': 'summer', 'A': 17, 'T': 'getaway', 'B': 67000, 'R': 8.6},
    'Thailand': {'W': 'summer', 'A': 17, 'T': 'getaway', 'B': 34000, 'R': 8.8},
    'Maldives': {'W': 'summer', 'A': 17, 'T': 'getaway', 'B': 32000, 'R': 8.6},
    'Australia': {'W': 'summer', 'A': 17, 'T': 'activities', 'B': 28000, 'R': 8.1},
    'Dubai': {'W': 'summer', 'A': 17, 'T': 'activities', 'B': 16000, 'R': 8.1},
    'New Zealand': {'W': 'summer', 'A': 17, 'T': 'activities', 'B': 27000, 'R': 8.1},
    'Machu Picchu': {'W': 'summer', 'A': 17, 'T': 'activities', 'B': 40000, 'R': 7.9},
    'Dehradun': {'W': 'winter', 'A': 17, 'T': 'getaway', 'B': 12000, 'R': 7.7},
    'Rishikesh': {'W': 'winter', 'A': 17, 'T': 'getaway', 'B': 8000, 'R': 7.1},
    'Kashmir': {'W': 'winter', 'A': 17, 'T': 'getaway', 'B': 18000, 'R': 8.4},
    'Shimla': {'W': 'winter', 'A': 17, 'T': 'activities', 'B': 10000, 'R': 7.9},
    'Manali': {'W': 'winter', 'A': 17, 'T': 'activities', 'B': 14000, 'R': 8.0},
    'Mussoorie': {'W': 'winter', 'A': 17, 'T': 'activities', 'B': 12000, 'R': 7.8},
    'Andaman and Nicobar': {'W': 'winter', 'A': 17, 'T': 'getaway', 'B': 15000, 'R': 8.2},
    'Norway': {'W': 'winter', 'A': 17, 'T': 'getaway', 'B': 50000, 'R': 8.9},
    'Greenland': {'W': 'winter', 'A': 17, 'T': 'getaway', 'B': 30000, 'R': 8.2},
    'Prague': {'W': 'winter', 'A': 17, 'T': 'getaway', 'B': 40000, 'R': 8.5},
    'Las Vegas': {'W': 'winter', 'A': 17, 'T': 'activities', 'B': 80000, 'R': 9.0},
    'Iceland': {'W': 'winter', 'A': 17, 'T': 'activities', 'B': 45000, 'R': 8.6},
    'London': {'W': 'winter', 'A': 17, 'T': 'activities', 'B': 50000, 'R': 8.2},
    'Switzerland': {'W': 'winter', 'A': 17, 'T': 'activities', 'B': 60000, 'R': 8.9},
    'Goa': {'W': 'tropical', 'A': 17, 'T': 'coastal', 'B': 19000, 'R': 8.9},
    'Mumbai': {'W': 'tropical', 'A': 17, 'T': 'coastal', 'B': 13500, 'R': 7.9},
    'Diu': {'W': 'tropical', 'A': 17, 'T': 'coastal', 'B': 18000, 'R': 7.9},
    'British Virgin Islands': {'W': 'tropical', 'A': 17, 'T': 'coastal', 'B': 30000, 'R': 7.7},
    'Bermuda': {'W': 'tropical', 'A': 17, 'T': 'coastal', 'B': 29000, 'R': 7.7},
    'Philippines': {'W': 'tropical', 'A': 17, 'T': 'coastal', 'B': 25000, 'R': 7.8},
    'Brazil': {'W': 'tropical', 'A': 17, 'T': 'rainforest', 'B': 89000, 'R': 8.0},
    'Costa Rica': {'W': 'tropical', 'A': 17, 'T': 'rainforest', 'B': 60000, 'R': 8.0},
    'Peru-Tambopata National Reserve': {'W': 'tropical', 'A': 17, 'T': 'rainforest', 'B': 50000, 'R': 8.2},
    'Cuyabeno Reserve-Amazon forest': {'W': 'tropical', 'A': 17, 'T': 'rainforest', 'B': 50000, 'R': 8.2},
    'Alaska': {'W': 'tropical', 'A': 17, 'T': 'rainforest', 'B': 56000, 'R': 8.3},
    'Puerto Rico': {'W': 'tropical', 'A': 17, 'T': 'rainforest', 'B': 47000, 'R': 8.3}
}

locations_activity_based = {
    'Disneyland': {'Ac': 'Theme Parks', 'Ag': 16, 'B':30000, 'T': 'Amusement Parks', 'R': 8.5},
    'Disneyworld - Florida': {'Ac': 'Theme Parks', 'Ag': 16, 'B':42000, 'T': 'Water Parks', 'R': 8.7},
    'Atlantis Resort': {'Ac': 'Theme Parks', 'Ag': 16, 'B':42000, 'T': 'Water Parks', 'R': 8.3},
    'Hawaii': {'Ac': 'Theme Parks', 'Ag': 16, 'B':42000, 'T': 'Water Parks', 'R': 8.2},
    'Universal Studios': {'Ac': 'Theme Parks', 'Ag': 16, 'B':50000, 'T': 'Movie Themed', 'R': 8.2},
    'Warner Bros. Movie World': {'Ac': 'Theme Parks', 'Ag': 16, 'B':50000, 'T': 'Movie Themed', 'R': 8.1},
    'Walt Disney Studio Park': {'Ac': 'Theme Parks', 'Ag': 16, 'B':50000, 'T': 'Movie Themed', 'R': 8.1},
    'Meghalaya': {'Ac': 'Close to Nature', 'Ag': 16, 'B':33000, 'T': 'Nature Walks', 'R': 8.0},
    'Sikkim': {'Ac': 'Close to Nature', 'Ag': 16, 'B':40000, 'T': 'Nature Walks', 'R': 8.6},
    'Jim Corbett': {'Ac': 'Close to Nature', 'Ag': 16, 'B':10000, 'T': 'National Parks', 'R': 8.7},
    'Kaziranga': {'Ac': 'Close to Nature', 'Ag': 16, 'B':26000, 'T': 'National Parks', 'R': 8.7},
    'Ranthambore': {'Ac': 'Close to Nature', 'Ag': 16, 'B':32000, 'T': 'National Parks', 'R': 8.6},
    'Jammu': {'Ac': 'Close to Nature', 'Ag': 16, 'B':45000, 'T': 'Trekking', 'R': 7.9},
    'Aravali': {'Ac': 'Close to Nature', 'Ag': 16, 'B':45000, 'T': 'Trekking', 'R': 7.1},
    'Leh': {'Ac': 'Adventure Sports', 'Ag': 16, 'B':28000, 'T': 'Land Sports', 'R': 8.9},
    'Ladakh': {'Ac': 'Adventure Sports', 'Ag': 16, 'B':28000, 'T': 'Land Sports', 'R': 8.8},
    'Kasauli': {'Ac': 'Adventure Sports', 'Ag': 16, 'B':28000, 'T': 'Land Sports', 'R': 7.2},
    'Lakshadweep': {'Ac': 'Adventure Sports', 'Ag': 16, 'B':29000, 'T': 'Water Sports', 'R': 8.2},
    'Pondicherry': {'Ac': 'Adventure Sports', 'Ag': 16, 'B':22000, 'T': 'Water Sports', 'R': 8.3},
    'Chennai': {'Ac': 'Adventure Sports', 'Ag': 16, 'B':18000, 'T': 'Air Sports', 'R': 7.9},
    'Mysore': {'Ac': 'Adventure Sports', 'Ag': 16, 'B':12000, 'T': 'Air Sports', 'R': 6.9},
    'Neemrana': {'Ac': 'Adventure Sports', 'Ag': 16, 'B':9000, 'T': 'Air Sports', 'R': 7.3},
}


def get_recommendations_weather(age, weather, trip_type, budget):
    recommendations = []
    for location, attributes in locations_weather_based.items():
        if attributes['W'] == weather and attributes['T'] == trip_type and attributes['B'] <= budget:
            recommendations.append((location, attributes['R']))
    return recommendations


def get_recommendations_activities(activity_broad, age, activity_type, budget):
    recommendations = []
    for location, attributes in locations_activity_based.items():
        if(attributes['Ac'] == activity_broad and attributes['T'] == activity_type and attributes['B'] <= budget):
            recommendations.append((location, attributes['R']))
    return recommendations


def add_new_location():
    place_name = input("Enter name of new place: ")
    age = int(input(f"Enter suited age for {place_name}: "))

    if(age>16):
        new_location_weather = input("Enter the weather type (summer/winter/tropical): ")
        new_location_type = input("Enter the trip type (getaway/activities): ")
        new_location_budget = int(input("Enter the estimated budget (max 100000): "))
        new_location_rating = float(input("Enter the rating (0 to 10): "))

        locations_weather_based[place_name] = {
            'W': new_location_weather,
            'A': age,
            'T': new_location_type,
            'B': new_location_budget,
            'R': new_location_rating
        }

    else:
        new_location = input("Enter the name of the new location: ")
        new_location_activity = input("Enter the activity type (Theme Parks/Close to Nature/Adventure Sports): ")
        new_location_age = int(input("Enter the minimum age requirement: "))
        new_location_budget = int(input("Enter the estimated budget (max 100000): "))

        invalid = 0
        while(invalid<2):
            if new_location_activity == 'Theme Parks':
                new_location_type = input("Enter the theme park type (Amusement Parks/Water Parks/Movie Themed): ")
            elif new_location_activity == 'Close to Nature':
                new_location_type = input("Enter the nature-based activity type (Nature Walks/National Parks/Trekking): ")
            elif new_location_activity == 'Adventure Sports':
                new_location_type = input("Enter the adventure sports type (Land Sports/Water Sports/Air Sports): ")
            else:
                invalid += 1
                if(invalid==2):
                    print("Too many incorrect values, aborting...")
                    return
                else:
                    print("Invalid activity type.")
                continue
            invalid = 1000000

        new_location_rating = float(input("Enter the rating: "))

        locations_activity_based[new_location] = {
            'Ac': new_location_activity,
            'Ag': new_location_age,
            'B': new_location_budget,
            'T': new_location_type,
            'R': round(new_location_rating, 1)
        }



if __name__ == "__main__":
    name = input('Enter your name: ')
    print(f'\nHello {name}')
    print('Welcome to the Travel Recommendation System\n')

    age = int(input('What is your age: '))
    
    if age > 16:
        print('\nWhat weather choice would you like?')
        print('1. summer')
        print('2. winter')
        print('3. tropical')
        weather = input()
        
        if weather == 'summer' or weather == 'winter':
            print('\nWhat kind of a trip would you like?')
            print('1. getaway')
            print('2. activities')
            trip_type = input()

            print('\nEnter an estimated budget (max = 100000): ')
            budget = int(input())

            places = get_recommendations_weather(age, weather, trip_type, budget)
            
            if(len(places)==0):
                print('Sorry, we couldn\'t find any locations suited to your needs. Would you like to add a new location? (Yes/No)')
                ans = input()

                if(ans.lower()=='yes'):
                    add_new_location()
            
            else:
                print('Here are some places you can visit:')
                for item in places:
                    print(item[0] + ": " + str(item[1]))
                    
        else:
            print('\nWhat kind of a location would you prefer?')
            print('1. coastal')
            print('2. rainforest')
            location_type = input()

            print('\nEnter an estimated budget (max = 100000): ')
            budget = int(input())

            places = get_recommendations_weather(age, weather, location_type, budget)
            
            if(len(places)==0):
                print('Sorry, we couldn\'t find any locations suited to your needs. Would you like to add a new location? (Yes/No)')
                ans = input()

                if(ans.lower()=='yes'):
                    add_new_location()
            
            else:
                print('Here are some places you can visit:')
                for item in places:
                    print(item[0] + ": " + str(item[1]))
    
    elif age <= 16:
        print('\nWhat kind of activities would you like on your trip?')
        print('1. Theme Parks')
        print('2. Close to Nature')
        print('3. Adventure Sports')
        activity_broad = input()
        
        if activity_broad == 'Theme Parks':
            print('\nWhat kind do you prefer the most?')
            print('1. Amusement Parks')
            print('2. Water Parks')
            print('3. Movie Themed')
            activity_type = input()

        elif activity_broad == 'Close to Nature':
            print('\nWhich would you prefer the most?')
            print('1. Nature Walks')
            print('2. National Parks')
            print('3. Trekking')
            activity_type = input()

        elif activity_broad == 'Adventure Sports':
            print('\nWhat Type of sports do you like the most?')
            print('1. Land Sports')
            print('2. Water Sports')
            print('3. Air Sports')
            activity_type = input()

        print('\nEnter an estimated budget (max = 100000): ')
        budget = int(input())
        
        places = get_recommendations_activities(activity_broad, age, activity_type, budget)
        
        if(len(places)==0):
            print('Sorry, we couldn\'t find any locations suited to your needs. Would you like to add a new location? (Yes/No)')
            ans = input()

            if(ans.lower()=='yes'):
                add_new_location()
        
        else:
            print('Here are some places you can visit:')
            for item in places:
                print(item[0] + ": " + str(item[1]))
