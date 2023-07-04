#!/usr/bin/python3

def My_GitHub_id(username, password):
    headers = {"Authentication": f"Token {access_token}"}
    url = "https://api.github.com/user"
    response = requests.get(url, headers=headers)
    code = response.status_code

    if code == 200:
        json_d = response.json()
        j_id = json_d.get('id')
        if j_id:
            print(j_id)
        else:
            print("None")
    else:
        print("None")

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    My_Github_id(username, password)
