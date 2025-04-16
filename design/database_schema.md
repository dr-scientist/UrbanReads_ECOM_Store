# UrbanReads E-Commerce Database Schema

This document outlines the initial database schema for the UrbanReads online bookstore.

## 📦 Tables Overview

### 1. Users Table

| Column Name      | Data Type    | Description                        |
|------------------|--------------|------------------------------------|
| user_id          | INT (PK)     | Unique identifier for the user     |
| full_name        | VARCHAR(100) | User’s full name                   |
| email            | VARCHAR(100) | User’s email address               |
| password_hash    | TEXT         | Encrypted password                 |
| phone_number     | VARCHAR(20)  | Contact number                     |
| address          | TEXT         | Shipping address                   |
| is_admin         | BOOLEAN      | Flag for admin accounts            |
| created_at       | TIMESTAMP    | Account creation date              |

---

### 2. Products Table

| Column Name      | Data Type    | Description                          |
|------------------|--------------|--------------------------------------|
| product_id       | INT (PK)     | Unique product ID                    |
| title            | VARCHAR(150) | Book title                           |
| author           | VARCHAR(100) | Author name                          |
| genre            | VARCHAR(50)  | Book genre (e.g., Fiction, Sci-Fi)  |
| price            | DECIMAL      | Price of the book                    |
| stock_quantity   | INT          | Inventory count                      |
| description      | TEXT         | Book description                     |
| cover_image_url  | TEXT         | URL for book cover image             |
| created_at       | TIMESTAMP    | Date the book was added              |

---

### 3. Orders Table

| Column Name      | Data Type    | Description                          |
|------------------|--------------|--------------------------------------|
| order_id         | INT (PK)     | Unique order ID                      |
| user_id          | INT (FK)     | ID of the user who placed the order  |
| total_amount     | DECIMAL      | Total cost of the order              |
| order_status     | VARCHAR(50)  | Status (e.g., Pending, Shipped)      |
| payment_status   | VARCHAR(50)  | Payment status (Paid, Failed)        |
| created_at       | TIMESTAMP    | Order placement date                 |

---

### 4. Order_Items Table

| Column Name      | Data Type    | Description                          |
|------------------|--------------|--------------------------------------|
| item_id          | INT (PK)     | Unique item ID                       |
| order_id         | INT (FK)     | Reference to Orders table            |
| product_id       | INT (FK)     | Reference to Products table          |
| quantity         | INT          | Quantity of the book ordered         |
| price_each       | DECIMAL      | Price of the item at time of order   |

---

### 5. Payments Table

| Column Name      | Data Type    | Description                          |
|------------------|--------------|--------------------------------------|
| payment_id       | INT (PK)     | Unique payment ID                    |
| order_id         | INT (FK)     | Order linked to the payment          |
| payment_method   | VARCHAR(50)  | (Credit Card, PayPal, etc.)          |
| payment_status   | VARCHAR(50)  | Paid, Failed, Refunded, etc.         |
| paid_at          | TIMESTAMP    | Date and time of payment             |

---

## 🔐 Notes on Security

- Passwords must be stored as **hashed values**, not in plain text.
- All personal data (like emails and addresses) should be encrypted in compliance with **GDPR**.
