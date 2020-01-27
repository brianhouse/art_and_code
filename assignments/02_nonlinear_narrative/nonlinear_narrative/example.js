// fyi, any line that starts with // is a "comment" and won't affect the program
// these next two lines are how we load the print and prompt functions
print = require('print')()
prompt = require('prompt-sync')()
//

// Let's ask the interactor their name and save it in a variable
print("What is your name?")
let name = prompt()

// Now we can print out that name in a middle of a sentence
// Notice the use of quotes to switch between static text and a variable
print("Hi, " + name + "!")

// Let's run the "intro" function
intro()

// Here's where we define what happens in the intro function
function intro() {

	// Start by describing what's going on
	print("You are in the lobby of the Art Department. A stairway leads upward, and a passage continues to the east. What do you want to do?")

	// Get a response from the interactor
	let response = prompt()

	// Depending on the response, call another function
	if (response.includes("passage")) {
		digitalMediaRoom()
	} else if (response.includes("east")) {
		digitalMediaRoom()
	} else if (response.includes("stairway")) {
		paintingRoom()
	} else if (response.includes("up")) {
		paintingRoom()
	} else {
		// If the interactor types something unexpected, repeat this function
		print("I don't understand.")
		intro()
	}

}


function digitalMediaRoom() {
	print("You are in the Digital Media Studio.")
}


function paintingRoom() {
	print("You are in the Painting Studio.")
}
