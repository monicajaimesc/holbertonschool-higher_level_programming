function newHeader () {
  $('header').text('New Header!!!');
}

function init () {
  $('DIV#update_header').click(newHeader);
}

$(document).ready(init);
