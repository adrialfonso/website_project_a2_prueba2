#  Software Engineering Project: ReadHub

## 1. Project Description  
Desciption of the Project and Bussiness value


## 2. Technologies used
This project incorporates the following technologies:
- **Frontend**: 
  - **Vue** - A framework for building the user interface.
  - **HTML/CSS** - For basic structure and styling.
  - **Bootstrap** - CSS framework for responsive design.
  - **JavaScript** - Core programming language for dynamic front-end interactions.
  - **HTTP/Axios** - Request service that connect frontend to backend.
- **Backend**:
  - **FastAPI** - A web framework for Python backend development.
  - **Python** - Programming language for backend logic and API development.
- **Database**: 
  - **MySQL** - Main relational database for storing user and book data.
  - **SQL** - Language used to manage and query the database.
- **Services**: 
  - **Cloud Server** - Hosting and deploying the application on a cloud-based environment.

## 3. Project Structure
In the project, two different applications are defined: the backend and the frontend.

The **backend (server)** refers to the part of an application that is not visible to users. Its functions include:  
* Business Logic: Implements the rules and processes related to the application.
* Database: Stores and manages the application's data.
* Security: Implements access policies to the application and its data, managing user authentication and authorization.
* Processes Requests (API): Handles requests from the frontend.

The **frontend (client)** is primarily concerned with user interaction. It takes care of:
* Page Design: Visual organization of information and its navigation.
* Buttons and Forms: Interactive elements that users can engage with.
* Visual Content: Images, videos, and text.

### 3.1 Directory Structure
Here is how the directory structure look:
```
/website_project_a2
├── /backend                     # Backend application folder
│   ├── /alembic                 # Database migrations directory
│   ├── /app                    
│   │   ├── /api                 # API related code
│   │   │   └──/routes           # Route definitions for the API
│   │   ├── /core                # Core functionalities (settings, utilities)
│   │   ├── /crud                # CRUD operations logic
│   │   ├── /models              # Database models
│   │   ├── /tests               # Tests for the backend
│   │   └── app.py               # Main application file
│   ├── requirements.txt         # Backend dependencies
│   ├── config.py                # Configuration settings for the backend
│   ├── main.py                  # Entry point for the application
│   ├── .env                     # Environment variables (API keys, database URLs)
│   └── README.md                # Documentation specific to the backend
├── /frontend                    # Frontend application folder
│   ├── /config                  # Configuration files for the frontend
│   │   ├── .env.local               # Local environment variables (APIurl backend)
│   ├── /src                     # Source code for the frontend application
│   │   ├── /assets              # Images, styles, and other assets
│   │   ├── /components          # Reusable Vue components
│   │   ├── /views               # Vue views of the application
│   │   ├── /router              # Vue router configuration
│   │   ├── /services            # API service calls for the backend
│   │   ├── App.vue              # Root Vue component
│   │   ├── main.js              # Entry point for the frontend application
│   │   └── http-common.js       # Common HTTP settings for API calls
│   ├── package.json             # Frontend dependencies
│   └── README.md                # Documentation specific to the frontend
├── .gitignore                   # Git ignore file to exclude certain files/folders from version control
└── README.md                    # Project documentation (overall)
```
This structure mainly separates the logic of the frontend and backend while keeping easy access to both.

The description of the main directories and files within the project:

#### **Backend** (`/backend`)
The backend folder manages server-side operations, handling the core application logic, API routes, 
database interactions, and business logic. Contains the backend code, developed with FastAPI in Python.

- **`/alembic`**: Contains files for handling database migrations.
- **`/app`**: Core backend code, including API routes and main business logic.
  - **`/api`**: Defines the API routes and controllers, handling HTTP requests and responses.
  - **`/core`**: Includes app settings and utility functions.
  - **`/crud`**: Contains CRUD (Create, Read, Update, Delete) operation logic to interact with the database.
  - **`/models`**: Defines the database models, representing tables and relationships used in the application.
  - **`/tests`**: Holds the unit tests to validate backend functionality.
  - **`app.py`**: Main application file where the FastAPI app is initialized and configured.
