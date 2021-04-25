<?php
	$command = escapeshellcmd('python test.py');
	$output = exec($command);
	
	var_dump($output);
	print($output);
	?>