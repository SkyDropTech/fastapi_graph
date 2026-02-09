document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/revenue")
        .then(res => res.json())
        .then(data => {
            const ctx = document.getElementById("revenueChart");

            new Chart(ctx, {
                type: "line",
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: "Revenue",
                        data: data.values,
                        borderWidth: 3,
                        tension: 0.4,
                        fill: true,
                        borderColor: "#4f46e5",
                        backgroundColor: "rgba(79,70,229,0.15)"
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { display: false }
                    },
                    scales: {
                        y: { beginAtZero: true }
                    }
                }
            });
        });
});
