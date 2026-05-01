<div align="center">

# 🔄 Python Web: Flask Session Counter
**State Management and Session Persistence**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Focus-Session_Management-black?style=for-the-badge)

</div>

---

## 📝 Description
This assignment introduces the `session` object in Flask, which allows the server to remember information about a user across multiple interactions. I built a dynamic counter application that tracks the number of page visits and maintains a customizable counter value, persisting these states even as the user interacts with different routes.



---

## 🎯 Key Concepts
* **Sessions:** Understanding that HTTP is a stateless protocol, and `session` (stored in encrypted cookies) is the tool used to maintain state.
* **`app.secret_key`:** Implementing a secret key to sign and secure session data, preventing user tampering.
* **Redirection:** Using `return redirect('/')` after processing `POST` requests to follow the **POST/Redirect/GET** design pattern, which prevents duplicate form submissions.
* **Session Lifecycle:** Learning to initialize keys, update values, and use `session.clear()` to destroy session data.

---

## 🛠️ Implementation Highlights
* **Dynamic Interaction:** The app allows users to increment the counter by a fixed amount (+2), by a custom user-defined amount, or reset it entirely.
* **Session Persistence:** The data persists through browser refreshes and form submissions, providing a smooth user experience.
* **Clean UI:** Styled with Bootstrap for a responsive layout and clear visual feedback on session values.

---

## 🚀 How to Run
1. Ensure your directory structure is as follows:
   ```text
   /project_folder
   ├── server.py
   ├── static/
   │   └── style.css
   └── templates/
       └── index.html
     ```

2. Run the server:

   ```bash
   python server.py
    ```

3. Visit the local server at http://127.0.0.1:5000/ and test the counter buttons.