// Toggle display of id edit-form when edit edit-button is clicked
let print = console.log; //TODO: Remove later

$(document).ready(function () {
	$("#edit-form").toggle();
	$("#edit-button").click(function () {
		$("#edit-form").toggle();
	});
});

const BASE_URL = "";

const app = new Vue({
	delimiters: ["[[", "]]"],
	el: "#loginApp",
	data: {
		csrfToken: document.getElementsByName("csrfmiddlewaretoken")[0],
		user: {
			username: "{{user.username}}",
			email: "{{user.email}}",
			first_name: "{{user.first_name}}",
			last_name: "{{user.last_name}}",
			id: "{{user.id}}",
		},
	},
	created: function () {
		axios.defaults.xsrfHeaderName = "X-CSRFToken";
		axios.defaults.headers = {
			"Content-Type": "application/json",
			"X-CSRFToken": this.csrfToken.value,
		};
		console.log("created");
		axios({
			method: "GET",
			url: BASE_URL + "/users/account/",
		})
			.then((response) => {
				this.user = response.data;
				console.log(this.user);
			})
			.catch((error) => {
				console.log(BASE_URL);
				console.log(error);
			});
	},
});

const app2 = new Vue({
	delimiters: ["[[", "]]"],
	el: "#kanbanApp",
	data: {
		csrfToken: document.getElementsByName("csrfmiddlewaretoken")[0],
		kanban: {
			id: "{{kanban.id}}",
			name: "{{kanban.name}}",
			description: "{{kanban.description}}",
			created_by: "{{kanban.created_by}}",
			created_at: "{{kanban.created_at}}",
			updated_at: "{{kanban.updated_at}}",
			columns: [
				{
					id: "{{column.id}}",
					name: "{{column.name}}",
					description: "{{column.description}}",
					created_by: "{{column.created_by}}",
					created_at: "{{column.created_at}}",
					updated_at: "{{column.updated_at}}",
					cards: [
						{
							id: "{{card.id}}",
							name: "{{card.name}}",
							description: "{{card.description}}",
							created_by: "{{card.created_by}}",
							created_at: "{{card.created_at}}",
							updated_at: "{{card.updated_at}}",
						},
					],
				},
			],
		},
		newName: "",
		newDescription: "",
		kanbans: 0,
	},
	created: function () {
		this.newName = "";
		this.newDescription = "";
		//this.kanbans = 0;
		axios.defaults.xsrfHeaderName = "X-CSRFToken";
		axios.defaults.headers = {
			"Content-Type": "application/json",
			"X-CSRFToken": this.csrfToken.value,
		};
		console.log("created");
		axios({
			method: "GET",
			url: BASE_URL + "/kanban/",
		})
			.then((response) => {
				this.kanban = response.data;
				console.log(response.data);
				this.kanbans = Object.values(response.data).length;
			})
			.catch((error) => {
				console.log(BASE_URL);
				console.log(error);
			});
	},
	methods: {
		createKanban: function () {
			axios({
				method: "POST",
				url: BASE_URL + "/create/",
				data: {
					name: this.newName,
					description: this.newDescription,
				},
			})
				.then((response) => {
					this.kanban = response.data;
					this.kanbans = this.kanbans + 1;
				})
				.catch((error) => {
					console.log(BASE_URL);
					console.log(error);
				});
		},
	},
});
