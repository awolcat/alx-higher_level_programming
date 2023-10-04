$(function() {
  $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json",
	(data, responseStatus) => {
	  $("#character").text(data.name);
	}, "json");
});
