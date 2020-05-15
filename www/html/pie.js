var list = document.getElementById('nomProtocole');
var nb = document.getElementById('nbParProtocole');
var ctx = document.getElementById('protocole');
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {                                           
        labels: list,
        datasets: [{
            label: 'Protocole',
            data: nb,  
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 10,
	    weight: 1
        }]
    },
    options: {
        responsive: true,
	maintainAspectRatio: false,
    }
    });
