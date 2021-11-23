<html>
    <head>
        <title>ACP Times with Restful API</title>
    </head>

    <body>
        <ul>
        <h1>listAll</h1>
            <?php
            $json = file_get_contents('http://laptop-service/listAll');
            $obj = json_decode($json);
	          $OpenTimes = $obj->Open;
                  $CloseTimes = $obj->Close;
            foreach ($OpenTimes as $opentime) {
                echo "<li>Open: $opentime</li>";
            }
            foreach ($CloseTimes as $closetime) {
                echo "<li>Close: $closetime</li>";
            }
            ?>

        <h1>listOpenOnly</h1>
            <?php
            $json = file_get_contents('http://laptop-service/listOpenOnly');
            $obj = json_decode($json);
                $OpenTimes = $obj->Open;
            foreach ($OpenTimes as $opentime) {
                echo "<li>Open: $opentime</li>";
            }
            ?>

        <h1>listCloseOnly</h1>
            <?php
            $json = file_get_contents('http://laptop-service/listCloseOnly');
            $obj = json_decode($json);
                $CloseTimes = $obj->Close;
            foreach ($CloseTimes as $closetime) {
                echo "<li>Close: $closetime</li>";
            }
            ?>

        <h1>listAllCSV</h1>
            <?php
            echo file_get_contents('http://laptop-service/listAll/csv');
            ?>

        <h1>listOpenOnlyCSV</h1>
            <?php
            echo file_get_contents('http://laptop-service/listOpenOnly/csv');
            ?>

        <h1>listCloseOnly</h1>
            <?php
            echo file_get_contents('http://laptop-service/listCloseOnly/csv');
            ?>

        <h1>listAllJSON</h1>
            <?php
            $json = file_get_contents('http://laptop-service/listAll/json');
            $obj = json_decode($json);
                $OpenTimes = $obj->Open;
                $CloseTimes = $obj->Close;
            foreach ($CloseTimes as $closetime) {
                echo "<li>Close: $closetime</li>";
            }
            foreach ($OpenTimes as $opentime) {
                echo "<li>Open: $opentime</li>";
            }
            ?>

        <h1>listOpenOnlyJSON</h1>
            <?php
            $json = file_get_contents('http://laptop-service/listOpenOnly/json');
            $obj = json_decode($json);
                $OpenTimes = $obj->Open;
            foreach ($OpenTimes as $opentime) {
                echo "<li>Open: $opentime</li>";
            }
            ?>

        <h1>listCloseOnlyJSON</h1>
            <?php
            $json = file_get_contents('http://laptop-service/listCloseOnly/json');
            $obj = json_decode($json);
                $CloseTimes = $obj->Close;
            foreach ($CloseTimes as $closetime) {
                echo "<li>Close: $closetime</li>";
            }
            ?>

        <h1>Top 3 Open CSV</h1>
            <?php
            echo file_get_contents('http://laptop-service/listOpenOnly/csv?top=3');
            ?>

        <h1>Top 5 Open JSON</h1>
            <?php
            $json = file_get_contents('http://laptop-service/listOpenOnly/json?top=5');
            $obj = json_decode($json);
                $OpenTimes = $obj->Open;
            foreach ($OpenTimes as $opentime) {
                echo "<li>Open: $opentime</li>";
            }
            ?>

        <h1>Top 6 Close CSV</h1>
            <?php
            echo file_get_contents('http://laptop-service/listCloseOnly/csv?top=6');
            ?>

        <h1>Top 4 Close JSON</h1>
            <?php
            $json = file_get_contents('http://laptop-service/listCloseOnly/json?top=4');
            $obj = json_decode($json);
                $CloseTimes = $obj->Close;
            foreach ($OpenTimes as $opentime) {
                echo "<li>Open: $opentime</li>";
            }
            ?>

        </ul>
    </body>
</html>
>
