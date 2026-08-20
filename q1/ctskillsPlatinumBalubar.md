# ANNEX A
Section: 9-Platinum                                                 Score:
C# / Name: Van Lester G. Balubar                                    Date: Aug 11, 2026

Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:
   
    * Some students take too long to decide what to order.
    * The cashier has to manually calculate totals and give change.
    * There is no system to track which food items are running out.

Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem

Main Problem:

The problem is that the students are piling up in one line and as it goes on, the student thought of making new lines and began compiling and twisting making it look like a large crowd. Others also cant think of what food to buys while interacting the cashier, also adding to slow line movement.

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. The line being so long makes students annoyed losing interest of buying because of time.
2. Canteen staff getting confused and worked up contributed to loss of communication.
3. Line formation is messy making it look like a crowd.
4. People cutting in line making it annoying and long to wait.

Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

Sub-Problems                       CT Skills                          Example Solution


[num 1]                            [Efficieny]          Record order before cashier.  


[num 2]                           [Decomposition]        Assign staff for each line.  


[num 3]                           [Organization]         Make multiple instead of one.


[num 4]                   [Proper Syntax and Semantics]   Avoid cutting, maintain    line    

Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem

INPUT:

START CanteenOrderingSystem

    // Step 1: Initialize Canteen Menu Items and Stock
    CREATE ARRAY FoodMenu = ["Meal A", "Meal B", "Snack C", "Drink D"]
    CREATE ARRAY Prices   = [50, 40, 20, 15]
    CREATE ARRAY Stock    = [30, 25, 50, 40]
    
    DISPLAY "--- Welcome to the PSHS Canteen ---"
    
    // Step 2: Digital Menu Display (Solves Sub-Problem 1: Slow Decision Making)
    FOR EACH item, price IN FoodMenu, Prices
        DISPLAY item + " - Php " + price
    END FOR

    // Step 3: Student Pre-Order System (Solves Sub-Problem 3 & 4: Line Organization)
    PRINT "Assign student to Queue Line A, B, or C based on arrival order"
    
    INITIALIZE TotalCost = 0
    INITIALIZE OrderingFinished = FALSE
    
    WHILE OrderingFinished IS FALSE DO
        INPUT SelectedItem
        
        IF SelectedItem IS IN FoodMenu THEN
            GET Index OF SelectedItem
            
            // Check Inventory (Solves Inventory Tracking)
            IF Stock[Index] > 0 THEN
                TotalCost = TotalCost + Prices[Index]
                Stock[Index] = Stock[Index] - 1
                PRINT SelectedItem + " added to order."
            ELSE
                PRINT "Sorry, " + SelectedItem + " is OUT OF STOCK."
            END IF
        ELSE
            PRINT "Invalid item. Please select from the menu."
        END IF
        
        INPUT "Do you want to add another item? (YES/NO)", Choice
        IF Choice IS "NO" THEN
            OrderingFinished = TRUE
        END IF
    END WHILE

    // Step 4: Automated Payment & Change Calculation (Solves Sub-Problem 2: Staff Workload)
    DISPLAY "Total Amount Due: Php " + TotalCost
    
    REPEAT
        INPUT PaymentAmount
        IF PaymentAmount < TotalCost THEN
            PRINT "Insufficient payment. Please provide enough cash."
        END IF
    UNTIL PaymentAmount >= TotalCost

    COMPUTE Change = PaymentAmount - TotalCost
    DISPLAY "Payment Accepted. Your Change: Php " + Change

    // Step 5: Issue Order Receipt and Ticket Number
    GENERATE QueueTicketNumber
    PRINT "Order Confirmed! Your Queue Number is: " + QueueTicketNumber
    PRINT "Please proceed to the pick-up counter when your number is called."

END CanteenOrderingSystem

