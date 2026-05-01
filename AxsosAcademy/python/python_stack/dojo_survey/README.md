<div align="center">

# 📝 Python Web: Form Handling with Flask
**Processing User Input and POST Requests**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Focus-POST_Requests-black?style=for-the-badge)

</div>

---

## 📝 Description
This project focuses on building a functional survey form. I learned how to collect various input types (text, select, radio, checkbox, textarea) from an HTML form and process them in the Flask backend using `request.form`. The collected data is then passed to a result page for display, demonstrating the full cycle of data input and output.

---

## 🎯 Key Concepts
* **POST Method:** Using `method="POST"` in the HTML form to securely send data to the server, as opposed to `GET` which exposes parameters in the URL.
* **`request.form`:** Accessing form data sent from the client-side to the Python route.
* **`getlist()` Method:** Correctly handling multiple values from a single field (like checkboxes) by retrieving them as a list.
* **Jinja2 Filters:** Using the `| join(', ')` filter to convert a list of interests into a readable, comma-separated string for display.
* **Bootstrap Forms:** Implementing professional form layouts using Bootstrap utility classes.

---

## 🛠️ Implementation Highlights
* **Data Mapping:** Successfully aggregated diverse input types into a single dictionary (`survey_data`) to pass cleanly between routes and templates.
* **Dynamic Feedback:** The `result.html` template acts as a confirmation page, reflecting exactly what the user entered.

---

## 🚀 How to Run
1. Ensure your directory structure is as follows:
   ```text
   /project_folder
   ├── server.py
   └── templates/
       ├── index.html
       └── result.html
    ```

2. Run the server:

   ```bash
   python server.py
    ```

3. Open your browser and navigate to http://127.0.0.1:5000/ to fill out the survey.