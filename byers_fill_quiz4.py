#define input spaces

test_blanks = ['__1__', '__2__', '__3__', '__4__']


#define questions for difficulties easy, medium, hard.

easy_quest = "In the Lord of the Rings trilogy. We know that the main character's first name is __1__ Baggins and he was accompanied by his hobit friends (first names not nicknames) __2__ Gamgee, __3__ Brandybuck, __4__ Took."

medium_quest = "In the Lord of the Rings trilogy. The premise of the story is that Frodo __1__ needed to throw a __2__ into the fire of Mount __3__ to save Middle __4__."

hard_quest = "The Lord of the Rings trilogy was written by J.R.R. __1__ and was first published in the year __2__. The book was later made into a film produced by New Line Cinema and was directed by Peter __3__. That series was first released in the year __4__ although there were many adaptions created in previous years."


#define answeres for difficulties easy, medium, hard.

easy_ans = ['Frodo', 'Samwise', 'Meriodoc', 'Peregrin']

medium_ans = ['Baggins', 'ring', 'Doom', 'Earth']

hard_ans = ['Tolkien', '1954', 'Jackson', '2001']




def end():
	'''The input of this comes from quest and the output is the statement below.'''
	print "\n" + "You've completed the quiz! Gandolf would be proud!" + "\n" + "\n" "End Game"


def blank_pos(word, blank):
	'''In the function blank_pos with the inputs being word and blank, we are trying to match the variable blank to the blanks in d_quest. 
	If blank matches the position in word it will return that position(associated blank) otherwise it will return None
	which will be appended to the blank string called replaced.'''
	if blank in word:
		return blank
	return None


def a_replacer(d_quest, answer, blank):
	'''When function quest has checked the answer it is requested to print the return value of this function. This was based on the madlibs function in Stage 2 course materials.
	The inputs to this function are d_quest, answer and the blank variable I assigned in the last function. What we are trying to do here is replace the correct d_quest blank with the associated answer 
	and the way we do that is by spliting d_quest into a list, find the pos that matches blank, and replace it with answer. Then we rejoin the list to be printed back to the user as the output.'''
	replaced = [] #this remains empty because we will be appended list items in d_quest + answer to it later. 
	 #the reason why there is a counter is because when d_quest is changed we need to prompt the function to look for the next test_blank.
	d_quest = d_quest.split() #this splits d_quest into a list. 
	for word in d_quest: #We assign every list item the variable word. 
		replacement = blank_pos(word, blank) #in the for loop we assign a new variable called replacement but it is actually for a new function. Please go to blank_pos for more. 
		if replacement != None:
			word = word.replace(replacement, answer)
			replaced.append(word)
		else:
			replaced.append(word)
	replaced = " ".join(replaced)
	return replaced  #I am trying to figure out how to assign this to d_quest so that the filled answer input stays put. 



def quest(d_quest, d_ans, test_blanks):
	'''This is were the user is able to put in his/her input and have that answer be verified. The inputs are d_quest, d_ans, test_blanks plus the raw_input which is assigned the variable answer. 
	If answer equals the variable d_ans(the associated answer depending on the depending on the difficulty requested), the function will print the output, 
	"That is correct! It is d_ans[q_count](q_count is a counter I use to pull the correct item from d_ans)!" From there I have have to find the correct position in d_quest and fill it with the user_input.
	So I assign the variable blank to test_blanks[q_count] and then the most importantat part; d_quest to a_replacer(see a_replacer for more details) then print d_quest. Frome there the q_count increases by 1
	and continues the loop. Once finished it refurns the end function.'''
	print d_quest + '\n'
	q_count = 0
	while q_count < len(test_blanks):
		print "What is " + test_blanks[q_count] + "?"
		answer = raw_input("")
		if answer == d_ans[q_count]:
			print "\n" + "That is correct! It is " + d_ans[q_count] + "!" + "\n" 
			blank = test_blanks[q_count]
			d_quest = a_replacer(d_quest, answer, blank) + '\n'
			print d_quest
			q_count += 1
			continue
		else:
			print "\n" + "That is incorrect! Try again." + "\n"
	return end() #This directs quest to go to def end. 


def game_difficulty():
	'''In this function, it begins by printing the below statement then asks the user to choose the desired difficulty. 
	Inputs are easy, medium, and hard. Once the input is set the output is the function quest() with it's parameters being 
	the associated questions, answers, and test_blanks.'''
	print "Game Settings"
	level = raw_input("Please choose a difficulty(easy, medium, hard): ")
	if level == 'easy':
		return quest(easy_quest, easy_ans, test_blanks)
	elif level == 'medium':
		return quest(medium_quest, medium_ans, test_blanks)
	elif level == 'hard':
		return quest(hard_quest, hard_ans, test_blanks)
	else:
		print "\n" + "Gandolf does not accept that entry. Please try again." + "\n"
		return game_difficulty() #this line points back to the beginning of the def if the user inputs something other than the options provided. 


def start_game():
	'''This function starts the game by printing the below statment. Then once the statement is printed, 
	the function starts the next called game_difficulty().'''
	print "\n" + "Welcome to the Lord of the Rings Quiz! \n"
	game_difficulty() #this directs the interpreter to go to the next def. 


start_game()