
# Librairies import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
import time
import unicodedata


#Import for driver 
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from bs4 import BeautifulSoup

# Driver initialization
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

def clean_string(string):
    
    # Remplacer les lettres accentuées par des lettres sans accent
    string = ''.join(unicodedata.normalize('NFD', char)[0] for char in string)
    
    #Supprimer les titres courants de la chaîne de caractères
    common_titles = ["M.", "Mme", "Monsieur", "Madame", "Prof"]
    string = ' '.join(word for word in string.split() if word not in common_titles) 
    
    # Mettre en minuscules
    string = string.lower()
    
    #Supprimer les caractères spéciaux sauf le tiret
    string = re.sub(r'[^a-zA-Z \-]', '', string)
       
    # Supprimer les espaces, les guillemets doubles au début et à la fin de la chaîne
    string = string.strip().replace('"', '')
    
    # Consolider l'espace blanc entre les mots
    string = ' '.join(string.split())
    
    return string

# Login to Linkedin
def login(mail, password):
    
    driver.get("https://www.linkedin.com/login")
    time.sleep(1)

    eml = driver.find_element(by=By.ID, value="username")
    eml.send_keys(mail)
    
    passwd = driver.find_element(by=By.ID, value="password")
    passwd.send_keys(password)
    
    loginbutton = driver.find_element(by=By.XPATH, value="//*[@id=\"organic-div\"]/form/div[3]/button")
    loginbutton.click()
    
    time.sleep(3)
    
# Retourne les personnes qui ont le poste recherché 
def getPerson(poste):
     
    driver.get("https://www.linkedin.com/search/results/people/?keywords=" + poste + "&origin=SWITCH_SEARCH_VERTICAL&sid=NqB")
      
    time.sleep(1)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    source = BeautifulSoup(driver.page_source, 'html.parser')
    
    profile_title = source.find_all(class_="entity-result__primary-subtitle t-14 t-black t-normal")
    profile_name = source.find_all(class_="t-roman t-sans")

    print("Voici des postes qui ont un poste similaires à " + poste)
    for name_profile in profile_name:
        for title_profile in profile_title:
            print("Nom : " + name_profile.text.strip() + " Poste : " + title_profile.text.strip())
     
    print('data updated')
   
    
    return name_profile, title_profile

# Retourne les employes qui ont un poste dans une entreprise donnée
def getCompanyEmployee(companyName, poste):
    
    time.sleep(1)
    
    driver.get("https://www.linkedin.com/company/" + companyName + "/people/?keywords=" + poste + "")
       
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
           
    source = BeautifulSoup(driver.page_source, 'html.parser')
    
    profile_name_C = source.find_all(class_="artdeco-entity-lockup__title ember-view")
    
    profile_post = source.find_all(class_="ember-view lt-line-clamp lt-line-clamp--multi-line")
    
    print("Voici les employés de l'entreprise " + companyName + " qui ont un poste similaire à " + poste)
    
    for name_profile_C in profile_name_C:
        for post_profile in profile_post:
            print("Nom : " + name_profile_C.text.strip() + " Poste : " + post_profile.text.strip())
     
    print('data updated')

if __name__ == "__main__":
    
   
    print('Pour faire des recherches sur LinkedIn, vous devez utiliser votre compte.')
    
    mail = input("Entrez votre mail : ")
    password = input("Entrez votre mot de passe : ")

    login(mail, password)
    
    poste = input("Entrez un nom de poste : ")
    poste = clean_string(poste)
    
    company = input("Entrez le nom d'une entreprise : ")
    company = clean_string(company)
    
    print("Liste des personnes ayant un poste similaire au poste recherché") 
    getPerson(poste)
    
    print(" 2) Recuperer les infos des employes d'une entreprise ayant un poste similaires au poste recherché ")
    getCompanyEmployee(company, poste)
     
    time.sleep(1)
    
    driver.quit()