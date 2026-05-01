<div align="center">

# 🥷 Python Web: Ninja Gold
**Complex State Management and Real-time Activity Logging**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Focus-Session_Game_Logic-black?style=for-the-badge)

</div>

---

## 📝 Description
**Ninja Gold** is a classic development exercise where the user visits different buildings to "earn" or "lose" gold. This project showcases advanced use of Flask sessions to track not only a simple counter but also a dynamic list of objects (activity logs), move counters, and complex win/loss conditions.



---

## 🎯 Key Concepts
* **Dynamic Activity Log:** Storing a list of dictionaries in `session['activities']` to keep track of every move with specific timestamps and CSS classes for color-coding.
* **Complex Game Logic:** Implementing different probability ranges for various buildings (Farm, Cave, House, and the risky Casino).
* **Win/Loss Constraints:** Setting up multi-condition game states where the user wins at 500 gold or loses after 15 moves.
* **Session Modification:** Using `session.modified = True` to ensure Flask recognizes changes made to nested structures like lists.
* **UI Feedback:** Leveraging Jinja2 to disable buttons and display contextual alerts once the `game_over` state is triggered.

---

## 🛠️ Implementation Highlights
* **Timestamping:** Every activity is logged with a human-readable date and time using Python's `datetime` module.
* **Conditional Styling:** Automatically applying Bootstrap text classes (`text-success` or `text-danger`) based on whether gold was earned or lost.
* **Hidden Inputs:** Using `<input type="hidden">` to pass the building type to the backend without cluttering the UI.

---

## 🚀 How to Run
1. Ensure your directory structure is as follows:
   ```text
   /ninja_gold
   ├── server.py
   └── templates/
       └── index.html
    ```

2. Run the server:
   ```bash
   python server.py
    ```

3. Open your browser and navigate to http://127.0.0.1:5000/.