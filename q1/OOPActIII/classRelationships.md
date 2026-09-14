# Previous Work
[View Object UML](q1/classObjectUML.md) [View Attributes Method](q1/OOPActII/classAttributesMethod.md)

# Previous Class
Class: Steam Games: A collection of games from the gaming platform, based on the game type you like best.

# New Class
Class: Achievements: An object that recognizes your excellence, hard work, and participation in the game.

# Association
A Steam game HAS-A/an achievement. It means that every game has achievements to recognize the players' participation and planting the goal to have more. 

# Multiplicity

Steam Game 1 ------------- 1... Achievement Explanation: A Steam can have only one achievement, mostly for beating the game.

# UML Class Relationship Diagram

# Python Implementation
[View](q1/OOPActIII/classRelationships.py)

# Test Run

# Object Relationship Diagram

## Analysis

1. What is the association between your two classes? Explain the relationship using your actual system.
  - The relationship is a 1-to-many composition association where a single SteamGame object acts as the primary owner that stores and manages one or more  Achievements instances.
    
2. What multiplicity did you choose, and why? Explain why 1:1, 1:0..*, or another multiplicity is
appropriate.
- I used 1 to 1..* because every game needs an achievement, some can only have one while others have many. 1:1 is more appropriate because this prevents orphaned achievements and avoids restricting games to only a single achievement.
  
3. How did you implement the relationship in Python? Identify which attribute stores the related object or objects.
   - The relationship is implemented by storing Achievements instances inside a list attribute inside the SteamGame class. The self.achievements holds the collection of related achievement objects.

4. Why did you store an object reference instead of copying its data? Use one example from your
implementation.
- Storing the object references ensure the single source of code and preventing the duplication of the source code.

6. If your relationship uses “many,” why is a list appropriate? Explain what the list actually contains.
- A list is appropriate because it is an ordered collection that flexibly holds multiple items, also storing direct memory references to individual Achievements class objects.


