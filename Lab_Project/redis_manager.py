class RedisManager:
    def init(self):
        self.r = redis.Redis(host="localhost", port=6379, decode_responses=True) 

# CREATE 
def add_repo(self, repo_name, data): 
   self.r.hset(f"repo:{repo_name}", mapping=data) 
   self.r.sadd("game:repos", repo_name) 
   self.r.sadd(f"language:{data['language']}", repo_name) 
 
# READ 
def get_repo(self, repo_name): 
   return self.r.hgetall(f"repo:{repo_name}") 
 
# UPDATE 
def update_repo_stars(self, repo_name, stars): 
   self.r.hset(f"repo:{repo_name}", "stars", stars) 
 
# DELETE 
def delete_repo(self, repo_name): 
   data = self.get_repo(repo_name) 
   if data: 
       self.r.srem("game:repos", repo_name) 
       self.r.srem(f"language:{data['language']}", repo_name) 
   self.r.delete(f"repo:{repo_name}") 
 
# Utility 
def get_all_repos(self): 
   return self.r.smembers("game:repos") 
