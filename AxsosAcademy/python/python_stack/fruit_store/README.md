<div align="center">

# 🍎 Dojo Fruit Store
**A Full-Cycle Order Management Application**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Focus-Full_Stack_App-black?style=for-the-badge)

</div>

---

## 📝 Description
The **Dojo Fruit Store** is a web application that allows students to order fruits, process their choices, and display a summary of their checkout. The application demonstrates the transition from a data-entry form to a dynamic result page, incorporating real-time data processing and server-side logic.


---

## 🎯 Core Features
* **Dynamic Ordering:** Students can select quantities for various fruits (Strawberry, Raspberry, Apple) via a form.
* **Backend Processing:** Flask handles the `POST` request, calculates the `total_count` of fruits, and captures the exact timestamp of the order using the `datetime` module.
* **Order Summary:** A dedicated checkout page (`checkout.html`) displays the user's name, ID, detailed order breakdown, and the order completion time.
* **Visual Gallery:** A separate route (`/fruits`) showcases the available fruit inventory using static image assets.

---

## 🛠️ Key Concepts
* **Data Processing:** Combining multiple form inputs into a cohesive summary.
* **Datetime Handling:** Implementing `datetime.now().strftime(...)` to log and display accurate transaction times.
* **Templating Inheritance & Structure:** Managing multiple HTML templates that share a common visual style through external CSS.
* **Static File Serving:** Correctly organizing and loading CSS and image assets using Flask's `url_for('static', ...)` pattern.

---

## 🚀 How to Run
1. Ensure your folder structure matches the provided architecture:
   ```text
   /dojo_fruit_store
   ├── server.py
   ├── static/
   │   ├── css/
   │   └── img/
   └── templates/
       ├── checkout.html
       ├── fruits.html
       └── index.html
    ```

2. Run the server:

   ```bash
   python server.py
    ```

3. Visit the local server at http://127.0.0.1:5000/ to start ordering.