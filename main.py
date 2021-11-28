import os.path
import time
import constants
import requests
import io
from PIL import Image

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

wd = webdriver.Chrome(constants.CHROME_DRIVER_PATH);

# Initialize web driver and go to google translate
def init_webdriver(driver):
    driver.maximize_window()
    driver.get(constants.URL)

    # Close 'I agree' pop-up
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, constants.I_AGREE_POP_UP))).click()
        closedPopUp1 = True
    except:
        print("I agree pop-up failed")


def readCommonWords():
    commonWords = []
    with open(constants.MOST_COMMON_WORDS) as file:
        commonWords = file.readlines()

    return commonWords


def translateWords(commonWordsList, driver):
    translatedWords = []

    for word in commonWordsList:
        # Tap on source language text area
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, constants.SOURCE_LANGUAGE_TEXT_AREA))).click()

        # Enter the word
        ActionChains(driver).send_keys(word).perform()

        # Append the translated word to the list
        word_translated =  WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.TARGET_LANGUAGE_TEXT_AREA))).text
        translatedWords.append(word_translated)

        # Write to the output file
        with open(constants.OUTPUT_DIR_PATH + "out.txt", "a", encoding="utf-8") as file:
            file.write(word.rstrip() + "###" + word_translated + "\n")

        # Clear the source language text area (press X)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, constants.CLEAR_SOURCE_LANGUAGE_TEXT_AREA))).click()

def main():
    init_webdriver(wd)
    commonWordsList = readCommonWords()
    translatedWords = translateWords(commonWordsList, wd)


if __name__ == "__main__":
    main()
