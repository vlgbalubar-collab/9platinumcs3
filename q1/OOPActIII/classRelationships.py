class Achievements:
    def __init__(self, achievement_name: str, description: str, level_of_status: str, reward: str, username: str):
        self.achievement_name = achievement_name
        self.description = description
        self.level_of_status = level_of_status
        self.reward = reward
        self.__username = username  # Private attribute (-)

    def display_achievement(self):
        print(f"Achievement: {self.achievement_name} | {self.description} | Reward: {self.reward}")


class SteamGame:
    def __init__(self, game_name: str, developer: str, game_type: str, total_storage_gb: int, finance_records: int):
        self.gamename = game_name
        self.developer = developer
        self.gametype = game_type
        self.totalstoragegb = total_storage_gb
        self.__financerecords = finance_records  # Private attribute (-)
        self.is_running = False
        
        # 1 to 1..* Relationship: Container for achievement instances
        self.achievements: list[Achievements] = []

    def add_achievement(self, achievement: Achievements):
        """Helper method to fulfill the 1..* composition relationship."""
        self.achievements.append(achievement)

    def update_storage(self, additional_gb: int):
        self.totalstoragegb += additional_gb
        print(f"Updated {self.gamename} storage. New size: {self.totalstoragegb} GB.")

    def play(self):  # Renamed/Added from UML diagram
        if not self.is_running:
            self.is_running = True
            print(f"{self.gamename} is now playing!")
        else:
            print(f"{self.gamename} is already running.")

    def install_game(self, game_name: str):
        print(f"Installing {game_name}...")

    def save(self):
        print(f"Progress saved for {self.gamename}.")

    def get_game_status(self) -> str:
        status = "Running" if self.is_running else "Stopped"
        return f"Game: {self.gamename} | Developer: {self.developer} | Size: {self.totalstoragegb} GB | Status: {status} | Achievements Unlocked: {len(self.achievements)}"


# --- Execution Example ---

game1 = SteamGame("TF2", "Valve Corp", "Action", 30, 500000)

# Creating achievements and adding them to the game instance
ach1 = Achievements("Headshot Master", "Get 100 headshots", "Gold", "Sniper Hat", "Player1")
ach2 = Achievements("First Blood", "Get the first kill in a match", "Bronze", "100 XP", "Player1")

game1.add_achievement(ach1)
game1.add_achievement(ach2)

print("--- GAME STATUS ---")
print(game1.get_game_status())

print("\n--- ACHIEVEMENTS ---")
for achievement in game1.achievements:
    achievement.display_achievement()
