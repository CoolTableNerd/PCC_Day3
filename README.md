# Python Crash Course: Day 3

### Python Lists & Loops (Chapter 4)

---

#### **1. Looping Through Lists**
- **For Loop Syntax**:
  ```python
  movies = ["Shutter Island", "Killers of the Flower Moon", "Wolf of Wall Street"]
  for movie in movies:
      print(f"{movie.title()}: Starring Leonardo DiCaprio")
  ```
  - `movie` = temporary loop variable  
  - Colon `:` and indentation are required.

---

#### **2. `range()` Function**
- Generates a sequence of numbers (exclusive of endpoint):
  ```python
  # Generate numbers 1-4
  for num in range(1, 5):
      print(num)  # Output: 1 2 3 4

  # Even numbers (2-10)
  even_numbers = list(range(2, 11, 2))  # [2, 4, 6, 8, 10]
  ```

---

#### **3. List Statistics**
- **Min/Max/Sum**:
  ```python
  numbers = [222, 333, 444, 555]
  print(min(numbers))  # 222
  print(max(numbers))  # 555
  print(sum(numbers))  # 1554
  ```

---

#### **4. Slicing Lists**
- Extract subsets using `[start:end]` (end index is exclusive):
  ```python
  players = ["LeBron James", "Luka Dončić", "Austin Reaves"]
  print(players[0:2])  # ["LeBron James", "Luka Dončić"]
  print(players[-2:])  # Last 2 players: ["Luka Dončić", "Austin Reaves"]
  ```

---

#### **5. Tuples**
- **Immutable lists** (cannot be modified):
  ```python
  coordinates = (40.7128, -74.0060)  # Uses parentheses
  print(coordinates[0])  # 40.7128
  ```

---

#### **6. `zip()` Function**
- Combine multiple iterables (lists, tuples) into pairs:
  ```python
  names = ["Luka", "Austin", "Lebron"]
  ages = [25, 26, 40]
  paired = list(zip(names, ages))  # [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
  ```

---

### Small Project: **Sports Team Roster Manager**

#### **Objective**  
Create a program to manage player rosters, calculate stats, and generate team pairings using lists, loops, slicing, and `zip()`.

---

#### **Requirements**
1. **Roster Setup**:
   - Create a list of players
   - Create a list of positions

2. **Slicing**:
   - Extract the starting lineup (first 3 players) and bench players (last 2).

3. **`zip()` Function**:
   - Pair players with their positions using `zip()`.

4. **Stats Calculation**:
   - Calculate average points per game (PPG) for a list of stats.

5. **Tuples**:
   - Store player-team pairs as immutable tuples (e.g., `("LeBron", "Lakers")`).

### Reflections