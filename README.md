# Mini-Project-1

Snake Water Gun - Python Game (Core Logic)

This is the backend logic for a Snake Water Gun game—built in Python, ready to plug into a GUI (like Tkinter, PyQt, or any other front-end).

Game Rules
	•	Snake drinks Water → Snake wins
	•	Water douses Gun → Water wins
	•	Gun kills Snake → Gun wins
	•	Same move? Draw

Input & Output

This version expects the user’s input as a string:
	•	"s" for Snake
	•	"w" for Water
	•	"g" for Gun

The computer makes a random choice. The logic compares both and returns the result.

Core Logic
	•	Internally maps:
	•	1 → Snake
	•	-1 → Water
	•	0 → Gun
	•	Runs comparison rules and determines the winner
	•	Prints outcome (for now), but you can replace print() with GUI updates or return values

Example Usage (Pseudocode)
result = get_result(user_choice)  # 's', 'w', or 'g'
# Now use result["outcome"], result["user"], result["computer"]
# to display in your GUI

What You Can Build On Top
	•	Tkinter or PyQt interface
	•	Buttons for Snake, Water, Gun
	•	Display computer’s choice and outcome with icons or colors
	•	Add score tracking, animations, or sounds
