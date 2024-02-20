import json
import requests
from bs4 import BeautifulSoup #probably dont need this anymore bc json :)

def main():
	print()
	print()
	print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
	print("This is a CLI interface that pulls answered results from Stack Overflow given a user selected keyword")
	print("this has no api authentication so it is very limited")
	print("Please limit each search to one keyword")
	print("Type !quit to quit")
	print("Use a '-' instead of a space when typing multiple words")
	print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
	print()
	print()
	while True:
		print('Type the keyword you wish to search: ')
		j = input('> ')
		count = 1
		print("Display post body (y/n)")
		qq = input('> ')
		if j == ('!quit'):
			break
		else:

			so_page = requests.get(f'https://api.stackexchange.com/2.3/search?order=desc&sort=activity&intitle={j}&site=stackoverflow&filter=withbody')
			tj = json.loads(so_page.text)
			questions = tj["items"]

			for question in questions:
				title = question["title"]
				link = question["link"]
				qid = question["question_id"]
				viewcount = question["view_count"]
				answercount = question["answer_count"]
				body = question["body"]
				answered = question["is_answered"]
				if answered:
					a = requests.get(f'https://api.stackexchange.com/2.3/questions/{qid}/answers?order=desc&sort=activity&site=stackoverflow')
					answers_json = json.loads(a.text)
					answers = answers_json["items"]

					#output to user

					print('-------- Result #{} --------'.format(count))
					print('{}:\n{}'.format(question["owner"]["display_name"], title))
					print(link)
					print(f"Views: {viewcount}")
					print(f"Number of Answers: {answercount}")
					if qq == "y":
						print(f"Body: {body}")
					print()
					# setting a 15 result limit as to not abuse the api.
					if count == 15:
						break
					count += 1

if __name__ == "__main__":
	main()

#for later commit, changed max return from 50 to 15 bc api abuse is too real aparently
				
#Introduced a new feature to allow the user to view the post's text body aka the contents of the post, along with the link and other information
#embedded the entire code within a main() as that is better practice. 2/5/24
#added a method for typing multiple words as a "keyword" 2/13/24
