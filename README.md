
# Hall Dining Coupon Management System

## Overview

The Hall Dining Coupon Management System is a Django-based application designed to efficiently manage dining coupons for hall residents. The system facilitates the issuance, validation, and tracking of dining coupons, improving resource management and user experience.
![image](https://github.com/user-attachments/assets/3785fda3-c92b-4cba-98b7-e0fc45dcca09)

## Features

- **Coupon Issuance**: Allows admins to issue dining coupons with specified values and expiration dates.
- **Coupon Validation**: Enables dining staff to validate and redeem coupons at the time of use.
- **Real-Time Tracking**: Provides real-time tracking of coupon status and usage.
- **User Management**: Manages resident profiles and their associated coupons.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) (v3.8 or later)
- [Django](https://www.djangoproject.com/) (v4.0 or later)
- [PostgreSQL](https://www.postgresql.org/) (for database management, optional)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/hall-dining-coupon-management.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd hall-dining-coupon-management
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv env
   ```

4. **Activate the virtual environment:**
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

5. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Set up the environment variables:**
   Create a `.env` file in the root directory with the following content:
   ```
   DEBUG=True
   SECRET_KEY=your_secret_key
   DATABASE_URL=postgres://user:password@localhost:5432/hall_dining
   ```

7. **Apply migrations to set up the database:**
   ```bash
   python manage.py migrate
   ```

8. **Create a superuser to access the admin panel:**
   ```bash
   python manage.py createsuperuser
   ```

9. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

10. **Access the application:**
    Open your browser and go to `http://localhost:8000`.


## Demo video
https://github.com/user-attachments/assets/ebc59834-ff96-48a3-a908-56034e0c543f

## Powerpoint Presentation
[web_group2_ppt.pptx](https://github.com/user-attachments/files/16919422/web_group2_ppt.pptx)




