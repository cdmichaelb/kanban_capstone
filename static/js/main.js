// Toggle display of id edit-form when edit edit-button is clicked
let print = console.log; //TODO: Remove later
$(document).ready(function () {
	console.log("Loaded");
	$("#mainNavbar").show("fast");
	$("#loginButton").click(function (event) {
		event.preventDefault();
		$("#loginForm").show("fast");
		$("#registerForm").hide("fast");
	});
	$("#registerButton").click(function (event) {
		event.preventDefault();
		$("#registerForm").show("fast");
		$("#loginForm").hide("fast");
	});
	$("#navLoginButton").click(function (event) {
		event.preventDefault();
		$("#loginForm").show("slow");
		$("#registerForm").hide("slow");
	});
	$("#navRegisterButton").click(function (event) {
		event.preventDefault();
		$("#registerForm").show("slow");
		$("#loginForm").hide("slow");
	});
	/* 	$(".loginSubmit").click(function (event) {
		event.preventDefault();
		console.log("Login submit");
		//$("#kanbanApp").show("fast");
		$("#loginForm").hide("fast");
		$("#registerForm").hide("fast");
	}); */
	$("#kanban-list-page-kanban-button").click(function (event) {
		event.preventDefault();
		//$("#kanban-list-page").hide("fast");
		$("#kanban-detail-page").show("fast");
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
	mounted() {
		$("#loginApp").show();
		console.log("ready");
	},
});

const app2 = new Vue({
	delimiters: ["[[", "]]"],
	el: "#kanbanApp",
	data: {
		csrfToken: document.getElementsByName("csrfmiddlewaretoken")[0],
		kanbans: {
			id: "{{kanban.id}}",
			name: "{{kanban.name}}",
			description: "{{kanban.description}}",
			created_by: "{{kanban.created_by}}",
			created_at: "{{kanban.created_at}}",
			updated_at: "{{kanban.updated_at}}",
			columns: [
				{
					id: "{{column.id}}",
					column_index: "{{column.column_index}}",
					name: "{{column.name}}",
					description: "{{column.description}}",
					created_by: "{{column.created_by}}",
					created_at: "{{column.created_at}}",
					updated_at: "{{column.updated_at}}",
					cards: [
						{
							id: "{{card.id}}",
							index: "{{card.index}}",
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
		newColumnName: "",
		newColumnDescription: "",
		newCardName: "",
		newCardDescription: "",
		kanban_count: 0,
		componentKey: 0,
	},
	mounted() {},
	created: function () {
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
				this.kanbans = response.data.kanbans_list;
				this.kanbans.columns = response.data.columns;
				this.kanbans.cards = response.data.card_list;
				this.kanbans.columns.cards = response.data.card_list;
				this.kanban_count = Object.values(response.data).length;
			})
			.catch((error) => {
				console.log(BASE_URL);
				console.log(error);
			});
	},
	methods: {
		deleteKanban: function (kanban_id) {
			axios({
				method: "DELETE",
				url: BASE_URL + "/kanban/delete/" + kanban_id,
			})
				.then((response) => {
					console.log("deleted");
					this.kanbans = response.data.kanbans_list;
					this.kanbans.columns = response.data.column_list;
					this.kanbans.cards = response.data.card_list;
					this.kanbans.columns.cards = response.data.card_list;
					this.kanban_count = Object.values(response.data.kanbans_list).length;
				})
				.catch((error) => {
					console.log(BASE_URL);
					console.log(error);
				});
		},
		moveCard: function (card_id, direction) {
			axios({
				method: "PUT",
				url: BASE_URL + "/card/move/" + card_id,
				data: {
					direction: direction,
				},
			})
				.then((response) => {
					console.log("moved");
					console.log(response.data.column_list);
					this.kanbans.columns = response.data.column_list;
				})
				.catch((error) => {
					console.log(BASE_URL);
					console.log(error);
				});
		},

		forceRerender() {
			this.componentKey += 1;
			//this.$forceUpdate();
		},
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
					this.kanbans = response.data.kanban_list;
					this.kanbans.columns = [];
					this.kanban_count = Object.values(response.data).length;
					this.kanban_count = this.kanban_count + 1;
				})
				.catch((error) => {
					console.log(BASE_URL);
					console.log(error);
				});
		},
		getColumns: function (kanban) {
			axios({
				method: "GET",
				url: BASE_URL + "/column/" + kanban,
			})
				.then((response) => {
					this.kanbans.columns = response.data.column_list;
				})
				.catch((error) => {
					console.log(BASE_URL);
					console.log(error);
				});
		},
		viewKanban: function (kanban) {
			console.log(kanban);
			axios({
				method: "GET",
				url: BASE_URL + "/detail/" + kanban,
			})
				.then((response) => {
					$("#kanban-list-page").hide("fast");
					$("#kanban-detail-page").show("fast");
					this.kanbans = response.data;
					this.getColumns(kanban);
				})
				.catch((error) => {
					console.log(BASE_URL);
					console.log(error);
				});
		},
		backToList: function () {
			$("#kanban-list-page").show("fast");
			$("#kanban-detail-page").hide("fast");
		},
		createColumn: function () {
			axios({
				method: "POST",
				url: BASE_URL + "/column/",
				data: {
					name: this.newColumnName,
					description: this.newColumnDescription,
					kanban: this.kanbans.id,
					column: this.kanbans.columns.id,
					column_index: this.kanbans.columns.length,
				},
			})
				.then((response) => {
					//console.log("Column: " + JSON.stringify(response.data.column_list));
					this.kanbans.columns = response.data.column_list;
					this.kanbans.columns.cards = response.data.card_list;
				})
				.catch((error) => {
					console.log(BASE_URL);
					console.log(error);
				});
		},
		createCard: function (column) {
			axios({
				method: "POST",
				url: BASE_URL + "/card/",
				data: {
					name: this.newCardName,
					description: this.newCardDescription,
					column: column,
				},
			})
				.then((response) => {
					console.log("card created");
					console.log(JSON.stringify(response.data));
					this.kanbans.column = response.data.column;
					this.kanbans.columns = response.data.column_list;
					this.kanbans.columns.cards = response.data.card_list;
					app2.$forceUpdate();
				})
				.catch((error) => {
					console.log(BASE_URL);
					console.log(error);
				});
		},
		updateKanban: function (kanban) {
			axios({
				method: "PUT",
				url: BASE_URL + "/update/" + kanban,
				data: {
					name: this.newName,
					description: this.newDescription,
				},
			})
				.then((response) => {
					console.log(response.data);
					this.kanbans = response.data;
				})
				.catch((error) => {
					console.log(BASE_URL);
					console.log(error);
				});
		},
		updateColumn: function (column) {
			axios({
				method: "PUT",
				url: BASE_URL + "/column/update/" + column,
				data: {
					name: this.newName,
					description: this.newDescription,
				},
			})
				.then((response) => {
					console.log(response.data);
					this.kanbans = response.data;
				})
				.catch((error) => {
					console.log(BASE_URL);
					console.log(error);
				});
		},
		updateCard: function (card) {
			axios({
				method: "PUT",
				url: BASE_URL + "/card/update/" + card,
				data: {
					name: this.newName,
					description: this.newDescription,
				},
			})
				.then((response) => {
					console.log(response.data);
					this.kanbans = response.data;
				})
				.catch((error) => {
					console.log(BASE_URL);
					console.log(error);
				});
		},
		deleteColumn: function (column) {
			axios({
				method: "DELETE",
				url: BASE_URL + "/column/delete/" + column,
			})
				.then((response) => {
					console.log(response.data);
					this.kanbans = response.data;
				})
				.catch((error) => {
					console.log(BASE_URL);
					console.log(error);
				});
		},
		deleteCard: function (card) {
			axios({
				method: "DELETE",
				url: BASE_URL + "/card/delete/" + card,
			})
				.then((response) => {
					console.log(response.data);

					this.kanbans.columns = response.data.column_list;
					this.kanbans.columns.cards = response.data.card_list;
					//this.kanbans = response.data;
				})
				.catch((error) => {
					console.log(BASE_URL);
					console.log(error);
				});
		},
	},
});
