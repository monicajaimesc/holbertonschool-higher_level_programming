function change () {
  console.log(this);
  if ($(this).is('.red')) {
    $(this).removeClass('red');
    return 'green';
  } else {
    $(this).removeClass('green');
    return 'red';
  }
}

function toggle () {
  $('header').toggleClass(change);
}

$('div#toggle_header').click(toggle);
