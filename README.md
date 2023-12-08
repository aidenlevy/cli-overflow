# Cli-Overflow
### Created by Aiden Levy

## Purpose

This is a Python program that prompts you to enter a keyword. Following, the first 50 responses from Stack Overflow with answers related to the keyword will be porovided via terminal along with the responses' link, author, view count, and answer count. This currently uses a non authenticated API, meaning you may be limited in number of requests. I would like to thank @polambert for help with understanding and guiding me through implimentation of the Stack Overflow API into my code.   

## How to Use

To use, run Cli-Overflow.py. A terminal will open and will display a welcome message with a brief description of the file's function. The terminal will prompt the user for an input of a Keyword to be searched on Stack Overflow as a term within a response's title. For example, if I search "js" the returned responses will all contain "js" in their response title. The terminal will also number each response and display the view count followed by the number of answers.