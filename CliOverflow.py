import json
import requests
from bs4 import BeautifulSoup

print("This is a CLI interface that pulls answered results given a user selected keyword")
print("this has no api authentication so it is very limited")

while True:
    print('Type the Tag you wish to search: ')
    j = input('> ')
    count = 1

#   Getting the page and parse the json format of responses
    so_page = requests.get(f'https://api.stackexchange.com/2.3/search?order=desc&sort=activity&intitle={j}&site=stackoverflow&filter=withbody')
    tj = json.loads(so_page.text)
    questions = tj["items"]

    for question in questions:
        title = question["title"]
        link = question["link"]
        qid = question["question_id"]
        viewcount = question["view_count"]
        answercount = question["answer_count"]
    # body = question["body"] for later
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
            print()

            if count == 50:
                break
            count += 1