from time import sleep
import sys

# zde jsou funkce pro veškerý tisk ve hře. Udělal jsem to tak, aby se text
# tiskl hezky postupně jako v různých hrách a ne tak, jak je v pythonu zvykem
# tisknout. Rozdíl mezi nimi je jen ten, že print_dial má po svém dokončení
# kratičkou přestávku


def print_dial(str):
    for char in str:
        print(char, end="")
        sys.stdout.flush()
        sleep(0.03)
    sleep(1.25)
    print("")


def print_question(str):
    for char in str:
        print(char, end="")
        sys.stdout.flush()
        sleep(0.03)
    print("")
