let ul = document.getElementById("ul_of_loko");

let activeId = -1;

for (let i = 10; i <= 29; i++) {
	let li = document.createElement('li');
	li.className += " nav-item loko-li";
	li.id = 'loko-' + i;
	
	li.onclick = function(e) {
		e.preventDefault();
		id = e.target.parentNode.id;
		if (activeId != -1) {
			document.getElementById(activeId).classList.remove('active');
		}
		document.getElementById(id).className += " active";
		activeId = id;
	};

	let a = document.createElement('a');
	a.className += " nav-link";
	a.innerText = "Локомотив " + i;

	li.appendChild(a);
	ul.appendChild(li);
}