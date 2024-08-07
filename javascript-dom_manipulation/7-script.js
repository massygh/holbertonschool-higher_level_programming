const moviesUri = 'https://swapi-api.hbtn.io/api/films/?format=json';
const $moviesList = $('ul#list_movies');

$.ajax({
    url: moviesUri,
    dataType: 'json',
}).done((data) => {
    const movies = data.results;

    for (let i = 0; i < movies.length; ++i) {
        const movieTitle = movies[i].title;
        const element = `<li>${moviesTitle}`;
        $moviesList.append(element);
    }
});