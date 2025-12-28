from collections import Counter 
import matplotlib.pyplot as plt 

def popular_languages(redis_mgr): 
    counter = Counter() 
  
    for repo in redis_mgr.get_all_repos(): 
        data = redis_mgr.get_repo(repo) 
        counter[data["language"]] += 1 
  
    print("Game Repositories by Language:") 
    for lang, count in counter.items(): 
        print(f"{lang}: {count}") 
  
def top_starred_repos(redis_mgr): 
    repos = [] 
  
    for repo in redis_mgr.get_all_repos(): 
        data = redis_mgr.get_repo(repo) 
        repos.append((repo, int(data["stars"]))) 
    repos.sort(key=lambda x: x[1], reverse=True) 
    print("Top Starred Game Repositories:") 
    for repo, stars in repos: 
        print(f"{repo}: {stars} stars") 

def stars_chart(redis_mgr): 
    repos = redis_mgr.get_all_repos() 
    names = [] 
    stars = [] 
  
    for repo in repos: 
        data = redis_mgr.get_repo(repo) 
        names.append(repo) 
        stars.append(int(data["stars"])) 
  
    plt.bar(names, stars) 
    plt.xticks(rotation=45) 
    plt.title("Stars per Game Repository") 
    plt.tight_layout() 
    plt.show() 
