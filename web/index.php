<!DOCTYPE html>
<html>
<body>
    <h1>The Churnbusters Team</h1>
    <ul>
        <?php
            $response = file_get_contents('http://chubs-api/');
            $chubs = json_decode($response)->churnbusters;
            foreach ($chubs as $chub) {
                echo "<li>$chub</li>";
            }
        ?>
    </ul>
</body>
</html>
