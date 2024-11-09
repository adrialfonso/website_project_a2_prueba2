---
name: Deployment Issue
about: General template for creating issues related to deployment tasks, including descriptions, and a structured checklist for deployment requirements.
title: ''
labels: deployment
assignees: ''

---

## Description
*Explanation of the deployment task. Describe what will be deployed, the environment (e.g., staging, production), and any relevant context.*

*Example: Prepare and deploy version 1.0.0 of the application to the production environment, ensuring that all new features and fixes are included.*

### Checklist
- **Pre-deployment Tasks**:  
  *List the tasks that must be completed before deployment, such as code reviews, testing, or database migrations.*
  - Verify that all pull requests have been merged into the main branch.
  - Ensure that all tests have passed successfully.
  - Perform code review on key components.

- **Deployment Steps**:  
  *Outline the specific steps required to deploy the application.*
  - Build the application using the production build command.
  - Push the built application to the production server.
  - Run database migration scripts, if applicable.

- **Configuration Changes**:  
  *Detail any configuration changes required during deployment, such as environment variables or server settings.*
  - Update the environment variables for production settings (e.g., API keys, database connection strings).

- **Post-deployment Verification**:  
  *Describe the steps to verify that the deployment was successful and that the application is functioning as expected.*
  - Check that the application is accessible in the production environment.
  - Perform smoke tests to ensure critical functionality is working.

## Additional Notes
*Not necessary. Include any other relevant information, such as links to deployment scripts, configuration files, or related issues that may influence this deployment task.*

---