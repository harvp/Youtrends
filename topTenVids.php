
<?php
	
	$command = escapeshellcmd('python topvideos.py');
	$output = json_decode(exec($command), true);
	$command2 = escapeshellcmd('python topvideos.py a');
	$output2 = json_decode(exec($command2), true);
	$outputStr = "<div class = \"flexContainerVert\">";
	for($i = 0; $i < 10; $i++)
	{
		$outputStr .= "<div>" . $output[$i][0] . " Engagement Score: " . $output2[$i][0] . "</div>";
	}
	$outputStr .= "</div>";

	echo($outputStr);
?>