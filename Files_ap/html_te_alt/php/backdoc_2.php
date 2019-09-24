<?php
$usuario = $_POST['usertext'];
$clave = $_POST['passtext'];

if($usuario == 'jhonatan' && $clave == 'shaki11'){
	echo "BIENVENIDO";
}
else{
	echo "LA CLAVE ES ERRADA"
}
?>