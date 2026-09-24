class Achievements:
    """Part Class: Representing achievements belonging to a game."""
    def __init__(self, achievement_name: str, description: str, level_of_status: str, reward: str, username: str):
        self.achievement_name = achievement_name
        self.description = description
        self.level_of_status = level_of_status
        self.reward = reward
        self.__username = username  # Private attribute (-)

    def display_achievement(self):
        print(f"Achievement: {self.achievement_name} | {self.description} | Reward: {self.reward}")


class SteamGame:
    """Parent Class: General Steam Game representation."""
    def __init__(self, game_name: str, developer: str, game_type: str, total_storage_gb: int, finance_records: int):
        self.gamename = game_name
        self.developer = developer
        self.gametype = game_type
        self.totalstoragegb = total_storage_gb
        self.__financerecords = finance_records  # Private attribute (-)
        self.is_running = False
        
        # COMPOSITION CONTAINER: Stores internal achievement instances
        self.achievements: list[Achievements] = []

    def create_achievement(self, name: str, desc: str, level: str, reward: str, username: str):
        """
        COMPOSITION METHOD:
        The SteamGame instance creates and manages the Achievements object directly.
        """
        new_achievement = Achievements(name, desc, level, reward, username)
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


class MultiplayerSteamGame(SteamGame):
    """
    CHILD CLASS (INHERITANCE):
    MultiplayerSteamGame IS-A SteamGame.
    """
    def __init__(self, game_name: str, developer: str, game_type: str, total_storage_gb: int, finance_records: int, max_players: int, server_region: str):
        # Reuse parent constructor using super().__init__()
        super().__init__(game_name, developer, game_type, total_storage_gb, finance_records)
        self.max_players = max_players
        self.server_region = server_region

    def display_multiplayer_info(self):
        print(f"{self.gamename} [Server: {self.server_region}] | Capacity: {self.max_players} players")


class SteamServer:
    """
    DEPENDENCY CLASS:
    Uses-A relationship. Temporarily receives a SteamGame object without owning it.
    """
    def ping_game(self, game: SteamGame):
        print(f"Pinging server for {game.gamename}... Connection stable.")


# ==========================================
# STEP 10: SYSTEM DEMONSTRATION & TEST RUN
# ==========================================
if __name__ == "__main__":
    print("==========================================")
    print("--- TEST 1: INHERITANCE DEMONSTRATION ---")
    print("==========================================")
    # Instantiate child class
    tf2 = MultiplayerSteamGame("TF2", "Valve Corp", "Action", 30, 500000, 32, "US-East")
    
    # Child uses inherited method from parent class (SteamGame)
    print("Parent Method Call:")
    print(tf2.get_game_status())
    
    # Child calls its own unique method
    print("\nChild Method Call:")
    tf2.display_multiplayer_info()

    print("\n==========================================")
    print("--- TEST 2: COMPOSITION DEMONSTRATION ---")
    print("==========================================")
    # The parent object creates the contained objects directly internally
    tf2.create_achievement("Headshot Master", "Get 100 headshots", "Gold", "Sniper Hat", "Player1")
    tf2.create_achievement("First Blood", "Get the first kill in a match", "Bronze", "100 XP", "Player1")
    
    # Display updated status and iterate over internally owned achievements
    print(tf2.get_game_status())
    print("\nListing Game Achievements:")
    for ach in tf2.achievements:
        ach.display_achievement()

    print("\n==========================================")
    print("--- TEST 3: DEPENDENCY DEMONSTRATION ---")
    print("==========================================")
    # SteamServer temporarily receives tf2 without owning it
    server = SteamServer()
    server.ping_game(tf2)
