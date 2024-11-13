1. Outline Requirements
    Asset Display
    Update Request Submission
    Admin Control
    Admin Dashboard/Employee Portal Views
    
2. Choose Tech Stack
    Backend (Server & Database)
        Python
        MySQL
    Frontend (User Interface)
        Consider a framework like React, Vue.js, or Angular for interactive UI elements and smoother user experience.
    Authentication
        OAuth
        Firebase

3. Set Up Database
    Define Tables: Start with tables for Assets, Users, and Requests.
        Assets Table: Fields like AssetID, Description, Location, Custodian, Status, etc.
        Users Table: Fields for user info, roles (Admin, Viewer), and permissions.
        Requests Table: Fields to store requests for updates with RequestID, AssetID, RequestedBy, NewCustodian, NewLocation, Status, etc.
    Populate the Assets table with your existing data from Excel, importing it via scripts or database import tools.

4. Develop Core Features
    Asset Display (Read-Only View): Build a page that pulls data from the Assets table to show machine details. Add search and filtering options to make it easy for users to locate specific assets.
    Update Request Form: Design a form that allows users to request changes to Custodian or Location by submitting a request, which populates the Requests table.
    Admin Dashboard: Create a page where you and your boss can review pending requests, approve or deny them, and directly edit asset information.

5. Implement Role-Based Access Control
    Set up authentication and role-based permissions:
        Admins: Full access to all fields, including approval workflows for requests.
        Viewers: Limited access (read-only asset view and permission to submit requests).
    Tools like JWT (JSON Web Tokens) or Firebase Authentication can simplify this setup if you’re not using company-specific Single Sign-On.

6. Create Notification and Approval Workflow
    Implement triggers so that when a new request is submitted, an alert goes to admins.
    For approvals, have the system update the asset record and notify the requestor of the status.

7. Testing
    Conduct user testing with your team to ensure everything works as expected.
    Test Permissions: Verify that admins have full access, while other users can only view and submit requests.
    Check for edge cases, such as what happens if an invalid request is submitted.

8. Deployment
    Host the app on a cloud provider like AWS or Google Cloud to ensure accessibility across your organization.
    If you don’t want to handle server management, Heroku or Firebase Hosting are beginner-friendly options.

9. Maintenance and Scaling
    Once the system is up, track user feedback to make further improvements.
    Plan periodic backups of your data and security audits, especially for user permissions and access.