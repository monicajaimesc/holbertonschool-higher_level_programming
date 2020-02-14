const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.ajax({ url: url })
  .done(function (data) {
    $('#hello').text(data.hello);
  });