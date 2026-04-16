let chart;

function carregarDados() {
    fetch('/api/dashboard/')
        .then(res => res.json())
        .then(data => {

         
            document.getElementById('total').innerText =
                data.total_vendas;

            document.getElementById('faturamento').innerText =
                "R$ " + data.faturamento_total;

            const listaVendedores = document.getElementById('lista_vendedores');
            listaVendedores.innerHTML = '';

            data.top_vendedores.forEach((v, index) => {
                listaVendedores.innerHTML +=
                    `<li> ${index + 1} - ${v.vendedor__nome} (${v.total} vendas)</li>`;
            });

            const listaProdutos = document.getElementById('lista_produtos');
            listaProdutos.innerHTML = '';

            data.top_produtos.forEach((p, index) => {
                listaProdutos.innerHTML +=
                    `<li> ${index + 1} - ${p.produto__nome} (${p.total} vendidos)</li>`;
            });

            const labels = data.vendas_por_produto.map(d => d.produto__nome);
            const valores = data.vendas_por_produto.map(d => d.total);

            if (chart) {
                chart.data.labels = labels;
                chart.data.datasets[0].data = valores;
                chart.update();
            } else {
                chart = new Chart(document.getElementById('grafico'), {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Vendas por Produto',
                            data: valores,
                            maxBarThickness: 50,
                            backgroundColor: '#4C9170',
                            borderColor: '#1E5E3F',
                        }]
                    },
                    options: {
                       

                        responsive: true,
                        maintainAspectRatio: false,

                        plugins: {
                            legend: {
                                display: false
                            }
                        },

                        scales: {
                            x: {
                                beginAtZero: true
                            },
                            y: {
                                ticks: {
                                    autoSkip: false 
                                }
                            }
                        }
                    }
                });
            }
        });
}

setInterval(carregarDados, 3000);
carregarDados();