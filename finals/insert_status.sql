INSERT INTO students (first_name, last_name, birth_date, gender_id, email_address, contact_number, nationality_id, address_street, degree_code, student_status)
VALUES
('John', 'Doe', '2008-01-01', FLOOR(RAND() * 2) + 1, 'johndoe@example.com', '09123456789', FLOOR(RAND() * 194) + 1, '123 Main St', FLOOR(RAND() * 72) + 145, 1),
('Jane', 'Smith', '2009-02-02', FLOOR(RAND() * 2) + 1, 'janesmith@example.com', '09987654321', FLOOR(RAND() * 194) + 1, '456 Elm St', FLOOR(RAND() * 72) + 145, 1),
('Michael', 'Johnson', '2010-03-03', FLOOR(RAND() * 2) + 1, 'michaeljohnson@example.com', '09876543210', FLOOR(RAND() * 194) + 1, '789 Oak St', FLOOR(RAND() * 72) + 145, 1),
('Emily', 'Brown', '2011-04-04', FLOOR(RAND() * 2) + 1, 'emilybrown@example.com', '09765432109', FLOOR(RAND() * 194) + 1, '101 Pine St', FLOOR(RAND() * 72) + 145, 1),
('David', 'Miller', '2012-05-05', FLOOR(RAND() * 2) + 1, 'davidmiller@example.com', '09654321098', FLOOR(RAND() * 194) + 1, '202 Cedar St', FLOOR(RAND() * 72) + 145, 1),
('Sarah', 'Davis', '2013-06-06', FLOOR(RAND() * 2) + 1, 'sarahdavis@example.com', '09543210987', FLOOR(RAND() * 194) + 1, '303 Maple St', FLOOR(RAND() * 72) + 145, 1),
('James', 'Wilson', '2014-07-07', FLOOR(RAND() * 2) + 1, 'jameswilson@example.com', '09432109876', FLOOR(RAND() * 194) + 1, '404 Oak St', FLOOR(RAND() * 72) + 145, 1),
('Olivia', 'Moore', '2015-08-08', FLOOR(RAND() * 2) + 1, 'oliviamoore@example.com', '09321098765', FLOOR(RAND() * 194) + 1, '505 Pine St', FLOOR(RAND() * 72) + 145, 1),
('William', 'Taylor', '2016-09-09', FLOOR(RAND() * 2) + 1, 'williamtaylor@example.com', '09210987654', FLOOR(RAND() * 194) + 1, '606 Cedar St', FLOOR(RAND() * 72) + 145, 1),
('Sophia', 'Anderson', '2017-10-10', FLOOR(RAND() * 2) + 1, 'sophiaanderson@example.com', '09109876543', FLOOR(RAND() * 194) + 1, '707 Maple St', FLOOR(RAND() * 72) + 145, 1);