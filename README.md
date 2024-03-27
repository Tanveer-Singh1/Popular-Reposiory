<h1>Python MySQL Database Interaction</h1>

<p>This Python project facilitates interaction with a MySQL database. It offers functionalities to view existing tables, create new tables, and insert values into tables seamlessly.</p>

<h2>Installation</h2>

<ol>
  <li><strong>Clone the Repository:</strong><br>
    <code>git clone https://github.com/Tanveer-Singh1/Popular-Reposiory</code></li>
  <li><strong>Install Dependencies:</strong><br>
    <code>pip install pymysql</code></li>
</ol>

<h2>Usage</h2>

<ol>
  <li><strong>Run the Script:</strong><br>
    <code>python Interactive_SQL_Table_Manager.py</code></li>
  <li><strong>Available Options:</strong>
    <ul>
      <li><strong>1: Details of Tables</strong><br>
        View the details of existing tables in the database.</li>
      <li><strong>2: Create New Table</strong><br>
        Create a new table in the database by specifying table name and column details.</li>
      <li><strong>3: Insert Values into Table</strong><br>
        Insert values into an existing table by selecting the table and providing values for each column.</li>
      <li><strong>'N': Quit</strong><br>
        Quit the application.</li>
    </ul>
  </li>
</ol>

<h2>Functionality Details</h2>

<ol>
  <li><strong>Viewing Existing Tables (<code>showtables</code>)</strong><br>
    This function lists all the tables in the database and allows the user to select a table to view its contents.</li>
  <li><strong>Creating New Table (<code>create_table</code>)</strong><br>
    Create a new table in the database by specifying the table name and column details. The user can choose from predefined data types for each column.</li>
  <li><strong>Inserting Values into Table (<code>insert_into_table</code>)</strong><br>
    Insert values into an existing table by selecting the table and providing values for each column. The user is guided through the process of entering values for each column.</li>
</ol>

<h2>Dependencies</h2>

<ul>
  <li><strong>pymysql:</strong> This library is used to interact with the MySQL database from Python.</li>
</ul>

<h2>Contributing</h2>

<p>Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or feature suggestions.</p>
