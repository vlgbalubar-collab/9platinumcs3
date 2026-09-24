class Achievements:
    def __init__(self, achievement_name: str, description: str, level_of_status: str, reward: str, username: str):
        self.achievement_name = achievement_name
        self.description = description
        self.level_of_status = level_of_status
        self.reward = reward
        self.__username = username  

    def display_achievement(self):
        print(f"Achievement: {self.achievement_name} | {self.description} | Reward: {self.reward}")


class VideoGames:
    def __init__(self, game_name: str, release_date: str):
        self.gamename = game_name
        self.release_date = release_date

    def view(self):
        print(f"Game: {self.gamename} | Release Date: {self.release_date}")

    def install(self):
        print(f"Installing {self.gamename}...")

class SteamGame(VideoGames):
    def __init__(self, game_name: str, release_date: str, developer: str, game_type: str, total_storage_gb: int, finance_records: int):
        super().__init__(game_name, release_date)
        
        self.developer = developer
        self.gametype = game_type
        self.totalstoragegb = total_storage_gb
        self.__financerecords = finance_records 
        self.is_running = False
        
        self.achievements: list[Achievements] = []

    def create_achievement(self, achievement_name: str, description: str, level_of_status: str, reward: str, username: str):
        new_achievement = Achievements(achievement_name, description, level_of_status, reward, username)
        self.achievements.append(new_achievement)

    def update_storage(self, additional_gb: int):
        self.totalstoragegb += additional_gb
        print(f"Updated {self.gamename} storage. New size: {self.totalstoragegb} GB.")

    def play(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.gamename} is now playing!")
        else:
            print(f"{self.gamename} is already running.")

    def get_game_status(self) -> str:
        status = "Running" if self.is_running else "Stopped"
        return f"Game: {self.gamename} | Developer: {self.developer} | Size: {self.totalstoragegb} GB | Status: {status} | Achievements Unlocked: {len(self.achievements)}"


# --- TEST RUN ---
if __name__ == "__main__":
    print("--- INHERITANCE TEST ---")
    # Inherits from VideoGames
    game1 = SteamGame("TF2", "October 10, 2007", "Valve Corp", "Action", 30, 500000)
    
    # Methods inherited from VideoGames parent class
    game1.view()
    game1.install()

    print("\n--- COMPOSITION TEST ---")
    # SteamGame creates achievements inside itself
    game1.create_achievement("Headshot Master", "Get 100 headshots", "Gold", "Sniper Hat", "Player1")
    game1.create_achievement("First Blood", "Get the first kill in a match", "Bronze", "100 XP", "Player1")

    print(game1.get_game_status())
    
    print("\n--- ACHIEVEMENTS ---")
    for achievement in game1.achievements:
        achievement.display_achievement()
