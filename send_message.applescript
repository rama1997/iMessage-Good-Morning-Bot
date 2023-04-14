on run {targetBuddyPhone, targetMessage}
	tell application "Messages"
		set targetService to 1st account whose service type = iMessage
		set targetBuddy to participant targetBuddyPhone of targetService
		send targetMessage to targetBuddy
	end tell
end run