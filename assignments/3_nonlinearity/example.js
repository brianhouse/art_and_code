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

// Let's run the "lobby" function to start off
lobby()

// Here's where we define what happens in the lobby
function lobby() {

	// Start by describing what's going on
	print("You are in the lobby of the Art Department. A stairway leads upward, and a passage continues to the east. What do you want to do?")

	// Get a response from the interactor
	let response = prompt()

	// Depending on the response, call another function
	if (response.includes("passage")) {
		digitalMediaRoom()	// go to digitalMediaRoom
	} else if (response.includes("east")) {
		digitalMediaRoom()	// go to digitalMediaRoom
	} else if (response.includes("stairway")) {
		paintingRoom()	// go to paintingRoom
	} else if (response.includes("up")) {
		paintingRoom()	// go to paintingRoom
	} else {
		print("I don't understand.")
		// If the interactor types something unexpected, repeat the code for "lobby" in order to re-ask the question
		lobby()
	}

}


function digitalMediaRoom() {
	print("You are in the Digital Media Studio. A door leads to a passage to the west. A computer sits on a table. What do you want to do?")

	// Get a response from the interactor
	let response = prompt()

	// Depending on the response, call another function
	if (response.includes("passage")) {
		lobby()	// return to the lobby
	} else if (response.includes("west")) {
		lobby()	// return to the lobby
	} else if (response.includes("door")) {
		lobby()	// return to the lobby
	} else if (response.includes("computer")) {
		usingComputer()	// run the usingComputer function
	} else {
		print("I don't understand.")
		digitalMediaRoom()
	}


}


function paintingRoom() {
	print("You are in the Painting Studio.")

	// more code goes here...

}

function usingComputer() {
	print("You sit down at the computer and begin to type...")

	// more code goes here...

}
