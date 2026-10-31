<?php session_start(); ?>
<!DOCTYPE html>
<html>
<head>
    <title>About</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<nav>
    <a href="index.php" id="nav_home">Home</a> |
    <a href="summary.php" id="nav_summary">Registered Students</a> |
    <a href="about.php" id="nav_about">About</a>
</nav>

<h2>About This Application</h2>

<p>This is a simple Student Registration System built with PHP as part of the ITC402 Major Assignment.</p>

<p>It lets a student register for a course by entering their name, email, and chosen course. The application validates the input, stores registrations in the PHP session (no database required), and displays all registered students on the summary page.</p>

<p>The application is tested automatically with Selenium WebDriver (Python) and version-controlled with Git and GitHub.</p>

<p><a href="index.php" id="back_home">Back to Home</a></p>

</body>
</html>