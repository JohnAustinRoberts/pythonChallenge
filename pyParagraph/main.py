# In this challenge, you get to play the role of chief linguist at a local learning academy. As chief linguist, you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a fairly simple set of metrics for assessing complexity.

# Your task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:

# Import a text file filled with a paragraph of your choosing.
file = "raw_data/paragraph_1.txt"

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

	#print(text)

	# Store all of the text inside a variable called "lines"
	lines = text.read()

	#print(lines)
# Assess the passage for each of the following:

# Instantiate Create Variables
wordList = []
wordCount = 0
sentList = []
sentCount = 0
lettAvg = 0
avgSentLen = 0
#Print Title
print("Paragraph Analysis")
print("-----------------------------")
# Approximate word count
#Split the content of the string lines on the spaces, appending it to  pgList.
wordList = lines.split(" ")
wordCount = str(len(wordList))
print("Number of Words: " + wordCount + " Words.")
print("-----------------------------")
# Approximate sentence count
sentList = lines.split(".")
sentCount = str(len(sentList))
print("Number of Sentences: " + sentCount + " Sentences.")
print("-----------------------------")
# Approximate letter count (per word)
spaceless = ''.join(e for e in lines if e.isalnum())
lettAvg = str(int(int(len(spaceless)) / int(len(wordList))))
print("Average Letter Count: " + lettAvg + " Per Word.")
print("-----------------------------")
# Average sentence length (in words)
avgSentLen = str(int(int(wordCount) / int(len(sentList))))
print("Average Sentence Length: " + avgSentLen + " Words.")
# As an example, this passage:

# “Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident - a blot of black upon a world of crimson and gold.”

# ...would yield these results:

# Paragraph Analysis
# -----------------
# Approximate Word Count: 122
# Approximate Sentence Count: 5
# Average Letter Count: 4.56557377049
# Average Sentence Length: 24.4
# Special Hint: You may find this code snippet helpful when determining sentence length (look into regular expressions if interested in learning more):










