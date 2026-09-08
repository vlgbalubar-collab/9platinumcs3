# Previous Work
[


## Design Revision
Changes from my previous design:
- Renamed the class from generic `Steam` to `SteamGame` to explicitly identify it as a blueprint for individual games.
- Updated attribute names to follow standard Python naming conventions (`game_name`, `developer`, `game_type`).
- Replaced `Amount of bits` with `__total_storage_gb` (integer) for clearer representation of required storage.
- Added a private boolean attribute `__is_running` to keep track of whether the game session is active.
