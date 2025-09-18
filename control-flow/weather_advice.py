# Prompt the user for weather input
weather_condition = input("What's the weather like today? (sunny/rainy/cold): ")

# Provide clothing recommendations based on the input
if weather_condition == "sunny":
    print("wear a t-shirt and sunglasses")
elif weather_condition == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_condition == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")