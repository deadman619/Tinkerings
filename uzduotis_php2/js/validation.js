function errorPrint() {
		var a = document.getElementById('drop1');
		var b = document.getElementById('drop2');
		var valueFrom = a.options[a.selectedIndex].value;
		var valueTo = b.options[b.selectedIndex].value;
		console.log(valueFrom);
		console.log(valueTo);
		if (valueFrom == valueTo) {
			document.getElementById("error").style.opacity='1';
			event.preventDefault();
			return false;
		} else {
			document.getElementById("error").style.opacity='0';
		}
	}