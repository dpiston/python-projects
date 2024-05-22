# A dictionary of constants, by planet name and gravity ratio compared to Earth
PLANET_GRAVITY = {'Mercury' : 0.38, 'Venus' : 0.91, 'Earth' : 1.0, 'Mars' : 0.38, 'Jupiter' : 2.36, 'Saturn' : 0.92, 'Uranus' : 0.89, 'Neptune' : 1.12}

# The conversion, outputs what your weight would be on every other planet
def weightConverter(wgt, planet):
	# Prints the original weight and planet entered
	print(f"Your weight is {wgt} lbs on {planet}.")
	# Converts the users weight to a float and it's earth equivilent for calculations
	wgt = float(wgt) / PLANET_GRAVITY[planet]
	# Iterating through our gravity dictionry, outputting the planet and user weight there
	for key, value in PLANET_GRAVITY.items():
		# Skip the original planet since it's our first output
		if key == planet:
			continue
		print(f"If you were on {key} you would weigh {value * wgt:.2f} lbs.")



if __name__ == "__main__":
	while(True):
		userWeight = input("Please enter your weight: ")

		# Ensuring the user inputs a number
		try:
			userWeight = float(userWeight)
			print()
			break
		# Clear the screen and ask for input again if a number was not provided
		except:
			print("\033[2J\033[1;1H")
			print("Invalid entry, please enter a number")
			print()

	while(True):
		print("What planet are you on?")
		# Saves all the key values in the list for looped print out of options
		keys = list(PLANET_GRAVITY.keys())
		for i in range(len(keys)):
			print(f"{i}) {keys[i]}")
		choice = input("Enter selection: ")

		# Ensuring the user inputs a number
		try:
			choice = int(choice)
			# Also making sure the number is valid
			if choice > len(keys) - 1:
				print("\033[2J\033[1;1H")
				print(f"Please enter a number between 0 and {len(keys) - 1}")
				print()
			else:
				break
		# Clear the screen and ask for input again if a number was not provided
		except:
			print("\033[2J\033[1;1H")
			print("Invalid entry, please enter a number")
			print()

	print()
	home_planet = keys[int(choice)]
	weightConverter(userWeight, home_planet)
