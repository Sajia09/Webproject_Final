# Hall Dining Coupon Management System

## Overview

The Hall Dining Coupon Management System is a Django-based application designed to efficiently manage dining coupons for hall residents. The system facilitates the issuance, validation, and tracking of dining coupons, improving resource management and user experience.

## Features

- **Coupon Issuance**: Allows admins to issue dining coupons with specified values and expiration dates.
- **Coupon Validation**: Enables dining staff to validate and redeem coupons at the time of use.
- **Real-Time Tracking**: Provides real-time tracking of coupon status and usage.
- **User Management**: Manages resident profiles and their associated coupons.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) (v3.8 or later)
- [Django](https://www.djangoproject.com/) (v4.0 or later)
- [SQL](https://www.postgresql.org/) (for database management, optional)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hall-dining-coupon-management.git
2. Navigate to the project directory:
   ```bash
   cd hall-dining-coupon-management
3.Create a virtual environment:
  ```bash
   python -m venv env

4. Activate the virtual environment:
```bash
   env\Scripts\activate

5.Install the required dependencies:
```bash
   pip install -r requirements.txt
6.Create a .env file in the root directory with the following content:
```bash
   DEBUG=True
   SECRET_KEY=your_secret_key
   DATABASE_URL=postgres://user:password@localhost:5432/hall_dining


