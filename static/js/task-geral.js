var ctx1 = document.getElementById('TaskGeral').getContext('2d');

fetch('https://apigsw.herokuapp.com/data/task/')
    .then(function (response) {
        return response.json();
    })
    .then(function (dados) {
        var chart = new Chart(ctx1, {
            type: 'doughnut',
            data: {

                labels: ['Fechada', 'Aberta'],
                datasets: [{
                    label: 'Tasks',
                    backgroundColor: [
                        'rgba(231, 74, 59)',
                        'rgba(28, 200, 138)'
                    ],
                    borderColor: [
                        'rgba(231, 74, 59)',
                        'rgba(28, 200, 138)'
                    ],
                    data: [(dados[1][1]), (dados[2][1])],
                }]
            },
        });
    });
