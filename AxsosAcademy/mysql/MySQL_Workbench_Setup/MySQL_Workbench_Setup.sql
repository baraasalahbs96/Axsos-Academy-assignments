#MySQL Workbench Setup - CRUD Queries
USE user_dashboard;

#CREATE (INSERT)
#to add user
INSERT INTO User (username, email, password_hash, role)
VALUES (‘baraa’, ‘baraa@email.com’, ‘123456hashed’, ‘admin’);
#to add project
INSERT INTO Project (owner_id, title, description, status, deadline)
VALUES (1, ‘My First Project’, ‘This is a test project’, ‘active’, ‘2026-12-31’);
#to add task
INSERT INTO Task (project_id, assigned_to, title, priority, is_done, due_date)
VALUES (1, 1, ‘Design the homepage’, ‘high’, FALSE, ‘2026-06-01’);
#to add notification
INSERT INTO Notification (user_id, message, type)
VALUES (1, ‘Your project has been created!’, ‘success’);
#to add activity
INSERT INTO Activity (user_id, action, entity_type, entity_id)
VALUES (1, ‘created’, ‘Project’, 1);
#to add setting
INSERT INTO Settings (user_id, theme, language, email_notif)
VALUES (1, ‘dark’, ‘en’, TRUE);


READ (SELECT)
#To view all users
SELECT * FROM User;
#To view all projects
SELECT * FROM Project;
#To view a specific user project
SELECT * FROM Project WHERE owner_id = 1;
#To view incomplete tasks
SELECT * FROM Task WHERE is_done = FALSE;
#To view unread notifications
SELECT * FROM Notification WHERE is_read = FALSE;
#To view specific user activity
SELECT * FROM Activity WHERE user_id = 1;


#UPDATE
#To update user name
UPDATE User SET username = ‘baraa_updated’ WHERE id = 1;
#To update project status
UPDATE Project SET status = ‘completed’ WHERE id = 1;
#To update done tasks
UPDATE Task SET is_done = TRUE WHERE id = 1;
#To update a notification as read
UPDATE Notification SET is_read = TRUE WHERE id = 1;
#To update theme
UPDATE Settings SET theme = ‘light’ WHERE user_id = 1;


#DELETE
#To delete task
DELETE FROM Task WHERE id = 1;
#To delete notification
DELETE FROM Notification WHERE id = 1;
#To delete project (it will automatically delete because of CASCADE)
DELETE FROM Project WHERE id = 1;
#To delete user (its informations will automatically delete because of CASCADE)
DELETE FROM User WHERE id = 1;