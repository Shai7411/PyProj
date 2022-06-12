import platform
import os.path
import urllib3

class colors:
    NORMAL = '\033[0m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'

if platform.system().lower() == "windows" or platform.system().lower() == "linux":
    bool = False
    while True:
        if bool:
            break

        intro = input(
            f"\n{colors.BLUE}Select your option:\n1. Path Scanner\n9. About\n0. Exit\n\nOption: {colors.NORMAL}")
        if intro.isdigit():
            if int(intro) == 1:
                url = input(f"\n{colors.BLUE}Enter URL: {colors.NORMAL}")

                bool2 = False
                while True:
                    if bool2:
                        break

                    wordlist_path = input(f"{colors.BLUE}Enter Wordlist: {colors.NORMAL}")

                    os.path.exists(wordlist_path)
                    if os.path.exists(wordlist_path):
                        if platform.system().lower() == "linux":
                            wordlist = []
                            with open(wordlist_path, "r") as file:
                                for j in file.readlines():
                                    data = "".join(j.split("\n"))
                                    wordlist.append(data)

                                http = urllib3.PoolManager()
                                request = http.request("GET", url)

                                if request.status == 200:
                                    print(
                                        f"{colors.GREEN}You requested to scan {url}, Request Status: {request.status}.{colors.NORMAL}\n")

                                    counter = 1
                                    xlist = []
                                    for i in wordlist:
                                        request = http.request("GET", f"{url}/{i}")
                                        if request.status == 200:
                                            print(
                                                f"[{counter}] | {url}/{i} | {colors.GREEN}Page Found.{colors.NORMAL}")
                                            xlist.append(f"[{counter}] | {url}/{i} | Page Found.")
                                        elif request.status == 404:
                                            print(
                                                f"[{counter}] | {url}/{i} | {colors.RED}Page Not Found.{colors.NORMAL}")
                                            xlist.append(f"[{counter}] | {url}/{i} | Page Not Found.")
                                        counter += 1

                                    bool = True
                                    bool2 = True
                                    while True:
                                        output = input(
                                            f"\n{colors.BLUE}Would you like to save the result into a text file (y/n) ? {colors.NORMAL}").lower()
                                        if output == "y".lower():
                                            output_path = input(
                                                f"{colors.BLUE}Enter a path where you like to save the file: {colors.NORMAL}")
                                            for i in xlist:
                                                with open(output_path, "a") as file:
                                                    file.write(f"{i}\n")
                                            break
                                        elif output == "n".lower():
                                            break
                                elif request.status > 400 or request.status < 499:
                                    print(
                                        f"{colors.YELLOW}You requested to scan {url}, Request Status: {request.status}.{colors.NORMAL}\n")
                                    break
                                elif request.status > 500 or request.status < 599:
                                    print(
                                        f"{colors.YELLOW}You requested to scan {url}, Request Status: {request.status}.{colors.NORMAL}\n")
                                    break
                        elif platform.system().lower() == "windows":
                            if wordlist_path.endswith('.txt'):
                                wordlist = []
                                with open(wordlist_path, "r") as file:
                                    for j in file.readlines():
                                        data = "".join(j.split("\n"))
                                        wordlist.append(data)

                                    http = urllib3.PoolManager()
                                    request = http.request("GET", url)

                                    if request.status == 200:
                                        print(
                                            f"{colors.GREEN}You requested to scan {url}, Request Status: {request.status}.{colors.NORMAL}\n")

                                        counter = 1
                                        xlist = []
                                        for i in wordlist:
                                            request = http.request("GET", f"{url}/{i}")
                                            if request.status == 200:
                                                print(f"[{counter}] | {url}/{i} | {colors.GREEN}Page Found.{colors.NORMAL}")
                                                xlist.append(f"[{counter}] | {url}/{i} | Page Found.")
                                            elif request.status == 404:
                                                print(
                                                    f"[{counter}] | {url}/{i} | {colors.RED}Page Not Found.{colors.NORMAL}")
                                                xlist.append(f"[{counter}] | {url}/{i} | Page Not Found.")
                                            counter += 1

                                        bool = True
                                        bool2 = True
                                        while True:
                                            output = input(
                                                f"\n{colors.BLUE}Would you like to save the result into a text file (y/n) ? {colors.NORMAL}").lower()
                                            if output == "y".lower():
                                                output_path = input(
                                                    f"{colors.BLUE}Enter a path where you like to save the file: {colors.NORMAL}")
                                                for i in xlist:
                                                    with open(output_path, "a") as file:
                                                        file.write(f"{i}\n")
                                                break
                                            elif output == "n".lower():
                                                break
                                    elif request.status > 400 or request.status < 499:
                                        print(
                                            f"{colors.YELLOW}You requested to scan {url}, Request Status: {request.status}.{colors.NORMAL}\n")
                                        break
                                    elif request.status > 500 or request.status < 599:
                                        print(
                                            f"{colors.YELLOW}You requested to scan {url}, Request Status: {request.status}.{colors.NORMAL}\n")
                                        break
                            else:
                                wordlist_path_splited = str(wordlist_path).split("\\")
                                print(
                                    f"{colors.YELLOW}Your file [{wordlist_path_splited[-1]}] is not a text (.txt) file.{colors.NORMAL}")
                    else:
                        print(f"{colors.YELLOW}Your path [{wordlist_path}] does not exist.{colors.NORMAL}")
            elif int(intro) == 9:
                print(
                    f"\n{colors.BLUE}# =================================================== #\nThis script is coded by Shai Halfon in Python language.\n# =================================================== #\n{colors.NORMAL}\n{colors.YELLOW}! ===== Disclaimer:\nThis script is coded for Educational Purposes Only, and I'm not responsible for anything that other people use (ex. Criminal Activities & Cyber Crimes).{colors.NORMAL}")
            elif int(intro) == 0:
                break
            else:
                print(f"{colors.YELLOW}Your choice [{intro}] option does not exist.{colors.NORMAL}\n")
        else:
            print(f"{colors.YELLOW}Your choice [{intro}] option should be digits only.{colors.NORMAL}\n")
else:
    print(f"{colors.YELLOW}This script is for Windows / Linux Operation Systems only.{colors.NORMAL}")
