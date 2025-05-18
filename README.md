# Meme Stream backend 🐸🎉

**Meme Stream backend** is a full-stack web application where users can create, view, and interact with memes. It includes user profiles, comments, and voting functionality. Built with Django and Django REST Framework on the backend, and designed to integrate seamlessly with a modern frontend (React, etc.).

## 🚀 Features

- Create, update, delete memes (posts)
- Comment on memes
- Upvote/downvote memes
- User profiles with auto-generated avatars (if none provided)
- Filter posts:
  - New
  - Top (24h, Week, All Time)
- API endpoints to fetch:
  - Posts by ID
  - Posts by user email
  - Comments by post ID
  - Users by email

---

## 🛠 Tech Stack

- **Backend Framework**: Django, Django REST Framework
- **Database**: SQLite
- **Media Storage**: Local file storage (customizable)
- **Avatar Generation**: Dicebear API
- **Deployment**: Railway.app or any other platform

---

## 📂 Project Structure

```
memehub/
├── api/ # Main app
│ ├── models.py # Post, Comment, User_profile
│ ├── views.py # ViewSets for APIs
│ ├── serializers.py # DRF serializers
│ ├── urls.py # API routes
├── media/ # Uploaded media (profile pics)
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yash-bisht711/backend-Memehub.git
cd backend-Memehub
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Apply migrations
```
python manage.py migrate
```

### 4. Run the development server
```
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/`.

## 📤 API Endpoints

### Posts

| Method | Endpoint                      | Description          |
| ------ | ----------------------------- | -------------------- |
| GET    | `/api/posts/`                 | List all posts       |
| POST   | `/api/posts/`                 | Create a post        |
| GET    | `/api/posts/<id>/`            | Get a post by ID     |
| PUT    | `/api/posts/<id>/`            | Update a post        |
| DELETE | `/api/posts/<id>/`            | Delete a post        |
| GET    | `/api/posts/new/`             | Get newest posts     |
| GET    | `/api/posts/top_day/`         | Top posts (24h)      |
| GET    | `/api/posts/top_week/`        | Top posts (Week)     |
| GET    | `/api/posts/top_all/`         | Top posts (All Time) |
| GET    | `/api/posts/by-user/<email>/` | Posts by user email  |

### Comments

| Method | Endpoint                           | Description         |
| ------ | ---------------------------------- | ------------------- |
| GET    | `/api/comments/`                   | List all comments   |
| POST   | `/api/comments/`                   | Create a comment    |
| GET    | `/api/comments/by-post/<post_id>/` | Comments for a post |


### Users

| Method | Endpoint                       | Description       |
| ------ | ------------------------------ | ----------------- |
| GET    | `/api/users/`                  | List all users    |
| POST   | `/api/users/`                  | Create a user     |
| GET    | `/api/users/by-email/<email>/` | Get user by email |


---

## 📸 Profile Picture Handling

- If a user does not upload a profile picture, an avatar is automatically generated using the Dicebear API.
- The avatar is saved to the profile_picture field on first save.

--

## 📃 License

This project is licensed under the MIT License.

---

## 🙌 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.