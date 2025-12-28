from redis_manager import RedisManager
from data_loader import load_game_repos
from features import popular_languages, top_starred_repos, stars_chart

def menu():
    print("\n--- Game Repositories (Redis) ---")
    print("1. Load game repositories data")
    print("2. View repository")
    print("3. Update stars")
    print("4. Delete repository")
    print("5. Popular game languages")
    print("6. Top starred repositories")
    print("7. Stars visualization")
    print("0. Exit")

def main():
    redis_mgr = RedisManager()

    while True:
        menu()
        choice = input("Select an option")

        if choice == "1":
            load_game_repos("data/game_repos.json", redis_mgr)

        elif choice == "2":
            name = input("Repository name: ")
            print(redis_mgr.get_repo(name))

        elif choice == "3":
            name = input("Repository name: ")
            stars= input("New star count: ")
            redis_mgr.update_repo_stars(name, stars)

        elif choice == "4": 
            name = input("Repository name: ") 
            redis_mgr.delete_repo(name) 

        elif choice == "5": 
            popular_languages(redis_mgr) 

        elif choice == "6": 
            top_starred_repos(redis_mgr) 

        elif choice == "7": 
            stars_chart(redis_mgr)

        elif choice == "0":
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
