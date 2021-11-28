##### USER INPUT #####
OUTPUT_DIR_PATH = "outDir/"

WORDS_TO_TRANSLATE = "words_to_translate.txt"

###### DRIVER #####
CHROME_DRIVER_PATH = "F:\PycharmProjects\Selenium\chromedriver.exe"

##### GOOGLE TRANSLATE URL #####
sl="en" # sourceLanguage
tl="ro" # targetLanguage
URL = "https://translate.google.ro/?hl=en&sl=" + sl + "&tl=" + tl + "&op=translate"


##### XPATHS #####
I_AGREE_POP_UP = "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div/div/button"

SOURCE_LANGUAGE_TEXT_AREA = "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea"
TARGET_LANGUAGE_TEXT_AREA = "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span"

CLEAR_SOURCE_LANGUAGE_TEXT_AREA = "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/div[1]/div/div/span/button/div[2]"
