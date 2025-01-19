# Day 1/100
# Create a program that ask to an user about his/her city and his/her pet name 
# Then, it has to returns a rock band proposal concatenating both text inputs

def band_name_generator(city:str, pet_name:str) -> str:
    '''Function that generates a band name based on a city and an animal'''

    print(f'Your band name could be {city.capitalize()} {pet_name.capitalize()}!!🤘🎸')


if __name__ == "__main__":
    print('Welcome to the band Name Generator\n')
    
    city_in = input("-What's the name of the city you grew up in?: ")
    pet_name_in = input("-What's your pet's name?: ")
    print('\n')

    band_name_generator(city=city_in, pet_name=pet_name_in)