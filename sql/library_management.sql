-- File: library_management.sql
-- Assignment: Build a Complete Database Management System
-- Description: MySQL database for a Library Management System
-- Student: bravonokoth
-- Date: April 25, 2025

-- Drop existing tables to ensure clean setup
DROP TABLE IF EXISTS Loans;
DROP TABLE IF EXISTS BookAuthors;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Authors;
DROP TABLE IF EXISTS Members;
DROP TABLE IF EXISTS Categories;

-- Table: Categories (Stores book categories/genres)
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(50) NOT NULL UNIQUE,
    Description TEXT
) COMMENT 'Stores book categories such as Fiction, Non-Fiction, etc.';

-- Table: Members (Stores library member information)
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Phone VARCHAR(20),
    JoinDate DATE NOT NULL DEFAULT (CURRENT_DATE),
    Address VARCHAR(255)
) COMMENT 'Stores information about library members';

-- Table: Authors (Stores author information)
CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Nationality VARCHAR(50)
) COMMENT 'Stores information about book authors';

-- Table: Books (Stores book information)
CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    ISBN VARCHAR(13) NOT NULL UNIQUE,
    PublicationYear INT,
    CategoryID INT NOT NULL,
    TotalCopies INT NOT NULL CHECK (TotalCopies >= 0),
    AvailableCopies INT NOT NULL CHECK (AvailableCopies >= 0),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE RESTRICT
) COMMENT 'Stores book details with category reference';

-- Table: BookAuthors (Many-to-Many relationship between Books and Authors)
CREATE TABLE BookAuthors (
    BookID INT,
    AuthorID INT,
    PRIMARY KEY (BookID, AuthorID),
    FOREIGN KEY (BookID) REFERENCES Books(BookID) ON DELETE CASCADE,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE
) COMMENT 'Links books to their authors (M-M relationship)';

-- Table: Loans (Stores book borrowing information)
CREATE TABLE Loans (
    LoanID INT AUTO_INCREMENT PRIMARY KEY,
    BookID INT NOT NULL,
    MemberID INT NOT NULL,
    LoanDate DATE NOT NULL DEFAULT (CURRENT_DATE),
    DueDate DATE NOT NULL,
    ReturnDate DATE,
    Fine DECIMAL(5,2) DEFAULT 0.00 CHECK (Fine >= 0),
    FOREIGN KEY (BookID) REFERENCES Books(BookID) ON DELETE RESTRICT,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE RESTRICT
) COMMENT 'Tracks book loans with references to Books and Members';

-- Insert Sample Data
-- Categories
INSERT INTO Categories (CategoryName, Description) VALUES
    ('Fiction', 'Fictional literature including novels and short stories'),
    ('Non-Fiction', 'Factual books including biographies and essays'),
    ('Science Fiction', 'Speculative fiction exploring futuristic concepts');

-- Members
INSERT INTO Members (FirstName, LastName, Email, Phone, JoinDate, Address) VALUES
    ('John', 'Doe', 'john.doe@email.com', '1234567890', '2025-01-01', '123 Main St'),
    ('Jane', 'Smith', 'jane.smith@email.com', '0987654321', '2025-02-01', '456 Oak Ave'),
    ('Emily', 'Clark', 'emily.clark@email.com', '5551234567', '2025-03-01', '789 Pine Rd');

-- Authors
INSERT INTO Authors (FirstName, LastName, Nationality) VALUES
    ('J.K.', 'Rowling', 'British'),
    ('Isaac', 'Asimov', 'American'),
    ('Chinua', 'Achebe', 'Nigerian');

-- Books
INSERT INTO Books (Title, ISBN, PublicationYear, CategoryID, TotalCopies, AvailableCopies) VALUES
    ('Harry Potter and the Sorcerer''s Stone', '9780590353427', 1997, 1, 10, 8),
    ('Foundation', '9780553293357', 1951, 3, 5, 4),
    ('Things Fall Apart', '9780385474542', 1958, 1, 7, 6);

-- BookAuthors (Linking Books to Authors)
INSERT INTO BookAuthors (BookID, AuthorID) VALUES
    (1, 1), -- Harry Potter by J.K. Rowling
    (2, 2), -- Foundation by Isaac Asimov
    (3, 3); -- Things Fall Apart by Chinua Achebe

-- Loans
INSERT INTO Loans (BookID, MemberID, LoanDate, DueDate, ReturnDate, Fine) VALUES
    (1, 1, '2025-04-01', '2025-04-15', NULL, 0.00), -- John Doe borrows Harry Potter
    (2, 2, '2025-04-10', '2025-04-24', '2025-04-20', 0.00), -- Jane Smith borrows Foundation
    (3, 3, '2025-04-15', '2025-04-29', NULL, 2.50); -- Emily Clark borrows Things Fall Apart