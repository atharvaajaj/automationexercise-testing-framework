# 🧪 Automation Testing Framework for AutomationExercise Website

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Framework-orange?logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI-CD-blue?logo=githubactions&logoColor=white)
![Status](https://img.shields.io/badge/Status-Stable-success)

A **Selenium–Pytest automation suite** built to validate key **e-commerce user flows** like login, signup, cart, checkout, and search on the [AutomationExercise](https://automationexercise.com/) demo web application.

---

## 🚀 Project Overview

This project demonstrates a **scalable and modular test automation framework** using the **Page Object Model (POM)**.  
It validates the functional behavior of major website components and generates detailed HTML reports after each execution.

This suite is ideal for showcasing automation skills in:
- **Web UI automation**
- **Framework design**
- **Selenium synchronization**
- **Pytest execution & reporting**

---

## 🧩 Features

- ✅ Page Object Model (POM) for maintainability  
- ✅ Comprehensive functional coverage (Login, Signup, Cart, Checkout, Search)  
- ✅ Stable explicit waits and ad-handling logic  
- ✅ HTML report generation using **pytest-html**  
- ✅ GitHub Actions CI/CD integration  
 

---

## 🧰 Tech Stack

| Category | Tool |
|-----------|------|
| Language | Python 3.12 |
| Test Runner | Pytest |
| Automation Tool | Selenium WebDriver |
| Reporting | Pytest-HTML |
| Structure | Page Object Model (POM) |
| Continuous Integration | GitHub Actions |
| Supported Browser | Chrome (default) |

---

## 📂 Project Structure

```
automationexercise_test_project/
├─ pageobjects/
│  ├─ login_page.py
│  ├─ cart_page.py
│  ├─ signup_page.py
│  ├─ checkout_page.py
│  ├─ home_page.py
│  └─ search_page.py
├─ tests/
│  ├─ test_login.py
│  ├─ test_signup.py
│  ├─ test_cart.py
│  ├─ test_checkout.py
│  ├─ test_search.py
│  └─ test_homepage.py
│  └─ conftest.py
├─ utils/
│  └─ webdriver_utils.py
├─ Final Run Command.txt
├─ Website Link.txt
├─ requirements.txt
├─ pytest.ini
├─ report.html ← auto-generated after run
└─ README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/automationexercise_test_project.git
cd automationexercise_test_project
```

---

### 2️⃣ Create and Activate a Virtual Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Tests

### 🧩 Run All Tests (Windows CMD)
```bash
set PYTHONPATH=%CD% && pytest -v --html=report.html --self-contained-html
```

---

### 🎯 Run a Single Test
```bash
pytest tests/test_login.py::TestLogin::test_invalid_login -v
```

---

### 🧾 Generate an HTML Report
After the test run, open `report.html` in your browser to view the detailed results.

---

## 🧠🧪 Test Scenarios Implemented

| **S.No.** | **Module / File**            | **Test Case**                                    | **Description**                                  | **Status** |
| --------- | ---------------------------- | ------------------------------------------------ | ------------------------------------------------ | ---------- |
| 1         | `test_automationexercise.py` | `TestAutomationExercise::test_open_homepage`     | Verify homepage loads successfully               | ✅ Passed   |
| 2         | `test_automationexercise.py` | `TestAutomationExercise::test_navigate_products` | Verify Products page navigation works            | ✅ Passed   |
| 3         | `test_automationexercise.py` | `TestAutomationExercise::test_search_product`    | Validate product search functionality            | ✅ Passed   |
| 4         | `test_cart.py`               | `TestCart::test_add_to_cart`                     | Add product to cart and verify count             | ✅ Passed   |
| 5         | `test_cart.py`               | `TestCart::test_remove_from_cart`                | Remove product from cart and verify empty state  | ✅ Passed   |
| 6         | `test_checkout.py`           | `TestCheckout::test_place_order_success`         | Verify successful order placement                | ✅ Passed   |
| 7         | `test_login.py`              | `TestLogin::test_valid_login`                    | Verify valid login with correct credentials      | ✅ Passed   |
| 8         | `test_login.py`              | `TestLogin::test_invalid_login`                  | Verify error message for invalid credentials     | ✅ Passed   |
| 9         | `test_search.py`             | `TestSearch::test_search_valid_product`          | Verify search results for a valid product        | ✅ Passed   |
| 10        | `test_search.py`             | `TestSearch::test_search_invalid_product`        | Verify message for invalid search query          | ✅ Passed   |
| 11        | `test_signup.py`             | `TestSignup::test_valid_signup`                  | Verify successful registration of new user       | ✅ Passed   |
| 12        | `test_signup.py`             | `TestSignup::test_signup_existing_email`         | Verify error when signing up with existing email | ✅ Passed   |


---

## 🏁 Sample Output
✅ 12 tests passed in 113.73s

---

## 💬 Future Enhancements
- Integrate **Allure Reports** for richer insights  
- Add **Cross-browser testing** (Firefox, Edge)  
- Enable **parallel execution** with `pytest-xdist`  
- Include **API testing module** for end-to-end validation  

---

## ✨ Summary

This framework demonstrates:
- Professional POM structure  
- Reusable utility-driven design  
- Reliable synchronization with dynamic web elements  
- Clean reporting and CI-ready automation flow  

Built with precision and best practices by **Atharva Joshi** 🧩  

---

## 👤 Author

**Atharva Joshi**  
*Aspiring Data Analyst & QA Automation Enthusiast*  

🔗 GitHub: [https://github.com/atharvaajaj](https://github.com/atharvaajaj)
