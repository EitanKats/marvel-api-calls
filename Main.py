import requests
import json
import uuid
from marvelrequest import MarvelRequest

URL = "http://gateway.marvel.com/v1/public/comics"


def main():
    jump = 25
    for offset in xrange(10050, 42234, jump):
        marvel_request = MarvelRequest(URL, offset, jump);
        print(marvel_request)

        response = requests.get(marvel_request.url)
        if response.status_code == 409:
            print offset
            break

        write_to_file(response.json())


def write_to_file(data):
    with open("DataSets/" + str(uuid.uuid4()) + ".json", 'wb')as f_handler:
        f_handler.write(json.dumps(data))


if __name__ == '__main__':
    main()
