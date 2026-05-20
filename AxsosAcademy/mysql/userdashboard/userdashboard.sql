CREATE DATABASE IF NOT EXISTS user_dashboard;
USE user_dashboard;

CREATE TABLE User (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    username      VARCHAR(100) NOT NULL UNIQUE,
    email         VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    avatar_url    VARCHAR(255),
    role          ENUM('admin', 'member', 'viewer') DEFAULT 'member',
    created_at    DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Project (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    owner_id    INT NOT NULL,
    title       VARCHAR(150) NOT NULL,
    description TEXT,
    status      ENUM('active', 'completed', 'archived') DEFAULT 'active',
    deadline    DATE,
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_id) REFERENCES User(id) ON DELETE CASCADE
);

CREATE TABLE Task (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    project_id  INT NOT NULL,
    assigned_to INT,
    title       VARCHAR(200) NOT NULL,
    priority    ENUM('low', 'medium', 'high') DEFAULT 'medium',
    is_done     BOOLEAN DEFAULT FALSE,
    due_date    DATE,
    FOREIGN KEY (project_id)  REFERENCES Project(id) ON DELETE CASCADE,
    FOREIGN KEY (assigned_to) REFERENCES User(id)    ON DELETE SET NULL
);

CREATE TABLE Notification (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    user_id     INT NOT NULL,
    message     TEXT NOT NULL,
    type        ENUM('info', 'warning', 'success', 'error') DEFAULT 'info',
    is_read     BOOLEAN DEFAULT FALSE,
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE
);

CREATE TABLE Activity (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    user_id     INT NOT NULL,
    action      VARCHAR(150) NOT NULL,
    entity_type VARCHAR(50),
    entity_id   INT,
    timestamp   DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE
);

CREATE TABLE Settings (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    user_id     INT NOT NULL UNIQUE,
    theme       ENUM('light', 'dark') DEFAULT 'light',
    language    VARCHAR(10) DEFAULT 'en',
    email_notif BOOLEAN DEFAULT TRUE,
    updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE
);

