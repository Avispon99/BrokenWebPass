
<?php

$username = $_POST['usertext'];
$password = $_POST['passtext'];

if(isset($username)&& $username=='jhona'){
if(isset($password) && $password == 'shaki'){

	$open_file = fopen('script_ht.html','r');
	$read_f='';

	while(!feof($open_file)){
		$lin=fgets($open_file);
		$read_f=$read_f.$lin;
	}

	fclose($open_file);

	echo 'WELCOME '.$username.'<br>'.$read_f;
}

else{
	echo "<br>THE PASS IS INCORRECT";
}

}
else{
	echo 'No exist';
}




?>




