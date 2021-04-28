
<?php
	$query = $_GET["q"];
	
	$command = 'python videoengagement.py ' . $query;
	$output = json_decode(exec($command), true);
	
	$outputStr = "<div><table style = \"width: 100%\">";
	$max = $output[21];
	if($max == 0)
		$outputStr .= "<tr><td>No Video Found</td></tr>";
	if($max > 20)
		$max = 20;
	else
		for($i = 0; $i < $max; $i++)
		{
			$outputStr .= "<tr><td>" . $output[$i][0] . "</td><td>" . $output[$i][1] . "</td></tr>";
		}
	$outputStr .= "</table></div>";
	
	echo $output;
	//echo $outputStr;
?>