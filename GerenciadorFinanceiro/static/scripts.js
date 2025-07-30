document.addEventListener("DOMContentLoaded", function () {
    const options = {
      chart: {
        type: 'donut',
        width: '100%',
        height: 400,
        background: '#2B2D3E',
        foreColor: '#eeeeee',
        animations: {
          enabled: true,
          easing: 'easeinout',
          speed: 800,
          animateGradually: { enabled: true, delay: 150 },
          dynamicAnimation: { enabled: true, speed: 350 }
        }
      },
      labels: labels,
      series: series,
      colors: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'],
      plotOptions: {
        pie: {
          donut: {
            size: '65%',
            background: '#121212'
          }
        }
      },
      legend: {
        position: 'bottom',
        horizontalAlign: 'center',
        labels: { colors: '#eeeeee' },
        markers: { width: 12, height: 12, radius: 12 }
      },
      dataLabels: {
        enabled: true,
        formatter(val, opts) {
          return opts.w.config.labels[opts.seriesIndex] + ': ' + val.toFixed(1) + '%';
        },
        style: { colors: ['#eeeeee'], fontSize: '14px', fontWeight: 'bold' }
      },
      tooltip: {
        enabled: true,
        y: { formatter: val => val + "% do patrimônio" }
      },
      responsive: [{
        breakpoint: 480,
        options: {
          chart: { height: 300 },
          legend: { position: 'bottom' }
        }
      }]
    };
  
    const chart = new ApexCharts(document.querySelector("#donutChart"), options);
    chart.render();
  });
  