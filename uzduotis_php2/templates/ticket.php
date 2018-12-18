<?php require ('../inc/data.php')?>

<!DOCTYPE html>
<html>
<head>
	<title>Bilietas</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="../css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<link href="https://fonts.googleapis.com/css?family=Dancing+Script" rel="stylesheet">
	<link rel="stylesheet" type="text/css" href="../css/ticketStyle.css">
</head>
<body>
	<div class='container-fluid'>
		<header class='jumbotron ticketPage'>
			<h2>Flight: <?=$flight?></h2>
			<div class='row flightInfo'>
				<div class='col-xs-8'>
					<div class='col-xs-4'>
						<h4>Flight date:<?=$flightDate?></h4>
					</div>
					<div class='col-xs-1'>
						<p>From:</p>
						<p>To:</p>
					</div>
					<div class='col-xs-2'>
						<h4><?=$flightFrom?></h4>
						<h4><?=$flightTo?></h4>
					</div>
				</div>
				<div class='col-xs-4'>
					<h2>Total price: <?=$price+$baggageExtra?>€</h2>
					<p class='price'>Ticket price: <?=$price?>€</p>
					<p class='price'>Baggage price: <?=$baggageExtra?>€</p>
					<?if($message):?><p>Message:<?=$message?></p>
				</div>
				<div>
					<h3>Passenger: <?=$name?></h3>
					<h3>SSN: <?=$SSN?></h3>
				</div>
			</div>
		</header>
</div>






<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script src="../js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
</body>
</html>

<?php