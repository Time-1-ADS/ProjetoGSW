//Tasks Abertas

//fetch('https://apigsw.herokuapp.com/data/horas/albuquerque/')
//    .then(function (response) {
//        return response.json();
//    })
//    .then(function (dados) {
//        document.write(dados[1][1])
//    });
var albhora = document.getElementById('albhora').getContext('2d');

function hora(){
    fetch('https://apigsw.herokuapp.com/data/horas/albuquerque/')
    .then(function (response) {
        return response.json();
    })
    .then(function (dados) {
        document.write(dados[1])
    });
}