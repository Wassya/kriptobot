import os
import os.path
import requests


def get_all_pages():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/90.0.4430.212 Safari/537.36 "
    }

    r = requests.get(
        url="https://docs.pancakeswap.finance", headers=headers)

    if not os.path.exists('parse'):
        os.mkdir('parse')

    with open('parse/page_1.html', "w") as file:
        file.write(r.text)


save_path = 'D:/прог/'


def main():
    get_all_pages()

    if __name__ == '__main__':
        main()

print(os.getcwd())
