function cherche(){
	
	var condition = document.getElementById("condition");
	var url = "affiche-tab.py?condition=" + condition.value;
	
	var req = new XMLHttpRequest();
	req.open("GET", url, true);
	
	req.onreadystatechange = function(){
		if(req.readyState == 4 && req.status == 200) {
			var tab=document.getElementById("tab");
			tab.innerHTML = req.responseText;
		}
	}
	
	req.send();
}
