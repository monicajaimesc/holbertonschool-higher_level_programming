const url = 'https://swapi.co/api/films/?format=json';
$.ajax({ url: url })
  .done(function (data) {
    data.results.forEach( function (index) {
      // console.log(index)
      $('#list_movies').append(`<li>${index.title}</li>`);
      // $('#list_movies').append('<li>'+index.title+'</li>');
    });
    });
  