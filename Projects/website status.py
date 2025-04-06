import sys
import requests
from requests import Response

def get_response(url:str) -> Response:
    if url.startswith('https://') or url.startswith('http://'):
        return requests.get(url)
    else:
        url = 'https://'+url
        return requests.get(url)


def show_response_info(response: Response) -> None:
    lines = [
        f"Status: {response.status_code}",
        f"OK: {response.ok}",
        f"Links: {response.links}",
        f"Encoding: {response.encoding}",
        f"Is Redirect: {response.is_redirect}",
        f"Is Permanent Redirect: {response.is_permanent_redirect}"
    ]

    width = max(len(line) for line in lines) + 4
    print('+' + '-' * width + '+')
    for line in lines:
        print('| ' + line.ljust(width - 1) + '|')
    print('+' + '-' * width + '+')

def main() -> None:
    try:
        while True:
            print(' ' * 90)
            print(' '*25+'welcome to website status checker!!🌐'+' '*25)
            print('-'*90)
            url:str = input('🔎enter website url:')

            try:
                response = get_response(url)
                show_response_info(response)
            except requests.exceptions.RequestException as e:
                print(f'❌ Failed to get the status. Error: {e}')

            flag: str = input('do you want to continue(y/n):').strip().lower()
            if flag != 'y':
                print("bye-bye! 👋")
                sys.exit()

    except KeyboardInterrupt:
        print("bye-bye! 👋")
        sys.exit()

if __name__ == '__main__':
    main()