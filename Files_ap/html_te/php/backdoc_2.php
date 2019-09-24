<?php

if(isset($_POST['user'])&&$_POST['user']=='jhonatan'){
if($_POST['pass']&&$_POST['pass']=='shaki11'){
	echo "BIENVENIDO";
}
else{
	echo "LA CLAVE ES ERRADA";
}
}else{
	echo "El usuario que ha ingresado no existe";
}

?>