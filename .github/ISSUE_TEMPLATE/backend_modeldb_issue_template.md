---
name: Backend Database Table/Model Issue
about: General template for creating a new table/model in the database, including a descriptions, and a structured format for requirements.
title: ''
labels: backend
assignees: ''

---

## Description
*Explanation of the database table/model to be created. Explain its purpose and how it will be used within the application.*

*Example: Define the database model for users, represented in a table. This model will facilitate user registration and management within the application.*

## Checklist
- **Table Structure**:  
  *Outline the structure of the database table, including each field and its properties.*
  - `field_name`: *data_type* (description)  
    *Example:*
    - `name`: `str` - The first name of the user.
    - `surname`: `str` - The last name of the user.
    - `username`: `str` - The unique username chosen by the user.
    - `email`: `str` (unique) - The user's email address, which must be unique in the database.
    - `id_user`: `int` (primary key) - A unique identifier for each user.
    - `hashed_password`: `str` - The user's password stored in a hashed format for security.

- **Models for XXX Input and Output**:  
  *Describe the models that will be created to handle user data input and output.*
  - **UserBase**: A base model that includes the essential fields for user registration (name, surname, username, and email).
  - **UserOut**: Inherits from `UserBase` and includes an additional property to return the user's ID.
  - **UsersOut**: A model that will return a list of users and the total count of users.
  - **UserCreate**: Inherits from `UserBase` and includes an additional property for the password (str).

- **Special Fields Handling**:  
  *Specify, for example, how the password will be managed within the model.*
  - The user model, `UserCreate`, should include a field for the password as a plain string, which will be hashed and stored in the `hashed_password` field.

## Additional Notes
*Not necessary field. Include any other relevant information, such as dependencies, links to documentation, or related issues that might impact the creation of this table/model.*

---