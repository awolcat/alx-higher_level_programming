$(function() {
  $.get("https://hellosalut.stefanbohacek.dev/?lang=fr",
	(data, statusText) => {
	  $("#hello").text(data.hello);
	}, "json");
});
