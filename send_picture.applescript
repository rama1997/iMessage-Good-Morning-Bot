on run {targetBuddyPhone}
	tell application "Finder"
		# find the cat file
		set path_to_file to do shell script "find /Users/ray/Documents/CS/Scripts/iMessage-Good-Morning-Bot -mindepth 1 -name 'dog_picture*'"

		# set it as a POSIX file
		set my_file to (path_to_file as POSIX file)
	end tell
	
	tell application "Messages"
		set targetService to 1st account whose service type = iMessage
		set targetBuddy to participant targetBuddyPhone of targetService
		send my_file to targetBuddy
	end tell
end run