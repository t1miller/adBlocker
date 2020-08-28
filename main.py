import requests
import webbrowser
import os
from bs4 import BeautifulSoup


def make_request(url):
    page = requests.get(url)

    # todo filter
    soup = BeautifulSoup(page.content, 'html.parser')
    p_tags = soup.find_all('p')
    for tag in p_tags:
        tag.string = tag.get_text() + ' TRENT AND NIMA WERE HERE.'

    img_tags = soup.find_all('img')
    for tag in img_tags:
        tag['src'] = os.getcwd() + "/lamma.jpg"

    # save file
    saved_file_name = 'sanitized_' + url.split(".")[1] + '.html'
    file_url = "file:" + os.getcwd() + "/" + saved_file_name
    print('saving file to: ', saved_file_name)
    with open(saved_file_name, 'w', encoding='utf-8') as file:
        file.write(str(soup))

    # open saved file in web browser
    webbrowser.open(file_url, new=2)


make_request('https://www.google.com')
make_request('http://www.trentrobison.com')

