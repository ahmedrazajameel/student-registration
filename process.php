<?php
session_start();

$name   = trim($_POST['name'] ?? '');
$email  = trim($_POST['email'] ?? '');
$course = $_POST['course'] ?? '';
$errors = [];

if (strlen($name) < 3) {
    $errors[] = "Name must be at least 3 characters.";
}

if (!preg_match("/^[a-zA-Z ']+$/", $name)) {
    $errors[] = "Name may contain only letters, spaces, and apostrophes.";
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errors[] = "Please enter a valid email address.";
}

if ($course === '') {
    $errors[] = "Please select a course.";
}

if ($errors) {
    $_SESSION['errors'] = $errors;
    header("Location: index.php");
    exit;
}

if (!isset($_SESSION['students'])) {
    $_SESSION['students'] = [];
}
$_SESSION['students'][] = [
    'name'   => $name,
    'email'  => $email,
    'course' => $course
];

header("Location: summary.php");
exit;