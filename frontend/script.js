document.getElementById('fetch-button').addEventListener('click', fetchOpportunities);

async function fetchOpportunities() {
    try {
        const response = await fetch('http://localhost:5000/opportunities'); // Adjust the URL based on your backend
        const data = await response.json();
        populateTable(data);
    } catch (error) {
        console.error('Error fetching opportunities:', error);
    }
}

function populateTable(opportunities) {
    const tableBody = document.getElementById('opportunities-body');
    tableBody.innerHTML = ''; // Clear existing rows

    opportunities.forEach(opportunity => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${opportunity.token_pair}</td>
            <td>${opportunity.binance_price.toFixed(4)}</td>
            <td>${opportunity.solana_price.toFixed(4)}</td>
            <td>${opportunity.profit.toFixed(4)}</td>
        `;
        tableBody.appendChild(row);
    });
}