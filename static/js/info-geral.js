$(document).ready(function () {
    $(function () {
        fetch('https://apigsw.herokuapp.com/data/horas/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("horasgeral").append(dados);
            });
    });
});