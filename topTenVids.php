
<?php
	/* TESTER DATA UNCOMMENT LINE TO REMOVE
	for($i = 0; $i < 10; $i++)
	{
		$output[$i]= $i * ($i);
		$output[$i] .= " TEST";
	}
	//*/
	$command = escapeshellcmd('python topvideos.py');
	$output = json_decode(exec($command), true);
	$outputStr = "<div class = \"flexContainerVert\">";
	for($i = 0; $i < 10; $i++)
	{
		$outputStr .= "<div>" . $output[$i] . "</div>";
	}
	$outputStr .= "</div>";

	echo($outputStr);
?>