## Libs
from os import getlogin
from selenium import webdriver
import csv
import time

def new_webdriver():
    op = webdriver.ChromeOptions()
    op.add_argument("--start-maximized")
    op.add_argument("--user-data-dir=C:/Users/"+getlogin()+"/AppData/Local/Google/Chrome/User Data/Profile 1")
    op.add_argument("--profile-directory=Profile 1")
    op.add_argument("--disable-extensions")
    
    driver = webdriver.Chrome(executable_path="chromedriver", options=op)
    return driver

def localize_nextPageButton(driver):
    driver.execute_script("window.scrollTo(0,3000)")
    try:
        nextPage_button = driver.find_element(by="xpath", value="//a[@class='next_page']")
        
        return nextPage_button
    except:
        return False

def localize_repositories(driver):
    time.sleep(1)
    org_repos = driver.find_elements(by="xpath", value="//*[@id='org-repositories']/div/div/div/ul/li")
    
    repo_names = []
    for repo in org_repos:
        name = repo.text.split("\n")[0]
        repo_names.append(name)
    
    return repo_names

def get_repoFrom_allPages(driver):
    nextPage_button = True;
    
    final_repoNames = []
    
    while (nextPage_button != False):
    
        repo_names = localize_repositories(driver=driver)
        
        for name in repo_names:
            final_repoNames.append(name)
    
        time.sleep(1)
    
        nextPage_button = localize_nextPageButton(driver=driver)
        if(nextPage_button == False):
            break
        nextPage_button.click()
        
    return final_repoNames

def get_repos_fromUrl(url):
    driver = new_webdriver()
    time.sleep(5)
    
    driver.get(url)
    time.sleep(2)
    
    repoNames = get_repoFrom_allPages(driver=driver)
    
    with open('data/bytelegend.csv', 'w') as f:
        writer = csv.writer(f)
    
        for repo in repoNames:
            writer.writerow(repo)

if __name__ == "__main__":
    get_repos_fromUrl("https://github.com/orgs/ByteLegendQuest/repositories?type=all")