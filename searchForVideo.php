
<?php
	$query = $_GET["q"];
	
	/*TESTER DATA UNCOMMENT LINE TO REMOVE
	for($i = 0; $i < 5; $i++)
	{
		$output[$i] = $i;
		$output[$i] .= " " . ($i * $i);
	}
	// */
	$command = 'python searchforvideo.py ' . $query;
	$output = json_decode(exec($command), true);
	
	$outputStr = "<div><table style = \"width: 100%\">";
	$max = $output[6];
	if($max == 0)
		$outputStr .= "<tr><td>No Video Found</td></tr>";
	else
		for($i = 0; $i < $max; $i++)
		{
			$outputStr .= "<tr><td>" . $output[$i][0] . "</td><td>" . $output[$i][1] . "</td></tr>";
		}
	$outputStr .= "</table></div>";
	
	echo $outputStr;
?>