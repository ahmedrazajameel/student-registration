<?php session_start(); ?>
<!DOCTYPE html>
<html>
<head>
    <title>Student Registration</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
</head>
<body>

<nav>
    <a href="index.php" id="nav_home">Home</a> |
    <a href="summary.php" id="nav_summary">Registered Students</a> |
    <a href="about.php" id="nav_about">About</a>
</nav>

<h2>Student Registration</h2>

<?php if (isset($_SESSION['errors'])): ?>
    <div style="color:red;">
        <?php foreach ($_SESSION['errors'] as $e): ?>
            <p><?php echo htmlspecialchars($e); ?></p>
        <?php endforeach; ?>
    </div>
    <?php unset($_SESSION['errors']); ?>
<?php endif; ?>

<form action="process.php" method="POST">
    <label>Name: <input type="text" name="name" id="name"></label><br><br>
    <label>Email: <input type="text" name="email" id="email"></label>
    <span id="email_hint" style="margin-left:10px;"></span><br><br>
    <label>Course:
        <select name="course" id="course">
            <option value="">--Select--</option>
            <option value="ITC402">ITC402</option>
            <option value="ITC401">ITC401</option>
            <option value="ITC403">ITC403</option>
        </select>
    </label><br><br>
    <button type="submit" id="submit">Register</button>
</form>

<p><a href="summary.php" id="summary_link">View Registered Students</a></p>

</body>
</html>