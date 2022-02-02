// Toggle display of id edit-form when edit edit-button is clicked
let print = console.log; //TODO: Remove later

$(document).ready(function () {
	$("#edit-form").toggle();
	$("#edit-button").click(function () {
		$("#edit-form").toggle();
	});
});

const BASE_URL = "{% url 'users:account' %}";
const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0];
console.log(BASE_URL);
console.log(csrfToken.value);
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.headers = {
	"Content-Type": "application/json",
	"X-CSRFToken": csrfToken.value,
};

const app = new Vue({
	delimiters: ["[[", "]]"],
	el: "#loginApp",
	data: {
		user: {
			username: "{{user.username}}",
			email: "{{user.email}}",
			first_name: "{{user.first_name}}",
			last_name: "{{user.last_name}}",
			id: "{{user.id}}",
		},
		created: function () {
			console.log("created");
			axios({
				method: "GET",
				url: BASE_URL,
			})
				.then((response) => {
					this.user = response.data;
					console.log(this.user);
				})
				.catch((error) => {
					console.log(error);
				});
		},
	},
});
