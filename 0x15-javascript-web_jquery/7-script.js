const url = 'https://swapi.co/api/people/5/?format=json';
$.ajax({ url: url })
  // request is done, data came from that request
  .done(function (data) {
    // console.log(data.name)
    $('#character').text(data.name);
  });
