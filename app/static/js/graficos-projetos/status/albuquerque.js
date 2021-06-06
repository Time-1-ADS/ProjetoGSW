var ctx1 = document.getElementById('Status').getContext('2d');

fetch('https://apigsw.herokuapp.com/data/status/albuquerque/')
    .then(function (response) {
        return response.json();
    })
    .then(function (dados) {
    var chart = new Chart(ctx1, {
        type: 'horizontalBar',
        data: {

            labels: [(dados[1][0]), (dados[2][0]), (dados[3][0]), (dados[4][0]), (dados[5][0]), (dados[6][0]), (dados[7][0])],
            datasets: [{
                label: 'Quantidade por Status',
                backgroundColor: [
                    'rgba(246, 194, 62)',
                    'rgba(9, 129, 239)',
                    'rgba(28, 200, 138)',
                    'rgba(234, 138, 79)',
                    'rgba(54, 185, 204)',
                    'rgba(231, 74, 59)',
                    'rgba(133, 135, 150)'
                ],
                borderColor: [
                    'rgb(246, 194, 62)',
                    'rgb(9, 129, 239)',
                    'rgb(28, 200, 138)',
                    'rgb(234, 138, 79)',
                    'rgb(54, 185, 204)',
                    'rgb(231, 74, 59)',
                    'rgb(133, 135, 150)'
                ],
                borderWidth: 1,
                data: [(dados[1][1]), (dados[2][1]), (dados[3][1]), (dados[4][1]), (dados[5][1]), (dados[6][1]), (dados[7][1])],

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