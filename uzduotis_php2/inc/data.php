<?php 

$flightNumber = [10000,rand(10000,99999),rand(10000,99999),rand(10000,99999),rand(10000,99999),rand(10000,99999),rand(10000,99999),rand(10000,99999)];
$flightFromTo = ['Lithuania', 'Germany', 'England', 'USA', 'Japan', 'India', 'Norway', 'Spain', 'Australia', 'Russia', 'Canada', 'Antarctica'];
$flightToFrom = ['Lithuania', 'Germany', 'England', 'USA', 'Japan', 'India', 'Norway', 'Spain', 'Australia', 'Russia', 'Canada', 'Antarctica'];
$baggage = ['<20kg', '>=20kg'];
shuffle($flightFromTo);
$flightDate = date('j. M, Y', strtotime('+ 30 days'));
$baggageExtra = 0;

if(isset($_POST['submit'])) {
		$flight = $_POST['number'];
		$SSN = $_POST['customerSSN'];
		$name = $_POST['customerName'];
		$flightFrom = $_POST['flightFrom'];
		$flightTo = $_POST['flightTo'];
		$bagWeight = $_POST['bagWeight'];
		$price = $_POST['price'];
		if ($bagWeight == end($baggage)) {
			global $baggageExtra;
			$baggageExtra = 30;
		}
		$message = $_POST['message'];
} 