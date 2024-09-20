# **Lisang API Documentation**

## **Base URL:**
```
http://127.0.0.1:8000
```

---

## **Authentication Routes**

### **Register a New User**
- **Endpoint:** `/register/`
- **Method:** `POST`
- **Description:** Registers a new user on the platform.
- **Request Body:**
  ```json
  {
    "username": "john_doe",
    "email": "john.doe@example.com",
    "password": "securepassword"
  }
  ```
- **Response:**
  ```json
  {
    "message": "User registered successfully",
    "user_id": 1234
  }
  ```

### **Login User**
- **Endpoint:** `/login/`
- **Method:** `POST`
- **Description:** Authenticates a user and returns a token for authenticated requests.
- **Request Body:**
  ```json
  {
    "email": "john.doe@example.com",
    "password": "securepassword"
  }
  ```
- **Response:**
  ```json
  {
    "token": "JWT-TOKEN-HERE"
  }
  ```

### **Authentication Check**
- **Endpoint:** `/auth-check/`
- **Method:** `GET`
- **Authentication:** `Bearer token`
- **Description:** Validates if the current token is valid.
- **Response:**
  ```json
  {
    "message": "Token is valid",
    "user": {
      "id": 1234,
      "username": "john_doe"
    }
  }
  ```

---

## **User Management**

### **Get All Users**
- **Endpoint:** `/users/`
- **Method:** `GET`
- **Authentication:** `Bearer token`
- **Description:** Retrieves a list of all users.
- **Response:**
  ```json
  [
    {
      "id": 1234,
      "username": "john_doe",
      "email": "john.doe@example.com",
      "is_active": true
    },
    {
      "id": 1235,
      "username": "jane_doe",
      "email": "jane.doe@example.com",
      "is_active": false
    }
  ]
  ```

### **Create a New User**
- **Endpoint:** `/users/create/`
- **Method:** `POST`
- **Authentication:** `Bearer token`
- **Description:** Allows an admin to create a new user manually.
- **Request Body:**
  ```json
  {
    "username": "new_user",
    "email": "new_user@example.com",
    "password": "newpassword"
  }
  ```
- **Response:**
  ```json
  {
    "message": "User created successfully",
    "user_id": 1236
  }
  ```

### **Update User**
- **Endpoint:** `/users/update/<int:pk>/`
- **Method:** `PUT`
- **Authentication:** `Bearer token`
- **Description:** Updates details of a specific user.
- **Request Body:**
  ```json
  {
    "username": "updated_user",
    "email": "updated_user@example.com",
    "is_active": true
  }
  ```
- **Response:**
  ```json
  {
    "message": "User updated successfully"
  }
  ```

### **Delete User**
- **Endpoint:** `/users/delete/<int:pk>/`
- **Method:** `DELETE`
- **Authentication:** `Bearer token`
- **Description:** Deletes a specific user from the platform.
- **Response:**
  ```json
  {
    "message": "User deleted successfully"
  }
  ```

### **Activate User**
- **Endpoint:** `/users/activate/<int:pk>/`
- **Method:** `PATCH`
- **Authentication:** `Bearer token`
- **Description:** Activates a deactivated user.
- **Response:**
  ```json
  {
    "message": "User activated successfully"
  }
  ```

### **Deactivate User**
- **Endpoint:** `/users/deactivate/<int:pk>/`
- **Method:** `PATCH`
- **Authentication:** `Bearer token`
- **Description:** Deactivates an active user.
- **Response:**
  ```json
  {
    "message": "User deactivated successfully"
  }
  ```

---

## **Event Management**

### **Get All Events**
- **Endpoint:** `/events/`
- **Method:** `GET`
- **Description:** Retrieves a list of all events.
- **Response:**
  ```json
  [
    {
      "id": 5678,
      "name": "Cultural Festival",
      "location": "Douala, Cameroon",
      "date": "2024-10-05",
      "time": "18:00",
      "category": "Festival"
    },
    {
      "id": 5679,
      "name": "Music Concert",
      "location": "Yaoundé, Cameroon",
      "date": "2024-11-15",
      "time": "20:00",
      "category": "Concert"
    }
  ]
  ```

### **Create a New Event**
- **Endpoint:** `/events/create/`
- **Method:** `POST`
- **Authentication:** `Bearer token`
- **Description:** Allows organizers to create a new event.
- **Request Body:**
  ```json
  {
    "name": "Art Exhibition",
    "description": "A showcase of local artists.",
    "location": "Douala, Cameroon",
    "date": "2024-12-01",
    "time": "10:00",
    "category": "Exhibition"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Event created successfully",
    "event_id": 5680
  }
  ```

### **Update Event**
- **Endpoint:** `/events/update/<int:pk>/`
- **Method:** `PUT`
- **Authentication:** `Bearer token`
- **Description:** Updates an existing event's details.
- **Request Body:**
  ```json
  {
    "name": "Updated Art Exhibition",
    "description": "A larger showcase of artists.",
    "date": "2024-12-02",
    "time": "11:00"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Event updated successfully"
  }
  ```

### **Delete Event**
- **Endpoint:** `/events/delete/<int:pk>/`
- **Method:** `DELETE`
- **Authentication:** `Bearer token`
- **Description:** Deletes an event.
- **Response:**
  ```json
  {
    "message": "Event deleted successfully"
  }
  ```

### **Get Event Details**
- **Endpoint:** `/events/detail/<int:pk>/`
- **Method:** `GET`
- **Description:** Retrieves detailed information about a specific event.
- **Response:**
  ```json
  {
    "id": 5678,
    "name": "Cultural Festival",
    "description": "A vibrant celebration of local culture",
    "location": "Douala, Cameroon",
    "date": "2024-10-05",
    "time": "18:00",
    "category": "Festival"
  }
  ```

### **Get My Events**
- **Endpoint:** `/events/my-events/`
- **Method:** `GET`
- **Authentication:** `Bearer token`
- **Description:** Retrieves a list of events created by the authenticated user.
- **Response:**
  ```json
  [
    {
      "id": 5678,
      "name": "Cultural Festival",
      "location": "Douala, Cameroon",
      "date": "2024-10-05",
      "time": "18:00"
    }
  ]
  ```

---

## **Category Management**

### **Get All Categories**
- **Endpoint:** `/categories/`
- **Method:** `GET`
- **Description:** Retrieves all event categories.
- **Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Concert"
    },
    {
      "id": 2,
      "name": "Festival"
    }
  ]
  ```

### **Create a Category**
- **Endpoint:** `/categories/create/`
- **Method:** `POST`
- **Authentication:** `Bearer token`
- **Description:** Allows admins to create a new event category.
- **Request Body:**
  ```json
  {
    "name": "Workshop"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Category created successfully",
    "category_id": 3
  }
  ```

### **Update Category**
- **Endpoint:** `/categories/update/<int:pk>/`
- **Method:** `PUT`
- **Authentication:** `Bearer token`
- **Description:** Updates an existing event category.
- **Request Body:**
  ```json
  {
    "name": "Updated Category"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Category updated successfully"
  }
  ```

### **Delete Category**
- **Endpoint:** `/categories/delete/<int:pk>/`
- **Method:** `DELETE`
- **Authentication:** `Bearer token`
- **Description:** Deletes a specific event category.
- **Response:**
