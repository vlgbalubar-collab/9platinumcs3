# Advanced Class Relationships

Previous Works

[View ClassAtr](q1/OOPActII/classAttributesMethod.md)
[ViewClassRel](q1/OOPActIII/classRelationships.md)

# System Inheritance Relationship:

Parent: VideoGames
Child: SteamGames
Explanation: VideoGames is the parent because SteamGames IS-A VideoGames. With that, the SteamGames can inherit the attributes (GameName and ReleaseDate) and the methods (view() and install()) of the VideoGames class. This will also have GameType as a specialized attribute to know the game category.

# Inheritance UML

<img width="165" height="376" alt="Screenshot 2026-09-24 214551" src="https://github.com/user-attachments/assets/565b0744-0c8e-4ceb-9437-e781691099d5" />

# Composition/Aggregation

Relationship: Composition (HAS-A)
Explanation: This is a Composition relationship because a SteamGame directly owns and creates its Achievements instances. An Achievements instance is not independent of its parent game. If a SteamGame is uninstalled, all made achievements inside its achievements list are destroyed alongside the game.

# Advanced UML Diagram

<img width="560" height="407" alt="Screenshot 2026-09-24 214957" src="https://github.com/user-attachments/assets/133fb0fb-31df-4886-8de3-6b598ad0cbf0" />

# Python Implementation Diagram


# Test Run

# Object Diagram

<img width="627" height="301" alt="Screenshot 2026-09-24 220257" src="https://github.com/user-attachments/assets/7674bfba-1c02-4483-9c1a-9e75f193222f" />

# Reflection

1. 
