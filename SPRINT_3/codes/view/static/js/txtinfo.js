//ALBUQUERQUE
$(document).ready(function () {
    $(function () {
        fetch('https://apigsw.herokuapp.com/data/task/albuquerque/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("tfalb").append(dados[1][1]),
                $("taalb").append(dados[2][1]);
            });
            fetch('https://apigsw.herokuapp.com/data/horas/albuquerque/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("halb").append(dados[1]),
                $("nalb").append(dados[0]);
            });
    });
});

//BATISTA
$(document).ready(function () {
    $(function () {
        fetch('https://apigsw.herokuapp.com/data/task/batista/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("tfbat").append(dados[1][1]),
                $("tabat").append(dados[2][1]);
            });
            fetch('https://apigsw.herokuapp.com/data/horas/batista/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("hbat").append(dados[1]),
                $("nbat").append(dados[0]);
            });
    });
});

//CARVALHO
$(document).ready(function () {
    $(function () {
        fetch('https://apigsw.herokuapp.com/data/task/carvalho/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("tfcar").append(dados[1][1]),
                $("tacar").append(dados[2][1]);
            });
            fetch('https://apigsw.herokuapp.com/data/horas/carvalho/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("hcar").append(dados[1]),
                $("ncar").append(dados[0]);
            });
    });
});

//COSTACOMERCIO
$(document).ready(function () {
    $(function () {
        fetch('https://apigsw.herokuapp.com/data/task/costacomercio/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("tfcosc").append(dados[1][1]),
                $("tacosc").append(dados[2][1]);
            });
            fetch('https://apigsw.herokuapp.com/data/horas/costacomercio/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("hcosc").append(dados[1]),
                $("ncosc").append(dados[0]);
            });
    });
});

//COSTALTDA
$(document).ready(function () {
    $(function () {
        fetch('https://apigsw.herokuapp.com/data/task/costaltda/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("tfcosl").append(dados[1][1]),
                $("tacosl").append(dados[2][1]);
            });
            fetch('https://apigsw.herokuapp.com/data/horas/costaltda/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("hcosl").append(dados[1]),
                $("ncosl").append(dados[0]);
            });
    });
});

//MELO
$(document).ready(function () {
    $(function () {
        fetch('https://apigsw.herokuapp.com/data/task/melo/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("tfmel").append(dados[1][1]),
                $("tamel").append(dados[2][1]);
            });
            fetch('https://apigsw.herokuapp.com/data/horas/melo/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("hmel").append(dados[1]),
                $("nmel").append(dados[0]);
            });
    });
});

//PEREIRA
$(document).ready(function () {
    $(function () {
        fetch('https://apigsw.herokuapp.com/data/task/pereira/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("tfper").append(dados[1][1]),
                $("taper").append(dados[2][1]);
            });
            fetch('https://apigsw.herokuapp.com/data/horas/pereira/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("hper").append(dados[1]),
                $("nper").append(dados[0]);
            });
    });
});

//SANTOS
$(document).ready(function () {
    $(function () {
        fetch('https://apigsw.herokuapp.com/data/task/santos/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("tfsan").append(dados[1][1]),
                $("tasan").append(dados[2][1]);
            });
            fetch('https://apigsw.herokuapp.com/data/horas/santos/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("hsan").append(dados[1]),
                $("nsan").append(dados[0]);
            });
    });
});

//SOUZA
$(document).ready(function () {
    $(function () {
        fetch('https://apigsw.herokuapp.com/data/task/souza/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("tfsou").append(dados[1][1]),
                $("tasou").append(dados[2][1]);
            });
            fetch('https://apigsw.herokuapp.com/data/horas/souza/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("hsou").append(dados[1]),
                $("nsou").append(dados[0]);
            });
    });
});

//XAVIER
$(document).ready(function () {
    $(function () {
        fetch('https://apigsw.herokuapp.com/data/task/xavier/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("tfxav").append(dados[1][1]),
                $("taxav").append(dados[2][1]);
            });
            fetch('https://apigsw.herokuapp.com/data/horas/xavier/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("hxav").append(dados[1]),
                $("nxav").append(dados[0]);
            });
    });
});