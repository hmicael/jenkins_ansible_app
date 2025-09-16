<?php
    // Connexion à la base de données MySQL
    $servername = "localhost";
    $username = "henintsoa";
    $password = "1698henintsoa";
    $dbname = "demo_app";

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "SELECT id, nom, email FROM utilisateurs";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        echo "<table border='1'>
                <tr><th>ID</th><th>Nom</th><th>Email</th></tr>";
        while($row = $result->fetch_assoc()) {
            echo "<tr>
                    <td>" . $row["id"] . "</td>
                    <td>" . htmlspecialchars($row["nom"]) . "</td>
                    <td>" . htmlspecialchars($row["email"]) . "</td>
                  </tr>";
        }
        echo "</table>";
    } else {
        echo "0 results";
    }

    $conn->close();
