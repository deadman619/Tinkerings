<?php 
$navbar = ['Log In'=>'login',
			 'Home'=>'home',
			 'Flight Details'=>'details',
			 'Order Flight' =>'order'];

function renderNav($navArray) {
	foreach ($navArray as $name=>$link):?> 
		<li><a href='?page=<?=$link?>'><?=$name?></a></li>
		<?php endforeach ?>

<?php
};