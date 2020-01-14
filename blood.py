# This script predicts someone's blood type based on the number of blood transfusions from unmatched donors they received, as well as the distribution of blood types in the population.

print("------------------------------------------------------")
print("Welcome to the blood type predictor script!")

# Define the variable to contain info on desired population
population = None
# By default, the blood types are all equally likely
shareA = 0.25
shareB = 0.25
shareAB = 0.25
shareO = 0.25
# The number of transfusions
transfusions = "unknown"

while (population != "European") and (population != "Finnish") and (population != "Italian") and (population != "custom"):
	print("Which population are you interested in?")
	print("Write 'European', 'Finnish', 'Italian', or 'custom'")
	population = raw_input()

	if population == "European":
		# Distribution used in the Dracula paper
		shareA = 0.43
		shareB = 0.09
		shareAB = 0.04
		shareO = 0.44
	elif population == "Finnish":
		# Blood type distribution in Finland
		shareA = 0.42
		shareB = 0.17
		shareAB = 0.08
		shareO = 0.33
	elif population == "Italian":
		# Blood type distribution in Italy
		shareA = 0.42
		shareB = 0.09
		shareAB = 0.03
		shareO = 0.46
	elif population == "custom":
		# Use this to input any distribution you want to test
		shareA = 0.39
		shareB = 0.00
		shareAB = 0.00
		shareO = 0.61
	else:
		print("Sorry, I don't understand your input. You only have four options.")

while not isinstance(transfusions, int):
	print("How many random blood transfusions should we subject the hypothetical person to?")
	transfusions = input()

# This function takes the blood type distribution and the number of transfusions as a parameter and gives the probability distribution of each blood type given that the recipient survived the number of random transfusions from people in the same population
def distributionCalculator(shareA,shareB,shareAB,shareO,transfusions):
	# The probability distribution being calculated
	probabilities = []
	survivalChanceA = ((shareA + shareO) ** transfusions) * shareA
	survivalChanceB = ((shareB + shareO) ** transfusions) * shareB
	survivalChanceAB = ((shareA + shareB + shareAB + shareO) ** transfusions) * shareAB
	survivalChanceO = (shareO ** transfusions) * shareO
	totalSurvival = survivalChanceA + survivalChanceB + survivalChanceAB + survivalChanceO
	probabilities.append(survivalChanceA / totalSurvival)
	probabilities.append(survivalChanceB / totalSurvival)
	probabilities.append(survivalChanceAB / totalSurvival)
	probabilities.append(survivalChanceO / totalSurvival)
	return probabilities


finalProbabilities = distributionCalculator(shareA,shareB,shareAB,shareO,transfusions)
print("The " + str(population) + " population has the following blood type distribution:")
print("A: " + str(shareA))
print("B: " + str(shareB))
print("AB: " + str(shareAB))
print("O: " + str(shareO))
print("This distribution gives the probabilities of an individual having a particular blood type after surviving " + str(transfusions) + " random transfusions from people in the same population.") 
print("A: " + str(finalProbabilities[0]))
print("B: " + str(finalProbabilities[1]))
print("AB: " + str(finalProbabilities[2]))
print("O: " + str(finalProbabilities[3]))
print("Thank you for your interest in blood! Come again soon!")
print("------------------------------------------------------")