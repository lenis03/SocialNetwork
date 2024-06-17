# SocialNetwork

SocialNetwork is a Django-based web application that allows users to register, log in, create posts, comment on posts, like/dislike posts, and follow/unfollow other users. This project includes user authentication, profile management, and a basic social feed.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  - [Account Endpoints](#account-endpoints)
  - [Home Endpoints](#home-endpoints)
- [License](#license)
- [Contributing](#contributing)
- [URL Configuration](#url-configuration)

## Features

- User Registration and Login
- Profile Management
- Follow/Unfollow Users
- Create, Update, and Delete Posts
- Comment on Posts
- Like/Dislike Posts
- Password Reset

## Installation

To get started with SocialNetwork, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/lenis03/SocialNetwork.git
    cd SocialNetwork
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

Once the server is running, you can use the following URLs to access different parts of the application:

- **Homepage:** `http://localhost:8000/`
- **Admin Panel:** `http://localhost:8000/admin/`
- **User Registration:** `http://localhost:8000/account/register/`
- **User Login:** `http://localhost:8000/account/login/`

## API Endpoints

### Account Endpoints

- `GET /account/register/` - Register a new user
- `POST /account/register/` - Create a new user
- `GET /account/login/` - User login
- `POST /account/login/` - Authenticate user
- `GET /account/logout/` - User logout
- `GET /account/profile/<int:user_id>/` - View user profile
- `GET /account/edit-profile/` - Edit user profile
- `POST /account/edit-profile/` - Save edited profile
- `GET /account/follow/<int:user_id>/` - Follow a user
- `GET /account/unfollow/<int:user_id>/` - Unfollow a user
- `GET /account/following/<int:user_id>/` - List of users the user is following
- `GET /account/followers/<int:user_id>/` - List of users following the user
- `GET /account/password-reset/` - Password reset form
- `POST /account/password-reset/` - Send password reset email
- `GET /account/password-reset/done/` - Password reset done
- `GET /account/password-reset/confirm/<uidb64>/<token>/` - Confirm password reset
- `POST /account/password-reset/confirm/<uidb64>/<token>/` - Complete password reset
- `GET /account/password-reset/complete/` - Password reset complete

### Home Endpoints

- `GET /` - List of all posts
- `GET /post/<int:post_id>/<slug:post_slug>/` - Post detail view
- `GET /post/create/` - Create a new post
- `POST /post/create/` - Save a new post
- `GET /post/update/<int:post_id>/` - Update a post
- `POST /post/update/<int:post_id>/` - Save updated post
- `GET /post/delete/<int:post_id>/` - Delete a post
- `POST /post/<int:post_id>/comment/` - Add a comment to a post
- `POST /post/<int:post_id>/comment/<int:comment_id>/reply/` - Reply to a comment
- `GET /post/<int:post_id>/like/` - Like a post
- `GET /post/<int:post_id>/dislike/` - Dislike a post

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
