### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  A database

- What is the difference between SQL and PostgreSQL?
  PostgreSQL supports Python, PHP, Perl, Tcl, Net, C, C++, Delphi, Java, JavaScript (Node. js), and more. SQL Server is more limited, offering support for Java, JavaScript

- In `psql`, how do you connect to a database?
  psql -d database_name -U user_name

- What is the difference between `HAVING` and `WHERE`?
  WHERE clause allows you to filter data from specific rows.
  HAVING clause allows you to filter data from a group of rows in a query based on conditions involving aggregate values.

- What is the difference between an `INNER` and `OUTER` join?
  Inner join keep only the information from both tables.
  Outer join keep information that is not related to the other table in the resulting table.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  A left outer join contains all records of the "left" table.
  A right outer join contains all records in the "right" able.
- What is an ORM? What do they do?
  A piece of software designed to translate between the data representations used by databases and those used in object-oriented programming.

- What are some differences between making HTTP requests using AJAX
  and from the server side using a library like `requests`?
  In ajax request, the current window/document is unaffected but the server side request will refresh the window.
- What is CSRF? What is the purpose of the CSRF token?
  A CSRF token is a secure random token that is used to prevent CSRF attacks.

- What is the purpose of `form.hidden_tag()`?
  To hide the CSRF token
