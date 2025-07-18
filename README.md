# Mini Blog API

This is a simple Django project that implements a mini blog with comments functionality. It provides a RESTful API for managing blog posts and their associated comments.

## Project Structure

```
mini_blog_api
├── mini_blog_api
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd mini_blog_api
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install django djangorestframework
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

- **Blog Posts**
  - `GET /api/posts/` - List all blog posts
  - `POST /api/posts/` - Create a new blog post
  - `GET /api/posts/{id}/` - Retrieve a specific blog post
  - `PUT /api/posts/{id}/` - Update a specific blog post
  - `DELETE /api/posts/{id}/` - Delete a specific blog post

- **Comments**
  - `GET /api/posts/{post_id}/comments/` - List all comments for a specific post
  - `POST /api/posts/{post_id}/comments/` - Create a new comment for a specific post
  - `GET /api/comments/{id}/` - Retrieve a specific comment
  - `PUT /api/comments/{id}/` - Update a specific comment
  - `DELETE /api/comments/{id}/` - Delete a specific comment

## Contributing

Feel free to submit issues or pull requests for any improvements or bug fixes. 

## License

This project is licensed under the MIT License.