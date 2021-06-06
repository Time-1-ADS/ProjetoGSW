$(document).ready(function () {
    $(function () {
        fetch('https://apigsw.herokuapp.com/data/horas/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("horasgeral").append(dados);
            });
        fetch('https://apigsw.herokuapp.com/data/mediahoras/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("mtgeral").append(dados);
            });
        fetch('https://apigsw.herokuapp.com/data/task/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("tag").append(dados[2][1]),
                $("tfg").append(dados[1][1]);
            });
    });
});