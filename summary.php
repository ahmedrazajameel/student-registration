<?php session_start(); ?>
<!DOCTYPE html>
<html>
<head>
    <title>Registered Students</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<nav>
    <a href="index.php" id="nav_home">Home</a> |
    <a href="summary.php" id="nav_summary">Registered Students</a> |
    <a href="about.php" id="nav_about">About</a>
</nav>

<h2>Registered Students</h2>

<?php if (empty($_SESSION['students'])): ?>
    <p id="empty_msg">No students registered yet.</p>
<?php else: ?>
    <table border="1" cellpadding="5">
        <tr><th>Name</th><th>Email</th><th>Course</th></tr>
        <?php foreach ($_SESSION['students'] as $s): ?>
        <tr>
            <td><?php echo htmlspecialchars($s['name']); ?></td>
            <td><?php echo htmlspecialchars($s['email']); ?></td>
            <td><?php echo htmlspecialchars($s['course']); ?></td>
        </tr>
        <?php endforeach; ?>
    </table>
<?php endif; ?>

<p id="total">Total students: <?php echo count($_SESSION['students'] ?? []); ?></p>

<p><a href="index.php" id="back_link">Register Another</a></p>

</body>
</html>