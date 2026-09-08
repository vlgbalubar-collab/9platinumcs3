class SteamGame:
    def __init__(self, game_name: str, developer: str, game_type: str, total_storage_gb: int, finance_records: int):
        self.gamename = gamename
        self.developer = developer
        self.gametype = gametype
        self.totalstoragegb = totalstoragegb
        self.is_running = False
        self.financerecords = financerecords

    def update_storage(self, additional_gb: int):
        self.totalstoragegb += additional_gb
        print(f"Updated {self.gamename} storage. New size: {self.totalstoragegb} GB.")
                
    def launch_game(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.gamename} has been launched!")
        else:
            print(f"{self.gamename} is already running.")

    def get_game_status(self) -> str:
        status = "Running" if self.is_running else "Stopped"
        return f"Game: {self.gamename} | Developer: {self.developer} | Size: {self.totalstoragegb} GB | Status: {status}"


game1 = SteamGame("TF2", "Valve Corp", "Action", 30, 500000)
game2 = SteamGame("Rome: Total War", "Creative Assembly", "Strategy", 16, 250000)

print("--- BEFORE ---")
print(game1.get_game_status())
print(game2.get_game_status())

print("\nPerforming action on Object 1...")
game1.launch_game()

print("\n--- AFTER ---")
print(game1.get_game_status())
print(game2.get_game_status())
