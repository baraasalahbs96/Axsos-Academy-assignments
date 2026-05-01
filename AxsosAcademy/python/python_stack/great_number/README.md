<div align="center">

# 🎮 Python Web: Great Number Game
**Managing Game State and User Sessions**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Focus-Game_Logic_in_Flask-black?style=for-the-badge)

</div>

---

## 📝 Description
The **Great Number Game** is an interactive web application where users try to guess a randomly generated number between 1 and 100 within a limited number of attempts (5). The project heavily utilizes Flask `session` to track the target number, attempt count, and game status across different HTTP requests, ensuring a persistent game experience.

---

## 🎯 Key Concepts
* **Game State Persistence:** Using the `session` object to store the secret `target_number` and `attempts` so the game doesn't reset on every guess.
* **Conditional Game Logic:** Implementing `if/elif/else` blocks to compare user input with the target number and determining game outcomes (too high, too low, winner, loser).
* **Limit Enforcement:** Managing a "Lose" condition by tracking attempt counts and locking the game (`game_over = True`) once the limit is reached.
* **Dynamic UI Rendering:** Using Jinja2 to conditionally show/hide the input form and the "Play Again" button based on the game's current status.
* **Bootstrap Theming:** Dynamically changing the UI color (e.g., green for win, red for loss) via session variables passed to CSS classes.

---

## 🛠️ Implementation Highlights
* **Robust Redirection:** The game follows the PRG (Post-Redirect-Get) pattern to ensure that refreshing the page doesn't inadvertently re-submit the previous guess.
* **Security:** Using `session` keeps the `target_number` hidden from the client-side HTML, preventing users from inspecting the code to see the answer.

---

## 🚀 How to Run
1. Ensure your directory structure is as follows:
   ```text
   /great_number_game
   ├── server.py
   └── templates/
       └── index.html
    ```

2. Run the server:
   ```bash
   python server.py
    ```

3. Visit the game at http://127.0.0.1:5000/