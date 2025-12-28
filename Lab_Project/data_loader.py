import json 
  
def load_game_repos(file_path, redis_mgr): 
    with open(file_path, "r", encoding="utf-8") as f: 
        repos = json.load(f) 
  
    for repo in repos: 
        redis_mgr.add_repo( 
            repo["repo_name"], 
            { 
                "language": repo["language"], 
                "stars": repo["stars"], 
                "license": repo["license"] 
            } 
        ) 

    print("Game repositories loaded into Redis.") 
