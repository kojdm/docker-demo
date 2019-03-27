<!DOCTYPE html>
<html>
<body>
    <h1>The Churnbusters Team</h1>
    <ul>
        <?php
            $response = file_get_contents('http://127.0.0.1:5000/');
            $chubs = json_decode($response)->churnbusters;
            foreach ($chubs as $chub) {
                echo "<li>$chub</li>";
            }
        ?>
    </ul>
</body>
</html>