- **`requirements.txt`**: Lists all the Python dependencies required by the backend, allowing easy setup and deployment.
- **`config.py`**: Central configuration file for environment-specific settings like database URL and API keys.
- **`main.py`**: Entry point for the backend application, running the FastAPI server.
- **`.env`**: Stores environment variables such as API keys and database connection URLs.

#### **Frontend** (`/frontend`)
The frontend folder manages the client-side interface, handling user interactions and page structure.

- **`/config`**: Configuration files specific to the frontend environment.
- **`/src`**: The source code directory for the Vue.js frontend application.
  - **`/assets`**: Contains static assets like images and CSS files used across the app.
  - **`/components`**: Houses reusable Vue components for UI elements, promoting modular and organized code.
  - **`/router`**: Contains Vue Router configuration, defining the navigation paths for the application.
  - **`/services`**: Manages API service calls, creating a centralized place for handling backend requests.
- **`package.json`**: Lists the dependencies required for the frontend, along with scripts for building and running the app.

## 4. Roles and Tasks 
Each team member has specific roles to ensure efficient project development:

- **Frontend Developers**: Responsible for designing and implementing the user interface using Vue.js. Focuses on responsiveness, UI/UX, and managing client-side logic.
- **Backend Developers**: Handle server-side logic, API development, database management, and user authentication with FastAPI and MySQL.
- **DevOps**: Automates deployment pipelines, manages cloud infrastructure, and monitors the application’s health in production.
- **QA Testers**: Conduct manual and automated testing to ensure functionality and resolve bugs before deployment.

## 5. Branching & Code Integration 
To structured development workflow, BookHub follows the GitFlow branching model.

### 5.1 GitFlow Model
The **GitFlow** model structures development work into several branch types, each with a specific purpose:

1. **Main Branch (`main`)**:
   - This is the production branch containing the stable, deployable version of the application.
   - Only tested and approved release versions are merged into `main`.

2. **Develop Branch (`develop`)**:
   - The branch for development work, contains the features before release.
   - New features, user story, and fixes are merged into `develop` from feature branches.
   - Once `develop` reaches a stable state with completed features for a new release, it is branched into a `release` branch.

3. **Feature/User Story Branches (`userstory/US<number>-<description>`)**:
   - Created off `develop` for each new feature or user story.
   - Each feature branch isolates the development of a specific feature or functionality.
   - Once completed and reviewed, feature branches are merged into `develop` through a pull request.

4. **Task Branches (`task/US<number>_Task<number>-<description>`)**:
   - These branches are sub-branches of specific **User Story** branches, for tasks of a larger feature.
   - When tasks are complete, they are merged back into their respective User Story branch.

5. **Release Branches (`release/<version>`)**:
   - Created from `develop` when the codebase is ready for a new release and feature testing is complete.
   - Any final modifications are made within the `release` branch to prepare the code for production.
   - Once finalized, the `release` branch is merged into both `main` (for deployment) and `develop` (to ensure the codebase remains synchronized).

6. **Hotfix Branches (`hotfix/<version>`)**:
   - Created from `main` to address urgent issues found after release.
   - Once the issue is resolved, the `hotfix` branch is merged into both `main` and `develop`.

### 5.2 Pull Request Process
1. **Initial Commit**: Make the first commit to initialize the branch.
2. **Verify Functionality**: Ensure the branch works as intended, with no issues.
3. **Create a Pull Request**: Open a pull request to the branch from which it originated (e.g., `develop` or the relevant User Story branch).
4. **Code Review**: Each PR is reviewed by at least one team member, who checks the code for adherence to project requirements.
5. **Merge After Approval**: Once the review is approved and all tests pass, the branch is merged into `develop` or the appropriate User Story branch.

### 5.3 Branch Naming Convention

All the branches names in the project follow the structure:

- **User Story Branches**: `userstory/US<number>-<description>`
  - Example: `userstory/US1-sign-up`
  
- **Task Branches**: `task/US<number>_Task<number>-<description>`
  - Example: `task/US1_Task1-frontend-signup`
  
- **Release Branches**: `release/<version>`
  - Example: `release/v1.0`
  
- **Hotfix Branches**: `hotfix/<version>`
  - Example: `hotfix/v1.0.1`

