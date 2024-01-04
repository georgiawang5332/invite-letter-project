/* ----------------------------------
*************************************
Dashboard Sidebar START
CodePen Home
Pro Sidebar Template with Bootstrap 4
*************************************
------------------------------------*/
var app = {
	submitForm: function (event) {
		"use strict";

		var b = document.getElementById("theButton"),
			thank = document.getElementById("thankyou"),
			isComing = document.getElementById("comingYes").checked === true,
			isBringing = document.getElementById("bringingYes").checked === true,
			names = document.getElementById("persons").value.trim(),
			message = "",
			inputs = document.getElementsByTagName("input");

		event.preventDefault();

		b.innerHTML = "Sending...";
		window.setTimeout(function () {
			b.innerHTML = "Thanks!";
			b.className += " sent";

			if (!isComing) {
				message = "Too bad you can't make it :(";
			} else {
				if (!isBringing) {
					message = "See you on the 18th then :)";
				} else if (names !== "") {
					message = "See you and " + names.split(", ").join(" and ") + " the 18th!";
				} else {
					message = "See you guys the 18th!";
				}
			}
			thank.innerHTML = message;

			for (var i = 0; i < inputs.length; i += 1) {
				inputs[i].setAttribute("disabled", true);
			}
		}, 900);
	},

	init: function () {
		"use strict";

		document.getElementById("theForm").onsubmit = app.submitForm;
	}
};

app.init();
/* ----------------------------------
*************************************
Dashboard Sidebar START
CodePen Home
Pro Sidebar Template with Bootstrap 4
*************************************
------------------------------------*/
