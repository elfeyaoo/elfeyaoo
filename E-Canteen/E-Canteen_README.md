# E-Canteen — Digital Canteen Management System for APSIT Campus

> A Java-based desktop application that digitizes food ordering, payment, and canteen management for a college campus.

---

## 📌 Overview

Traditional campus canteens struggle with long queues, manual order-taking, no order tracking, and cash-only payments. **E-Canteen** solves this with a digital ordering and management system built for the APSIT campus — students can browse menus, place orders, and track them in real time, while admins manage menus, orders, and inventory through a dedicated dashboard.

**Team:** Mini Project — S.E., CSE (Data Science)
- Avadhoot Virkar (22107064)
- Atharva Thube (22107062)
- Akash Vidwan (22107007)

**Project Guide:** Prof. Sheetal Jadhav
**Institute:** A.P. Shah Institute of Technology, University of Mumbai (Academic Year 2023–24)

---

## ❗ Problem This Solves

- Inefficient, error-prone manual order-taking and payment processing
- No visibility for customers into their order status
- Cumbersome cash-based payment systems for both staff and students
- Long queues and wait times during peak dining hours

## 🎯 Objectives

- Simplify food ordering and reduce waiting times for students/faculty
- Digitize order management and inventory tracking for canteen operators
- Make menus easily accessible and browsable, with images and pricing
- Reduce order errors through a clear customization/order interface
- Provide real-time order tracking and status notifications

---

## 🛠️ Technology Stack

**Language:** Java (both frontend GUI and backend logic)
**Database:** MySQL
**IDE:** Apache NetBeans
**JDK:** Java Development Kit 21

---

## 🚀 Features

### Student Module
- Account registration/login with college ID
- Browse categorized menu (breakfast, lunch, snacks, beverages) with images, descriptions, and prices, across two campus canteens
- Place orders, specify quantities, and pay via a dummy/simulated payment system
- Real-time order tracking with estimated waiting time
- View past order records

### Admin Module
- Secure admin login, separate from student accounts
- Add, update, or remove menu items (prices, descriptions, prep time)
- View, process, and track ongoing and completed orders
- Review payment records
- Manage user accounts (reset passwords, resolve account issues)

---

## ⚙️ How It Works

1. **Registration** — Students create an account using their college ID; accounts are verified before use.
2. **Browse Menu** — Students view the categorized menu with images and prices for two campus canteens.
3. **Place Order** — Students select items, specify quantities, and confirm — the system calculates the total amount and estimated waiting time before final confirmation.
4. **Payment** — Payment is processed through a simulated/dummy payment system built into the app.
5. **Order Tracking** — Students can track their order status in real time until it's ready.
6. **Admin Management** — Admins log in separately to view/process incoming orders, edit the menu (add, update, remove items), and review payment records.

---

## 🏗️ System Architecture

<!-- Paste your block diagram / system architecture below -->



---

## 📸 Screenshots

<!-- Paste each screenshot below its heading -->

### Student Dashboard


### Admin Dashboard


### Student Order/Menu Page


### Admin Edit Menu Page


---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/elfeyaoo/My-Projects.git
cd My-Projects/E-Canteen

# Open the project in Apache NetBeans

# Set up the MySQL database
# 1. Create a database (e.g., ecanteen_db)
# 2. Import the provided .sql schema file (if included)
# 3. Update the MySQL connector credentials in the project's DB config file

# Build and run the project from NetBeans
```
*(Adjust these steps to match your actual project structure — add a `.sql` schema file to the repo if you haven't already, so the database is reproducible for anyone who clones it.)*

---

## 🔮 Future Scope

- Replace the dummy payment system with a real payment gateway integration
- Migrate from a desktop Java GUI to a web or mobile interface for wider accessibility
- Add push notifications for order status updates
- Introduce data analytics on order history to help canteen operators optimize menu and pricing decisions
- Scale to support more canteens/locations across campus

---

## 👥 Team

- **Avadhoot Virkar** — [GitHub](https://github.com/elfeyaoo)
- **Atharva Thube**
- **Akash Vidwan**

*Project Guide: Prof. Sheetal Jadhav*

---

## 📄 License

*(Add a license if you intend for others to reuse this code — MIT is a common choice for student/portfolio projects.)*
