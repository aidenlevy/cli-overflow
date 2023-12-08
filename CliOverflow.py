import json
import requests
from bs4 import BeautifulSoup
count = 1

print("This is a CLI interface that pulls answered results given a user selected keyword")
print("this has no api authentication so it is very limited")
while True:
    print('Type the Tag you wish to search: ')
    j = input('> ')

    # TODO: download the page using requests
    so_page = requests.get(f'https://api.stackexchange.com/2.3/search?order=desc&sort=activity&intitle={j}&site=stackoverflow&filter=withbody')
    tj = json.loads(so_page.text)
    questions = tj["items"]

    for question in questions:
        title = question["title"]
        link = question["link"]
        qid = question["question_id"]
        viewcount = question["view_count"]
        answercount = question["answer_count"]
    # body = question["body"]
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



    """soup = BeautifulSoup(so_page.content, 'html.parser')
    # StackOverflow website, top 45 unanswered questions with python tags
    # TODO: using BeautifulSoup, extract the following from the list of questions: title, user, text excerpt
    post_list = soup.find_all('div', 's-post-summary--content')
    for post in post_list:
        title = post.h3.a.text.strip()
        excerpt = post.div.text.strip()
        user_card = post.find('div', 's-user-card--info')
        user = user_card.div.a.text.strip()
        try:
            user = user_card.div.a.text.strip()
        except AttributeError:
            user = user_card.div.text.strip()"""
