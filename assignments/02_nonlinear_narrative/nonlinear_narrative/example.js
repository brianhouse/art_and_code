prompt = require('prompt-sync')()
print = require('print')()

print("What is your name?")
name = prompt()

print("Hi, " + name + "!")
intro()


function intro() {

	print("You are in the lobby of the Art Department. A stairway leads upward, and a passage continues to the east. What do you want to do?")
	response = prompt()

	if (response.includes("passage") || response.includes("east")) {
		digitalMedia()
	} else if (response.includes("stairway") || response.includes("up")) {
		painting()
	} else {
		print("I don't understand.")
		intro()
	}

}


function digitalMedia() {
	print("You are in the Digital Media Studio.")
}


function painting() {
	print("You are in the Painting Studio.")
}
