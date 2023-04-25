# a program to generate a band name
print("Welcome, answer the following questions to get a band name\n")

# ask the user for their city
city = input("which city are you from?\n")
    
# ask the user for their pet's name
pet = input("what's the name of your pet?\n")
    
# add the user's city and pet name to generate band name
band_name = f"{city} {pet}"
    
# print the band name to the user
print(f"Your band name is {band_name}")