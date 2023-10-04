$(function() {
  $.get("https://swapi-api.alx-tools.com/api/films/?format=json",
	(data, statusText) => {
	  $.each(data.results, (index, movie) => {
	    $("#list_movies").append("<li>" + movie.title + "</li>");
	  });
	}, "json");
});
