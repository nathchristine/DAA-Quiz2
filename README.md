# DAA-Quiz2
### Project Design 
Our program aims to simplify the shopping experience by calculating the shortest path through the mall, focusing on highly-rated stores, and ensuring that each type of store is represented only once in the route. This way, shoppers can cover their essentials without unnecessary backtracking or duplicate visits to the same type of store.

### Algorithm Analysis
We’re implementing a greedy algorithm to find the best way to visit mall stores while reducing the overall walking distance.

Each data store contains information about the store itself, including its name, type or category, floor number, rating, and location on the mall layout (x and y coordinate).

Based on the user's input, (store type and a starting store), greedy initializes the starting point. 
Traversal proceeds by selecting the next store based on: the Euclidean distance between the current store and potential candidates and best rating. Traversal continues until all store types have been visited, with each store category covered at least once.
When there are no more stores to visit, the algorithm ends.
Total walking distance is calculated by summing the euclidean distances.

For the overall time complexity is O(n^2)

By going to every kind of retailer at least once, our algorithm offers a sensible route, but the greedy algorithm does not ensure the worldwide best route. It's efficient for smaller datasets but may struggle with a larger one.

### Visual

<img width="512" alt="Screenshot 2025-05-25 at 20 48 53" src="https://github.com/user-attachments/assets/24624a75-8396-4585-9ad8-09da2219247e" />

This is the home page of the Mall Greedy Path Finder, where users can select the type of store they want to visit and choose a starting store. Store types include Entertainment, Fashion, Food, Goods, and Service.

<img width="511" alt="Screenshot 2025-05-25 at 20 50 18" src="https://github.com/user-attachments/assets/b49ec556-9e4f-4f5f-997d-43dc7c93ce68" />

After selecting a store type, users can choose their starting store, which varies depending on the selected category. Each starting point is unique to its store type.

<img width="245" alt="Screenshot 2025-05-25 at 20 50 40" src="https://github.com/user-attachments/assets/2d159130-f53f-4d9c-8cf6-4e1a1a6e57e0" />

When the "Find Optimal Path" button (in purple) is clicked, the algorithm runs and displays the optimal path. The results include:
- Total Distance Traveled
- Stores Visited
- Execution Time of the algorithm
There are two different sections: a path table, which shows the path from the initial store to each store type with the optimal distance. For example, if the first store is Amazon, the table will also include details such as the floor it is located on and its category.

<img width="588" alt="Screenshot 2025-05-25 at 20 51 15" src="https://github.com/user-attachments/assets/9f83120d-eca8-4a51-8283-6e1109a1ab47" />

<img width="695" alt="Screenshot 2025-05-25 at 20 51 36" src="https://github.com/user-attachments/assets/2d3151b4-3b8d-465c-b905-31e7f4710377" />

### Analysis
For routing in small/ medium sized malls, our greedy algorithm performs well. By visiting every kind of retailer at least once, it provides a nice route, but it does not ensure the worldwide best route. It is effective for smaller datasets but may not be able to handle more stores due to its complexity of O(n^2). Although it helps in navigation, the UI visualization has no effect on algorithm performance.







