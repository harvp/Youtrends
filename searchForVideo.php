
<?php
	$query = $_GET["q"];
	
	// /*TESTER DATA UNCOMMENT LINE TO REMOVE
	for($i = 0; $i < 5; $i++)
	{
		$output[$i] = $i;
		$output[$i] .= " " . ($i * $i);
	}
	// */
	//$command = escapeshellarg('python searchforvideo.py $query');
	//$output = json_decode(exec($command));
	$title;
	$number;
	for($i = 0; $i < 5; $i++)
	{
		$title[$i] = substr($output[$i], 0, strripos($output[$i], " "));
		$number[$i] = substr($output[$i], strripos($output[$i], " "));
	}
	$outputStr = "<div><table style = \"width: 100%\">";
	for($i = 0; $i < 5; $i++)
	{
		$outputStr .= "<tr><td>" . $title[$i] . "</td><td>" . $number[$i] . "</td></tr>";
	}
	$outputStr .= "</table></div>";
	
	echo $outputStr;
?>