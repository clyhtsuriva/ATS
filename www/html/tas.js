function affiche_tas(){
	
	var url = "affiche-tas.py";
	
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
