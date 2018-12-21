var ajaxData = new XMLHttpRequest();

ajaxData.onreadystatechange = function() {
	if (ajaxData.readyState === 4) {
		var goods = JSON.parse(ajaxData.responseText);
		var saleList = '<ul>';
		var dropdown = '<select class="form-control"><option value=0 default>Select Category</option>';
		for(type in goods) {
			dropdown+= '<option value=' + type + '>' + type.substring(0,1).toUpperCase()+type.slice(1) + '</option>';
			if (!type.search(category)) {
				for (let i = 0; i<goods[type].length; i++) {
					if (goods[type][i].name.match(displayGoods)) {
						saleList+='<div class="col-sm-6 product"><img src=' + 
						goods[type][i].picture + '> ' + '<p class="name">' + 
						goods[type][i].name.substring(0,1).toUpperCase()+goods[type][i].name.slice(1) + 
						'</p> <p class="price">' + goods[type][i].price.toFixed(2) + '€</p></div>';
					}
				}
			}
		}
		dropdown+='</select>';
		saleList+='</ul>';
		document.getElementById('dropdown').innerHTML = dropdown;
		document.getElementById('goods').innerHTML = saleList;
	}
}

var dropdown = document.getElementById('dropdown');
dropdown.addEventListener('change', filterCategory);

function filterCategory() {
 	category = document.getElementById('dropdown').firstChild.value;
	ajaxData.open('GET', 'data/goods.json');
	ajaxData.send();
	displayGoods = '';
 	return category;
}
function filterSearch() {
	ajaxData.open('GET', 'data/goods.json');
	ajaxData.send();
	displayGoods = document.getElementById('search').value;
	category = '';
	return displayGoods;
	}
filterSearch();
