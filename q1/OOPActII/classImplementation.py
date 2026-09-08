class Steam:
def __init__(self, gamename: str = "", developer: str = "", totalstoragegb: int = 0, gametype: str = "" ):
self.gamename = gamename
slef.developer = developer
self.gametype = gametype
self.totalstoragegb = totalstoragegb
self.financerecords = {
            "price": price,
            "total_sales": 0,
            "gross_revenue": 0.0,
            "total_refunds": 0
        }

def buy_game(self, copies_sold: int) -> None:
        """Receives a parameter and safely updates the private financial records state."""
        if copies_sold > 0:
            self.__finance_records["total_sales"] += copies_sold
            added_revenue = copies_sold * self.__finance_records["price"]
            self.__finance_records["gross_revenue"] += added_revenue
            print(f"[{self.game_name}] Processed {copies_sold} sale(s). Revenue added: ${added_revenue:.2f}")

    def process_refund(self, refunds_count: int) -> None:
        """Safely deducts revenue from private finance records while enforcing bounds."""
        if refunds_count > 0 and refunds_count <= self.__finance_records["total_sales"]:
            self.__finance_records["total_sales"] -= refunds_count
            self.__finance_records["total_refunds"] += refunds_count
            deducted_revenue = refunds_count * self.__finance_records["price"]
            self.__finance_records["gross_revenue"] -= deducted_revenue
            print(f"[{self.game_name}] Processed {refunds_count} refund(s). Revenue deducted: ${deducted_revenue:.2f}")
        else:
            print(f"[{self.game_name}] Invalid refund request.")

    def get_game_info(self) -> str:
        """Reads and returns information from both private attributes."""
        records = self.__finance_records
        return (f"Game: {self.game_name} ({self.game_type}) | Size: {self.__total_storage_gb} GB | "
                f"Price: ${records['price']:.2f} | Units Sold: {records['total_sales']} | "
                f"Gross Revenue: ${records['gross_revenue']:.2f}")

if __name__ == "__main__":
    game1 = SteamGame("Elden Ring", "FromSoftware", "Action RPG", 60, 59.99)
    game2 = SteamGame("Stardew Valley", "ConcernedApe", "Farming Sim", 1, 14.99)

    print("--- BEFORE ---")
    print("Object 1:", game1.get_game_info())
    print("Object 2:", game2.get_game_info())

    print("\nPerforming action on Object 1 only...")
    game1.buy_game(10)  

    print("\n--- AFTER ---")
    print("Object 1:", game1.get_game_info()) 
    print("Object 2:", game2.get_game_info())  
