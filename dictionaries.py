# a dictionary is a special structure in python which allow us to store informations in what are called key:value pairs
# you're gonna be using them a lot to store different types of data

# in a normal dictionary you would have a word and a definition attached to that word

# we'll create a little program that converts a 3digits month name into the full month name. jan => january

month_conversions = {
  "Jan": "January",
  "Feb": "February",
  "Mar": "March"
}

# get() returns the value for key if key is in the dictionary, else default.
print(month_conversions["Feb"])
print(month_conversions.get("Apr", "Not a valid key"))