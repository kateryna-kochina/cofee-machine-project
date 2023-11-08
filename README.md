This Python script represents a virtual coffee machine simulation. The program allows users to interact with a menu, 
select a coffee recipe, insert coins to pay for the order, and receive a virtual coffee in return. The simulation also 
keeps track of resources such as water, milk, and coffee grounds, as well as the machine's balance in terms of accepted coins.


Here's a brief overview of the main functionalities:
1. Menu Display: The program displays a menu of coffee recipes along with their respective costs.
2. Order Placement: Users can choose a coffee recipe by typing the corresponding number (1, 2, or 3) from the menu.
3. Resource and Coin Management:
* The program checks if there are sufficient resources (water, milk, and coffee) to fulfill the order.
* Users are prompted to insert coins of different values (quarters, dimes, nickels, and pennies) to pay for the selected coffee.
4. The program calculates the total amount of money inserted and compares it with the cost of the selected coffee.
* If the inserted amount matches the cost, the coffee is prepared, resources are deducted, and the remaining balance is updated.
* If the inserted amount is insufficient, the program prompts the user to insert more coins or refunds the inserted amount.
* If the inserted amount exceeds the cost, the excess amount is returned as change, and the coffee is prepared.

**Reporting: **Users can request a report that displays the current status of available resources (water, milk, coffee) and the machine's balance.
**Shutdown: **Users can type "off" to turn off the coffee machine simulation.

The script is structured with functions for various tasks such as checking resource sufficiency, 
handling coin insertion, updating the balance, and preparing the coffee. The main while loop allows continuous 
interaction with the coffee machine until the user decides to turn it off.
