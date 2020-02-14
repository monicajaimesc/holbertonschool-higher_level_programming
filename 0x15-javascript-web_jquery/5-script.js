function Li () {
  $('UL.my_list').append('<li>Item</li>');
}

function init () {
  $('DIV#add_item').click(Li);
}

$(document).ready(init);
