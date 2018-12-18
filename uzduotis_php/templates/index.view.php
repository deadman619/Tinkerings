<?php include ('./inc/data.php');	?>

<html>
<head>
	<title>Uzduotis</title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
</head>
<body>
	<h2 class='text-center'>Forma</h2>
	<form action='' class='text-center'>
		<label>First name</label>
		<input type='text' name='firstName'><br>
		<label>Last name</label>
		<input type='text' name='lastName'><br>
		<label>E-mail</label>
		<input type='text' name='name'><br>
	</form>


	<table class='table table-striped text-center'>
		<tr>
			<th class='text-center'>Klase</th>
			<th class='text-center'>Kodas</th>
			<th class='text-center'>Vardas</th>
			<th class='text-center'>Pavarde</th>
			<th class='text-center'>Kontroliniu darbu vidurkis</th>
			<th class='text-center'>Duomenu formavimo data</th>
		</tr>
<?php
	foreach ($mokiniai['klase'] as $klasesNumeris => $mokinioInfo):?> 
		<?php foreach ($mokinioInfo as $duomenuPavadinimas => $informacija):?>
			<tr><td><?=$klasesNumeris;?></td>
				<td><?=$mokinioInfo[$duomenuPavadinimas]['Kodas'];?></td>
				<td><?=$mokinioInfo[$duomenuPavadinimas]['Vardas'];?></td>
				<td><?=$mokinioInfo[$duomenuPavadinimas]['Pavarde'];?></td>
				<td><?=number_format((intval($mokinioInfo[$duomenuPavadinimas]['Kontroliniu darbu ivertinimai']['Matematika'])
				 + intval($mokinioInfo[$duomenuPavadinimas]['Kontroliniu darbu ivertinimai']['Informatika'])
				 + intval($mokinioInfo[$duomenuPavadinimas]['Kontroliniu darbu ivertinimai']['Anglu']))/3, 2);?></td>
				<td><?=$mokinioInfo[$duomenuPavadinimas]['Duomenu formavimo data'];?></td></tr>
		<?php endforeach ?>
	<?php endforeach ?>
<?php
?>

<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
</body>
</html>