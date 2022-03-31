from nltk import *
import re

from google_images_search import GoogleImagesSearch
gis = GoogleImagesSearch('AIzaSyAShNoLk0FK63xjSpKpPsMAH_LTWUXwoas', 'e7d15d193639f2144', validate_images=True)

# Define the search parameters


def getImage(imageName):

    print("Searching for ", imageName)
    searchParams= {
    'q': imageName,
    'num': 1,
    'fileType': 'jpg|jpeg|png|tiff'
    }

    gis.search(search_params=searchParams, custom_image_name=imageName, path_to_dir='C:/Users/Anthony/Documents/GitHub/GAPT/GAPT Images/')

def main():
    parseScript("script.txt")

def parseScript(data):

    listOfContents = []
    listOfCharacters = []
    listOfActions = []
    listOfBackground = []

    background = '\((.*)\)'
    actions = '\{(.*)\}'
    characters = '\[(.*)\]'
    title = ""
    
    reBackgrounds = re.compile(background)
    reActions = re.compile(actions)
    reCharacters = re.compile(characters)
    
    with open(data, "r") as script:
        for line in script:
            content = line.split('\n')
            while '' in content:
                content.remove('')
                
            if len(content) >= 1:
                listOfContents.append(content)

        #print(listOfContents)
    
    title = listOfContents[0]
    for cl in listOfContents:
        for line in cl:
            if reBackgrounds.match(line):
                listOfBackground.append(re.search(reBackgrounds, line).group(1)) 
            elif reActions.match(line):
                listOfActions.append(re.search(reActions, line).group(1))
            elif reCharacters.match(line):
                listOfCharacters.append(re.match(reCharacters, line).group(1))
            else:
                pass
    
    listOfCharacters = list(set(listOfCharacters))

    print("Title: ", title)
    print("List of Actions: ", listOfActions) 
    print("List of Backgrounds: ", listOfBackground)
    print("List of Characters: ", listOfCharacters)

    for bg in listOfBackground:
        getImage(bg)

main()    
