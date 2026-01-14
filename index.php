<?php

// ------------------------------------------------------------
// DATABASE CONNECTION
// ------------------------------------------------------------

$db = mysqli_connect("localhost", "root", "", "bot");

if (!$db) {
    exit("Database connection error");
}

// ------------------------------------------------------------
// INPUT PARAMETERS
// ------------------------------------------------------------

$phone = $_GET['telefone'] ?? '';
$clientMessage = $_GET['msg'] ?? '';
$userEmail = $_GET['usuario'] ?? '';

if ($phone === '' || $clientMessage === '') {
    exit("Invalid request parameters");
}

// ------------------------------------------------------------
// USER LOOKUP
// ------------------------------------------------------------

$sql = "SELECT * FROM usuario WHERE telefone = '$phone'";
$result = mysqli_query($db, $sql);
$totalRows = mysqli_num_rows($result);

$status = 0;
$botReply = "";

// ------------------------------------------------------------
// NEW CLIENT
// ------------------------------------------------------------

if ($totalRows === 0) {

    mysqli_query(
        $db,
        "INSERT INTO usuario (telefone, status) VALUES ('$phone', 1)"
    );

    $status = 1;

    $botReply =
        "Hello! Welcome to Prime Mobile Store.\n\n" .
        "We specialize in the sale of smartphones from leading brands.\n\n" .
        "Please reply with one of the options below:\n" .
        "1️⃣ View available smartphones\n" .
        "2️⃣ Check prices and promotions\n" .
        "3️⃣ Financing and payment plans\n" .
        "4️⃣ Speak with a sales consultant";

} else {

    // --------------------------------------------------------
    // EXISTING CLIENT
    // --------------------------------------------------------

    $row = mysqli_fetch_assoc($result);
    $status = (int)$row['status'];

    if ($status === 1) {

        $botReply =
            "Thank you for your interest.\n\n" .
            "Please choose what you would like to see:\n" .
            "1️⃣ Latest smartphone models\n" .
            "2️⃣ Android devices\n" .
            "3️⃣ iPhone devices\n" .
            "4️⃣ Best value-for-money options";

    } elseif ($status === 2) {

        $botReply =
            "Great choice.\n\n" .
            "Select the category you are most interested in:\n" .
            "1️⃣ Entry-level smartphones\n" .
            "2️⃣ Mid-range smartphones\n" .
            "3️⃣ Premium smartphones\n" .
            "4️⃣ Current promotions";

    } elseif ($status === 3) {

        $botReply =
            "Almost done.\n\n" .
            "How would you like to proceed?\n" .
            "1️⃣ Receive detailed specifications\n" .
            "2️⃣ View current offers and prices\n" .
            "3️⃣ Simulate financing options\n" .
            "4️⃣ Talk to a sales consultant";

    } elseif ($status === 4) {

        $botReply =
            "Final step.\n\n" .
            "Please confirm your next action:\n" .
            "1️⃣ Proceed with purchase\n" .
            "2️⃣ Request contact from a consultant\n" .
            "3️⃣ Receive catalogs and product links\n" .
            "4️⃣ End conversation";

    } else {

        $botReply =
            "Thank you for contacting Prime Mobile Store.\n" .
            "We remain available whenever you need assistance.";

        mysqli_query(
            $db,
            "UPDATE usuario SET status = 1 WHERE telefone = '$phone'"
        );

        echo $botReply;
        exit;
    }

    // --------------------------------------------------------
    // STATUS UPDATE
    // --------------------------------------------------------

    $status++;
    mysqli_query(
        $db,
        "UPDATE usuario SET status = $status WHERE telefone = '$phone'"
    );
}

// ------------------------------------------------------------
// MESSAGE HISTORY
// ------------------------------------------------------------

$timestamp = date("Y-m-d H:i:s");

mysqli_query(
    $db,
    "INSERT INTO historico (telefone, msg_cliente, msg_bot, data)
     VALUES ('$phone', '$clientMessage', '$botReply', '$timestamp')"
);

// ------------------------------------------------------------
// OUTPUT
// ------------------------------------------------------------

echo $botReply;
