var cosctask = document.getElementById('cosctask').getContext('2d');

fetch('https://apigsw.herokuapp.com/data/task/costacomercio/')
    .then(function (response) {
        return response.json();
    })
    .then(function (dados) {
        console.log(dados)
        var chart = new Chart(cosctask, {
            type: 'horizontalBar',
            data: {

                labels: ['Aberta', 'Fechada'],
                datasets: [{
                    label: 'Tasks',
                    backgroundColor: [
                        'rgba(28, 200, 138)',
                        'rgba(231, 74, 59)'
                    ],
                    borderColor: [
                        'rgb(28, 200, 138)',
                        'rgb(231, 74, 59)'
                    ],
                    borderWidth: 3,
                    data: [(dados[1][1]), (dados[2][1])],
                }]
            },
            options: {
                scales: {
                    xAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    });
