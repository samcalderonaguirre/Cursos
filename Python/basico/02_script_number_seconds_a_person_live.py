# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years.
years = int(input('Enter number of years you have lived: -> '))
seconds = years * 365 * 24 * 60 * 60

print('You have lived for', seconds,'seconds')