"""Practice with booleans and conditionals."""

# Write a function called check_first_leter
# that takes an input two strs: word and letter
# It should return "match!" if the first character of the word is letter
# Otherwise, it should return "no match!"


def check_first_letter(word: str, letter: str) -> str:
    """Check if the first character in word == letter."""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter("perfect", "p"))


def get_weather_report(weather: str) -> str:
    """Helpful took for weather."""
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


print(get_weather_report(weather="cold"))
get_weather_report(weather=input("What is the weather?"))
