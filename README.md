
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

## Usage

- **Admin Panel**: Access the Django admin panel at `http://localhost:8000/admin` to manage coupons and user profiles.
- **Dining Staff Interface**: Use the provided interfaces to validate and redeem dining coupons.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/) - High-level Python web framework
- [Bootstrap](https://getbootstrap.com/) - Front-end framework for responsive web design
- [SQL](https://www.postgresql.org/) - Advanced open-source database management system
```
