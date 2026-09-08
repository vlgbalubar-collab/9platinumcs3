# Previous Work
# Link to my previous activity
[View OOPAct](q1/classObjectUML.md)

## Design Revision
Changes from my previous design:
- Renamed the class from generic `Steam` to `SteamGame` to explicitly identify it as a blueprint for individual games.
- Updated attribute names to follow standard Python naming conventions (`game_name`, `developer`, `game_type`).
- Replaced `Amount of bits` with `__total_storage_gb` (integer) for clearer representation of required storage.
- Added a private boolean attribute `__is_running` to keep track of whether the game session is active.

## Visibility Decisions
|   Attribute   | Data Type | Visibility |                               Reason                                    |
|---------------|-----------|------------|-------------------------------------------------------------------------|
|+GameName      | String    | Public     | A general attribute that can be accessed from outside the class         |
|+Developer     | String    | Public     | A general attribute that can be accessed from outside the class         |
|+TotalStorageGB| Integer   | Public     | A general attribute that can be accessed from outside the class         |
|+GameType      | String    | Public     | A general attribute that can be accessed from outside the class         |
|-IsRunning     | Boolean   | Private    | A sensitive attribute that should not be accessed from outside the class|

## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)
## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
