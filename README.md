
# 🏦 Bank Management System (Python)

## 📌 Description

This is a **Bank Management System** project developed using **Core Python**. It simulates basic banking operations such as:
- Admin login and management
- Customer account creation and login
- Deposit and withdrawal
- Balance inquiry
- View, search, and delete accounts

All data is stored securely in **JSON files** (no database required), making it lightweight and easy to run.

---

## 🚀 Features

### 👨‍💼 Admin
- Login using Admin ID and password
- Forgot password option with reset
- View all customer accounts
- Search a customer account by account number
- Delete a customer account

### 👤 Customer
- Create a new account (random account number is generated)
- Secure login using account number and password
- Deposit and withdraw money
- View current account balance

---

## 💾 Data Storage
- Customer data is stored in `db/customers.json`
- Admin credentials are stored in `db/admin.json`

---

## 📁 Folder Structure

```
project-folder/
│
├── db/
│   ├── customers.json
│   └── admin.json
│
├── admin_panel.py
├── account.py
├── customer_dashboard.py
├── main.py
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3
- JSON for persistent data storage
- OOP Concepts: Classes, Inheritance, Encapsulation, etc.

---

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bank-management-system.git
   ```

2. Navigate to the project folder:
   ```bash
   cd bank-management-system
   ```

3. Run the program:
   ```bash
   python main.py
   ```

---

## 📌 Requirements

- Python 3.x installed
- No external libraries needed (only built-in modules)

---

## 📣 Author

**Kunal Pandit**
