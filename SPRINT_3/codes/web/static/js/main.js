var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'horizontalBar',
    data: {
        labels: ['DONE', 'FOR_TEST', 'IN_PROGRESS', 'RELEASE_TO_PROD', 'PROD_DELOYING', 'QA_DEPLOYING', 'QA_TESTING'],
        datasets: [{
            label: 'Quantidade por Status',
            backgroundColor: [
                'rgba(255, 99, 132)',
                'rgba(255, 159, 64)',
                'rgba(255, 205, 86)',
                'rgba(75, 192, 192)',
                'rgba(54, 162, 235)',
                'rgba(153, 102, 255)',
                'rgba(201, 203, 207)'
            ],
            borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(201, 203, 207)'
            ],
            borderWidth: 1,
            data: [171, 177, 1000, 166, 177, 135, 174],

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


var ctx2 = document.getElementById('myChart2').getContext('2d');
var chart2 = new Chart(ctx2, {
    type: 'pie',
    data: {
        labels: ['Tasks Abertas', 'Tasks fechadas'],
        datasets: [{
            label: 'Tasks Abertas e Fechadas',
            backgroundColor: [
                'rgba(0, 255, 0)',
                'rgba(255, 99, 132)',
            ],
            borderColor: [
                'rgb(0, 255, 0)',
                'rgb(255, 99, 132)'
            ],
            borderWidth: 1,
            data: [171, 177],
        }]
    },
    options: {}
});