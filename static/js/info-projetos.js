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
        fetch('https://apigsw.herokuapp.com/data/nome/albuquerque/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("colab").append(dados[0][0]),
                    $("colab1").append(dados[1][0]);
                $("horas1").append(dados[3][0]);
                $("colab2").append(dados[0][1]),
                    $("colab3").append(dados[1][1]);
                $("horas2").append(dados[3][1]);
                $("colab4").append(dados[0][2]),
                    $("colab5").append(dados[1][2]);
                $("horas3").append(dados[3][2]);
                $("colab6").append(dados[0][3]),
                    $("colab7").append(dados[1][3]);
                $("horas4").append(dados[3][3]);
                $("colab8").append(dados[0][4]),
                    $("colab9").append(dados[1][4]);
                $("horas5").append(dados[3][4]);
                $("colab10").append(dados[0][5]),
                    $("colab11").append(dados[1][5]);
                $("horas6").append(dados[3][5]);
                $("colab12").append(dados[0][6]),
                    $("colab13").append(dados[1][6]);
                $("horas7").append(dados[3][6]);
                $("colab14").append(dados[0][7]),
                    $("colab15").append(dados[1][7]);
                $("horas8").append(dados[3][7]);
                $("colab16").append(dados[0][8]),
                    $("colab17").append(dados[1][8]);
                $("horas9").append(dados[3][8]);
                $("colab18").append(dados[0][9]),
                    $("colab19").append(dados[1][9]);
                $("horas10").append(dados[3][9]);
                $("colab20").append(dados[0][10]),
                    $("colab21").append(dados[1][10]);
                $("horas11").append(dados[3][10]);
                $("colab22").append(dados[0][11]),
                    $("colab23").append(dados[1][11]);
                $("horas12").append(dados[3][11]);
                $("colab24").append(dados[0][12]),
                    $("colab25").append(dados[1][12]);
                $("horas13").append(dados[3][12]);
                $("colab26").append(dados[0][13]),
                    $("colab27").append(dados[1][13]);
                $("horas14").append(dados[3][13]);
                $("colab28").append(dados[0][14]),
                    $("colab29").append(dados[1][14]);
                $("horas15").append(dados[3][14]);
                $("colab30").append(dados[0][15]),
                    $("colab31").append(dados[1][15]);
                $("horas16").append(dados[3][15]);
                $("colab32").append(dados[0][16]),
                    $("colab33").append(dados[1][16]);
                $("horas17").append(dados[3][16]);
                $("colab34").append(dados[0][17]),
                    $("colab35").append(dados[1][17]);
                $("horas18").append(dados[3][17]);
                $("colab36").append(dados[0][18]),
                    $("colab37").append(dados[1][18]);
                $("horas19").append(dados[3][18]);
            });
        fetch('https://apigsw.herokuapp.com/data/mediahoras/albuquerque/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("mtalb").append(dados[1]);
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
        fetch('https://apigsw.herokuapp.com/data/nome/batista/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("colab38").append(dados[0][0]),
                    $("colab39").append(dados[1][0]);
                $("horas20").append(dados[3][0]);
                $("colab40").append(dados[0][1]),
                    $("colab41").append(dados[1][1]);
                $("horas21").append(dados[3][1]);
                $("colab42").append(dados[0][2]),
                    $("colab43").append(dados[1][2]);
                $("horas22").append(dados[3][2]);
                $("colab44").append(dados[0][3]),
                    $("colab45").append(dados[1][3]);
                $("horas23").append(dados[3][3]);
                $("colab46").append(dados[0][4]),
                    $("colab47").append(dados[1][4]);
                $("horas24").append(dados[3][4]);
                $("colab48").append(dados[0][5]),
                    $("colab49").append(dados[1][5]);
                $("horas25").append(dados[3][5]);
                $("colab50").append(dados[0][6]),
                    $("colab51").append(dados[1][6]);
                $("horas26").append(dados[3][6]);
                $("colab52").append(dados[0][7]),
                    $("colab53").append(dados[1][7]);
                $("horas27").append(dados[3][7]);
                $("colab54").append(dados[0][8]),
                    $("colab55").append(dados[1][8]);
                $("horas28").append(dados[3][8]);
                $("colab56").append(dados[0][9]),
                    $("colab57").append(dados[1][9]);
                $("horas29").append(dados[3][9]);
                $("colab58").append(dados[0][10]),
                    $("colab59").append(dados[1][10]);
                $("horas30").append(dados[3][10]);
                $("colab60").append(dados[0][11]),
                    $("colab61").append(dados[1][11]);
                $("horas31").append(dados[3][11]);
                $("colab62").append(dados[0][12]),
                    $("colab63").append(dados[1][12]);
                $("horas32").append(dados[3][12]);
                $("colab64").append(dados[0][13]),
                    $("colab65").append(dados[1][13]);
                $("horas33").append(dados[3][13]);
                $("colab66").append(dados[0][14]),
                    $("colab67").append(dados[1][14]);
                $("horas34").append(dados[3][14]);
                $("colab68").append(dados[0][15]),
                    $("colab69").append(dados[1][15]);
                $("horas35").append(dados[3][15]);
                $("colab70").append(dados[0][16]),
                    $("colab71").append(dados[1][16]);
                $("horas36").append(dados[3][16]);
                $("colab72").append(dados[0][17]),
                    $("colab73").append(dados[1][17]);
                $("horas37").append(dados[3][17]);
                $("colab74").append(dados[0][18]),
                    $("colab75").append(dados[1][18]);
                $("horas38").append(dados[3][18]);
            });
            fetch('https://apigsw.herokuapp.com/data/mediahoras/batista/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("mtbat").append(dados[1]);
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
        fetch('https://apigsw.herokuapp.com/data/nome/carvalho/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("colab76").append(dados[0][0]),
                    $("colab77").append(dados[1][0]);
                $("horas39").append(dados[3][0]);
                $("colab78").append(dados[0][1]),
                    $("colab79").append(dados[1][1]);
                $("horas40").append(dados[3][1]);
                $("colab80").append(dados[0][2]),
                    $("colab81").append(dados[1][2]);
                $("horas41").append(dados[3][2]);
                $("colab82").append(dados[0][3]),
                    $("colab83").append(dados[1][3]);
                $("horas42").append(dados[3][3]);
                $("colab84").append(dados[0][4]),
                    $("colab85").append(dados[1][4]);
                $("horas43").append(dados[3][4]);
                $("colab86").append(dados[0][5]),
                    $("colab87").append(dados[1][5]);
                $("horas44").append(dados[3][5]);
                $("colab88").append(dados[0][6]),
                    $("colab89").append(dados[1][6]);
                $("horas45").append(dados[3][6]);
                $("colab90").append(dados[0][7]),
                    $("colab91").append(dados[1][7]);
                $("horas46").append(dados[3][7]);
                $("colab92").append(dados[0][8]),
                    $("colab93").append(dados[1][8]);
                $("horas47").append(dados[3][8]);
                $("colab94").append(dados[0][9]),
                    $("colab95").append(dados[1][9]);
                $("horas48").append(dados[3][9]);
                $("colab96").append(dados[0][10]),
                    $("colab97").append(dados[1][10]);
                $("horas49").append(dados[3][10]);
                $("colab98").append(dados[0][11]),
                    $("colab99").append(dados[1][11]);
                $("horas50").append(dados[3][11]);
                $("colab100").append(dados[0][12]),
                    $("colab101").append(dados[1][12]);
                $("horas51").append(dados[3][12]);
                $("colab102").append(dados[0][13]),
                    $("colab103").append(dados[1][13]);
                $("horas52").append(dados[3][13]);
                $("colab104").append(dados[0][14]),
                    $("colab105").append(dados[1][14]);
                $("horas53").append(dados[3][14]);
                $("colab106").append(dados[0][15]),
                    $("colab107").append(dados[1][15]);
                $("horas54").append(dados[3][15]);
                $("colab108").append(dados[0][16]),
                    $("colab109").append(dados[1][16]);
                $("horas55").append(dados[3][16]);
                $("colab110").append(dados[0][17]),
                    $("colab111").append(dados[1][17]);
                $("horas56").append(dados[3][17]);
                $("colab112").append(dados[0][18]),
                    $("colab113").append(dados[1][18]);
                $("horas57").append(dados[3][18]);
            });
            fetch('https://apigsw.herokuapp.com/data/mediahoras/carvalho/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("mtcar").append(dados[1]);
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
        fetch('https://apigsw.herokuapp.com/data/nome/costacomercio/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("colab114").append(dados[0][0]),
                    $("colab115").append(dados[1][0]);
                $("horas58").append(dados[3][0]);
                $("colab116").append(dados[0][1]),
                    $("colab117").append(dados[1][1]);
                $("horas59").append(dados[3][1]);
                $("colab118").append(dados[0][2]),
                    $("colab119").append(dados[1][2]);
                $("horas60").append(dados[3][2]);
                $("colab120").append(dados[0][3]),
                    $("colab121").append(dados[1][3]);
                $("horas61").append(dados[3][3]);
                $("colab122").append(dados[0][4]),
                    $("colab123").append(dados[1][4]);
                $("horas62").append(dados[3][4]);
                $("colab124").append(dados[0][5]),
                    $("colab125").append(dados[1][5]);
                $("horas63").append(dados[3][5]);
                $("colab126").append(dados[0][6]),
                    $("colab127").append(dados[1][6]);
                $("horas64").append(dados[3][6]);
                $("colab128").append(dados[0][7]),
                    $("colab129").append(dados[1][7]);
                $("horas65").append(dados[3][7]);
                $("colab130").append(dados[0][8]),
                    $("colab131").append(dados[1][8]);
                $("horas66").append(dados[3][8]);
                $("colab132").append(dados[0][9]),
                    $("colab133").append(dados[1][9]);
                $("horas67").append(dados[3][9]);
                $("colab134").append(dados[0][10]),
                    $("colab135").append(dados[1][10]);
                $("horas68").append(dados[3][10]);
                $("colab136").append(dados[0][11]),
                    $("colab137").append(dados[1][11]);
                $("horas69").append(dados[3][11]);
                $("colab138").append(dados[0][12]),
                    $("colab139").append(dados[1][12]);
                $("horas70").append(dados[3][12]);
                $("colab140").append(dados[0][13]),
                    $("colab141").append(dados[1][13]);
                $("horas71").append(dados[3][13]);
                $("colab142").append(dados[0][14]),
                    $("colab143").append(dados[1][14]);
                $("horas72").append(dados[3][14]);
                $("colab144").append(dados[0][15]),
                    $("colab145").append(dados[1][15]);
                $("horas73").append(dados[3][15]);
                $("colab146").append(dados[0][16]),
                    $("colab147").append(dados[1][16]);
                $("horas74").append(dados[3][16]);
                $("colab148").append(dados[0][17]),
                    $("colab149").append(dados[1][17]);
                $("horas75").append(dados[3][17]);
                $("colab150").append(dados[0][18]),
                    $("colab151").append(dados[1][18]);
                $("horas76").append(dados[3][18]);
            });
            fetch('https://apigsw.herokuapp.com/data/mediahoras/costacomercio/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("mtcosc").append(dados[1]);
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
        fetch('https://apigsw.herokuapp.com/data/nome/costaltda/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("colab152").append(dados[0][0]),
                    $("colab153").append(dados[1][0]);
                $("horas77").append(dados[3][0]);
                $("colab154").append(dados[0][1]),
                    $("colab155").append(dados[1][1]);
                $("horas78").append(dados[3][1]);
                $("colab156").append(dados[0][2]),
                    $("colab157").append(dados[1][2]);
                $("horas79").append(dados[3][2]);
                $("colab158").append(dados[0][3]),
                    $("colab159").append(dados[1][3]);
                $("horas80").append(dados[3][3]);
                $("colab160").append(dados[0][4]),
                    $("colab161").append(dados[1][4]);
                $("horas81").append(dados[3][4]);
                $("colab162").append(dados[0][5]),
                    $("colab163").append(dados[1][5]);
                $("horas82").append(dados[3][5]);
                $("colab164").append(dados[0][6]),
                    $("colab165").append(dados[1][6]);
                $("horas83").append(dados[3][6]);
                $("colab166").append(dados[0][7]),
                    $("colab167").append(dados[1][7]);
                $("horas84").append(dados[3][7]);
                $("colab168").append(dados[0][8]),
                    $("colab169").append(dados[1][8]);
                $("horas85").append(dados[3][8]);
                $("colab170").append(dados[0][9]),
                    $("colab171").append(dados[1][9]);
                $("horas86").append(dados[3][9]);
                $("colab172").append(dados[0][10]),
                    $("colab173").append(dados[1][10]);
                $("horas87").append(dados[3][10]);
                $("colab174").append(dados[0][11]),
                    $("colab175").append(dados[1][11]);
                $("horas88").append(dados[3][11]);
                $("colab176").append(dados[0][12]),
                    $("colab177").append(dados[1][12]);
                $("horas89").append(dados[3][12]);
                $("colab178").append(dados[0][13]),
                    $("colab179").append(dados[1][13]);
                $("horas90").append(dados[3][13]);
                $("colab180").append(dados[0][14]),
                    $("colab181").append(dados[1][14]);
                $("horas91").append(dados[3][14]);
                $("colab182").append(dados[0][15]),
                    $("colab183").append(dados[1][15]);
                $("horas92").append(dados[3][15]);
                $("colab184").append(dados[0][16]),
                    $("colab185").append(dados[1][16]);
                $("horas93").append(dados[3][16]);
                $("colab186").append(dados[0][17]),
                    $("colab187").append(dados[1][17]);
                $("horas94").append(dados[3][17]);
                $("colab188").append(dados[0][18]),
                    $("colab189").append(dados[1][18]);
                $("horas95").append(dados[3][18]);
            });
            fetch('https://apigsw.herokuapp.com/data/mediahoras/costaltda/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("mtcosl").append(dados[1]);
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
        fetch('https://apigsw.herokuapp.com/data/nome/melo/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("colab190").append(dados[0][0]),
                    $("colab191").append(dados[1][0]);
                $("horas96").append(dados[3][0]);
                $("colab192").append(dados[0][1]),
                    $("colab193").append(dados[1][1]);
                $("horas97").append(dados[3][1]);
                $("colab194").append(dados[0][2]),
                    $("colab195").append(dados[1][2]);
                $("horas98").append(dados[3][2]);
                $("colab196").append(dados[0][3]),
                    $("colab197").append(dados[1][3]);
                $("horas99").append(dados[3][3]);
                $("colab198").append(dados[0][4]),
                    $("colab199").append(dados[1][4]);
                $("horas100").append(dados[3][4]);
                $("colab200").append(dados[0][5]),
                    $("colab201").append(dados[1][5]);
                $("horas101").append(dados[3][5]);
                $("colab202").append(dados[0][6]),
                    $("colab203").append(dados[1][6]);
                $("horas102").append(dados[3][6]);
                $("colab204").append(dados[0][7]),
                    $("colab205").append(dados[1][7]);
                $("horas103").append(dados[3][7]);
                $("colab206").append(dados[0][8]),
                    $("colab207").append(dados[1][8]);
                $("horas104").append(dados[3][8]);
                $("colab208").append(dados[0][9]),
                    $("colab209").append(dados[1][9]);
                $("horas105").append(dados[3][9]);
                $("colab210").append(dados[0][10]),
                    $("colab211").append(dados[1][10]);
                $("horas106").append(dados[3][10]);
                $("colab212").append(dados[0][11]),
                    $("colab213").append(dados[1][11]);
                $("horas107").append(dados[3][11]);
                $("colab214").append(dados[0][12]),
                    $("colab215").append(dados[1][12]);
                $("horas108").append(dados[3][12]);
                $("colab216").append(dados[0][13]),
                    $("colab217").append(dados[1][13]);
                $("horas109").append(dados[3][13]);
                $("colab218").append(dados[0][14]),
                    $("colab219").append(dados[1][14]);
                $("horas110").append(dados[3][14]);
                $("colab220").append(dados[0][15]),
                    $("colab221").append(dados[1][15]);
                $("horas111").append(dados[3][15]);
                $("colab222").append(dados[0][16]),
                    $("colab223").append(dados[1][16]);
                $("horas112").append(dados[3][16]);
                $("colab224").append(dados[0][17]),
                    $("colab225").append(dados[1][17]);
                $("horas113").append(dados[3][17]);
                $("colab226").append(dados[0][18]),
                    $("colab227").append(dados[1][18]);
                $("horas114").append(dados[3][18]);
            });
            fetch('https://apigsw.herokuapp.com/data/mediahoras/melo/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("mtmel").append(dados[2]);
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
        fetch('https://apigsw.herokuapp.com/data/nome/pereira/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("colab228").append(dados[0][0]),
                    $("colab229").append(dados[1][0]);
                $("horas115").append(dados[3][0]);
                $("colab230").append(dados[0][1]),
                    $("colab231").append(dados[1][1]);
                $("horas116").append(dados[3][1]);
                $("colab232").append(dados[0][2]),
                    $("colab233").append(dados[1][2]);
                $("horas117").append(dados[3][2]);
                $("colab234").append(dados[0][3]),
                    $("colab235").append(dados[1][3]);
                $("horas118").append(dados[3][3]);
                $("colab236").append(dados[0][4]),
                    $("colab237").append(dados[1][4]);
                $("horas119").append(dados[3][4]);
                $("colab238").append(dados[0][5]),
                    $("colab239").append(dados[1][5]);
                $("horas120").append(dados[3][5]);
                $("colab240").append(dados[0][6]),
                    $("colab241").append(dados[1][6]);
                $("horas121").append(dados[3][6]);
                $("colab242").append(dados[0][7]),
                    $("colab243").append(dados[1][7]);
                $("horas122").append(dados[3][7]);
                $("colab244").append(dados[0][8]),
                    $("colab245").append(dados[1][8]);
                $("horas123").append(dados[3][8]);
                $("colab246").append(dados[0][9]),
                    $("colab247").append(dados[1][9]);
                $("horas124").append(dados[3][9]);
                $("colab248").append(dados[0][10]),
                    $("colab249").append(dados[1][10]);
                $("horas125").append(dados[3][10]);
                $("colab250").append(dados[0][11]),
                    $("colab251").append(dados[1][11]);
                $("horas126").append(dados[3][11]);
                $("colab252").append(dados[0][12]),
                    $("colab253").append(dados[1][12]);
                $("horas127").append(dados[3][12]);
                $("colab254").append(dados[0][13]),
                    $("colab255").append(dados[1][13]);
                $("horas128").append(dados[3][13]);
                $("colab256").append(dados[0][14]),
                    $("colab257").append(dados[1][14]);
                $("horas129").append(dados[3][14]);
                $("colab258").append(dados[0][15]),
                    $("colab259").append(dados[1][15]);
                $("horas130").append(dados[3][15]);
                $("colab260").append(dados[0][16]),
                    $("colab261").append(dados[1][16]);
                $("horas131").append(dados[3][16]);
                $("colab262").append(dados[0][17]),
                    $("colab263").append(dados[1][17]);
                $("horas132").append(dados[3][17]);
                $("colab264").append(dados[0][18]),
                    $("colab265").append(dados[1][18]);
                $("horas133").append(dados[3][18]);
            });
            fetch('https://apigsw.herokuapp.com/data/mediahoras/pereira/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("mtper").append(dados[1]);
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
        fetch('https://apigsw.herokuapp.com/data/nome/santos/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("colab266").append(dados[0][0]),
                    $("colab267").append(dados[1][0]);
                $("horas134").append(dados[3][0]);
                $("colab268").append(dados[0][1]),
                    $("colab269").append(dados[1][1]);
                $("horas135").append(dados[3][1]);
                $("colab270").append(dados[0][2]),
                    $("colab271").append(dados[1][2]);
                $("horas136").append(dados[3][2]);
                $("colab272").append(dados[0][3]),
                    $("colab273").append(dados[1][3]);
                $("horas137").append(dados[3][3]);
                $("colab274").append(dados[0][4]),
                    $("colab275").append(dados[1][4]);
                $("horas138").append(dados[3][4]);
                $("colab276").append(dados[0][5]),
                    $("colab277").append(dados[1][5]);
                $("horas139").append(dados[3][5]);
                $("colab278").append(dados[0][6]),
                    $("colab279").append(dados[1][6]);
                $("horas140").append(dados[3][6]);
                $("colab280").append(dados[0][7]),
                    $("colab281").append(dados[1][7]);
                $("horas141").append(dados[3][7]);
                $("colab282").append(dados[0][8]),
                    $("colab283").append(dados[1][8]);
                $("horas142").append(dados[3][8]);
                $("colab284").append(dados[0][9]),
                    $("colab285").append(dados[1][9]);
                $("horas143").append(dados[3][9]);
                $("colab286").append(dados[0][10]),
                    $("colab287").append(dados[1][10]);
                $("horas144").append(dados[3][10]);
                $("colab288").append(dados[0][11]),
                    $("colab289").append(dados[1][11]);
                $("horas145").append(dados[3][11]);
                $("colab290").append(dados[0][12]),
                    $("colab291").append(dados[1][12]);
                $("horas146").append(dados[3][12]);
                $("colab292").append(dados[0][13]),
                    $("colab293").append(dados[1][13]);
                $("horas147").append(dados[3][13]);
                $("colab294").append(dados[0][14]),
                    $("colab295").append(dados[1][14]);
                $("horas148").append(dados[3][14]);
                $("colab296").append(dados[0][15]),
                    $("colab297").append(dados[1][15]);
                $("horas149").append(dados[3][15]);
                $("colab298").append(dados[0][16]),
                    $("colab299").append(dados[1][16]);
                $("horas150").append(dados[3][16]);
                $("colab300").append(dados[0][17]),
                    $("colab301").append(dados[1][17]);
                $("horas151").append(dados[3][17]);
                $("colab302").append(dados[0][18]),
                    $("colab303").append(dados[1][18]);
                $("horas152").append(dados[3][18]);
            });
            fetch('https://apigsw.herokuapp.com/data/mediahoras/santos/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("mtsan").append(dados[1]);
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
        fetch('https://apigsw.herokuapp.com/data/nome/souza/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("colab304").append(dados[0][0]),
                    $("colab305").append(dados[1][0]);
                $("horas153").append(dados[3][0]);
                $("colab306").append(dados[0][1]),
                    $("colab307").append(dados[1][1]);
                $("horas154").append(dados[3][1]);
                $("colab308").append(dados[0][2]),
                    $("colab309").append(dados[1][2]);
                $("horas155").append(dados[3][2]);
                $("colab310").append(dados[0][3]),
                    $("colab311").append(dados[1][3]);
                $("horas156").append(dados[3][3]);
                $("colab312").append(dados[0][4]),
                    $("colab313").append(dados[1][4]);
                $("horas157").append(dados[3][4]);
                $("colab314").append(dados[0][5]),
                    $("colab315").append(dados[1][5]);
                $("horas158").append(dados[3][5]);
                $("colab316").append(dados[0][6]),
                    $("colab317").append(dados[1][6]);
                $("horas159").append(dados[3][6]);
                $("colab318").append(dados[0][7]),
                    $("colab319").append(dados[1][7]);
                $("horas160").append(dados[3][7]);
                $("colab320").append(dados[0][8]),
                    $("colab321").append(dados[1][8]);
                $("horas161").append(dados[3][8]);
                $("colab322").append(dados[0][9]),
                    $("colab323").append(dados[1][9]);
                $("horas162").append(dados[3][9]);
                $("colab324").append(dados[0][10]),
                    $("colab325").append(dados[1][10]);
                $("horas163").append(dados[3][10]);
                $("colab326").append(dados[0][11]),
                    $("colab327").append(dados[1][11]);
                $("horas164").append(dados[3][11]);
                $("colab328").append(dados[0][12]),
                    $("colab329").append(dados[1][12]);
                $("horas165").append(dados[3][12]);
                $("colab330").append(dados[0][13]),
                    $("colab331").append(dados[1][13]);
                $("horas166").append(dados[3][13]);
                $("colab332").append(dados[0][14]),
                    $("colab333").append(dados[1][14]);
                $("horas167").append(dados[3][14]);
                $("colab334").append(dados[0][15]),
                    $("colab335").append(dados[1][15]);
                $("horas168").append(dados[3][15]);
                $("colab336").append(dados[0][16]),
                    $("colab337").append(dados[1][16]);
                $("horas169").append(dados[3][16]);
                $("colab338").append(dados[0][17]),
                    $("colab339").append(dados[1][17]);
                $("horas170").append(dados[3][17]);
                $("colab340").append(dados[0][18]),
                    $("colab341").append(dados[1][18]);
                $("horas171").append(dados[3][18]);
            });
            fetch('https://apigsw.herokuapp.com/data/mediahoras/souza/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("mtsou").append(dados[1]);
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
        fetch('https://apigsw.herokuapp.com/data/nome/xavier/')
            .then(function (hora) {
                return hora.json();
            })
            .then(function (dados) {
                $("colab342").append(dados[0][0]),
                    $("colab343").append(dados[1][0]);
                $("horas172").append(dados[3][0]);
                $("colab344").append(dados[0][1]),
                    $("colab345").append(dados[1][1]);
                $("horas173").append(dados[3][1]);
                $("colab346").append(dados[0][2]),
                    $("colab347").append(dados[1][2]);
                $("horas174").append(dados[3][2]);
                $("colab348").append(dados[0][3]),
                    $("colab349").append(dados[1][3]);
                $("horas175").append(dados[3][3]);
                $("colab350").append(dados[0][4]),
                    $("colab351").append(dados[1][4]);
                $("horas176").append(dados[3][4]);
                $("colab352").append(dados[0][5]),
                    $("colab353").append(dados[1][5]);
                $("horas177").append(dados[3][5]);
                $("colab354").append(dados[0][6]),
                    $("colab355").append(dados[1][6]);
                $("horas178").append(dados[3][6]);
                $("colab356").append(dados[0][7]),
                    $("colab357").append(dados[1][7]);
                $("horas179").append(dados[3][7]);
                $("colab358").append(dados[0][8]),
                    $("colab359").append(dados[1][8]);
                $("horas180").append(dados[3][8]);
                $("colab360").append(dados[0][9]),
                    $("colab361").append(dados[1][9]);
                $("horas181").append(dados[3][9]);
                $("colab362").append(dados[0][10]),
                    $("colab363").append(dados[1][10]);
                $("horas182").append(dados[3][10]);
                $("colab364").append(dados[0][11]),
                    $("colab365").append(dados[1][11]);
                $("horas183").append(dados[3][11]);
                $("colab366").append(dados[0][12]),
                    $("colab367").append(dados[1][12]);
                $("horas184").append(dados[3][12]);
                $("colab368").append(dados[0][13]),
                    $("colab369").append(dados[1][13]);
                $("horas185").append(dados[3][13]);
                $("colab370").append(dados[0][14]),
                    $("colab371").append(dados[1][14]);
                $("horas186").append(dados[3][14]);
                $("colab372").append(dados[0][15]),
                    $("colab373").append(dados[1][15]);
                $("horas187").append(dados[3][15]);
                $("colab374").append(dados[0][16]),
                    $("colab375").append(dados[1][16]);
                $("horas188").append(dados[3][16]);
                $("colab376").append(dados[0][17]),
                    $("colab377").append(dados[1][17]);
                $("horas189").append(dados[3][17]);
                $("colab378").append(dados[0][18]),
                    $("colab379").append(dados[1][18]);
                $("horas190").append(dados[3][18]);
            });
            fetch('https://apigsw.herokuapp.com/data/mediahoras/xavier/')
            .then(function (task) {
                return task.json();
            })
            .then(function (dados) {
                $("mtxav").append(dados[1]);
            });
    });
});