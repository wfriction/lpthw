# to include: lists, functions, modules

from sys import exit
from sys import argv
import platform

os = platform.system()

def call_os(os, q):
    if os == 'Linux':
        Linux(q)
    elif os == 'Darwin':
        Darwin(q)
    elif os == 'Windows':
        Windows(q)

def Linux(q):
    if q == 0:
        paper(os)
    elif q == 1:
        ios(os)

# def Windows():
# def Darwin():
def paper(os):
    paper = raw_input("Do you have no desire for backups or searchability? (y/n)")
    if paper == 'y':
        solution('Pen and paper')
    elif paper == 'n':
        call_os(os, 1)
    else:
        print "Please type y or n, without the quotes."
        paper()
def ios(os):
    ios = raw_input("Do you live in your iPhone and iPad? (y/n")
    if ios == 'y':
        research('ios')
    else:
        richtext()
def research(mobile):
    research = raw_input("Will you be using this for web research and notes?")
    if research == 'y' and mobile == 'ios':
        solution('100%. Evernote')
    elif research == 'y':
        solution('Evernote')
    elif research == 'n':
        richtext()
def richtext():
    richtext = raw_input("Would you rather write plaintext notes? (no images, tables, etc)")
    if richtext == 'y':
        dropbox = raw_input("Do you use dropbox and a favorite text-editor often?")
        if dropbox == 'y':
            solution('Dropbox combined with your favorite texteditor')
        elif dropbox == 'n':
            solution('Simplenote')
    elif richtext == 'n':
        hacker = raw_input("Answer yes if you are a hacker, a geek, and/or use emacs.")
        if hacker == 'y' or hacker == 'yes':
            solution('Emacs org-mode')
        else:
            solution('Springpad')

def solution(answer):
    print "Congratulations! %s is the best tool for you." % answer
    exit(0)

def check_platform():
    """Checks the platform using platform.system()"""
    platforms = ['Windows', 'Darwin', 'Linux']
    for os in platforms:
        if platform.system() == os:
            os = raw_input("Is %s your most used os? If not, enter what is." % os)
            os = platform.system()
            Linux(0)
#            os(0)

def start():
    script, player = argv
    
    print "Your player name will be %s." % player
    namecheck = raw_input("Is that correct? (y/n)")
    if namecheck == 'n':
        player = raw_input("Please enter a correct name")
    else:
        check_platform()

start()

# could add the indicated app to a list, then use count at the end to give best option
