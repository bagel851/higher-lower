def play_higher_lower():
	playing_game = True
	while playing_game:
    
		score = 0
		still_guessing = True
		while still_guessing:

			clear()
			print(logo)
			
			person1 = assign()
			person2 = assign()
			
			if score > 0:
				person1 = person2
				person2 = assign()
				
				if person1 == person2:
					person2 = assign()
			
			print(f"Name: {person1['name']}, Desc: {person1['description']}")
			print(vs)
			print(f"Name: {person2['name']}, Desc: {person2['description']}")
			

			print("----------------------------------------------")
			print(f"Your current score is: {score}")
			print("----------------------------------------------")
			

			guess = input("Enter name of person with Higher Followers: ")
			
			if compare(person1, person2, guess):

				score += 1
			else:
				still_guessing = False
								
		play_again = input("Want to Play Again? (y/n): ").lower()
		
		if play_again == 'y':
			continue
		elif play_again == 'n':
			playing_game = False
			clear()
			print("Game Exited Successfully")
		else:
			playing_game = False
			print("Invalid Input Taken as no.")
