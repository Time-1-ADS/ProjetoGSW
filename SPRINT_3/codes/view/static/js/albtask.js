var albtask = document.getElementById('albtask').getContext('2d');

fetch('https://apigsw.herokuapp.com/data/task/albuquerque/')
    .then(function (response) {
        return response.json();
    })
    .then(function (dados) {
        var chart = new Chart(albtask, {
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