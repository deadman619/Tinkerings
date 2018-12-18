
<?php require ('inc/data.php');	?>

<html>
<head>
	<title>Uzduotis</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>

<content class='jumbotron text-center'>
	<form action='templates/ticket.php' method='post' class='form-group'>
		<div class='col-md-2 noPad'>
			<select name='number' class="form-control">
				<?php foreach ($flightNumber as $number):?>
					<option value='<?=$number;?>'><?=$number;?></option>
				<?php endforeach ?>
			</select>
		</div>
		<div class='col-md-1 noPad'>
			<input type='text' name='customerSSN' placeholder='SSN' class="form-control" pattern='[0-9]+' required>
		</div>
		<div class='col-md-1 noPad'>
			<input type='text' name='customerName' placeholder='Name' class="form-control" required>
		</div>
		<div class='col-md-2 noPad'>
			<select id='drop1' name='flightFrom' class="form-control">
				<?php foreach ($flightFromTo as $location):?>
					<option value='<?=$location;?>'><?=$location;?></option>
				<?php endforeach ?>
			</select>
		</div>
		<div class='col-md-2 noPad'>
			<select id='drop2' name='flightTo' class="form-control">
				<?php foreach ($flightToFrom as $destination):?>
					<option value='<?=$destination;?>'><?=$destination;?></option>
				<?php endforeach ?>
			</select>
		</div>
		<div class='col-md-1 noPad'>
			<select name='bagWeight' class="form-control">
				<?php foreach ($baggage as $weight):?>
					<option value='<?=$weight;?>'><?=$weight;?></option>
				<?php endforeach ?>
			</select>
		</div>
		<div class='col-md-1 noPad'>
			<input type='text' name='price' pattern='[0-9]+' placeholder='Price' class="form-control" required>
		</div>
		<div class='col-md-2 noPad'>
			<textarea name='message' placeholder='Comments' class="form-control"></textarea>
		</div>
		<div class='col-md-offset-4 col-md-4 noPad'>
			<button type='submit' name='submit' class="btn btn-lg btn-danger topMargin" onclick="errorPrint()">Order flight</button>
				<p id='error' class='errorP'>Cannot have the same location and destination. Please choose another location or destination.</p>
		</div>
	</form>
</content>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script src="js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
<script src="js/validation.js" type="text/javascript"></script>

</body>
</html>