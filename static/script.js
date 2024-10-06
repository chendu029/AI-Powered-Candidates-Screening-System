document.getElementById('candidateForm').addEventListener('submit', async function (event) {
    event.preventDefault();  // Prevent default form submission behavior

    const formData = new FormData(this);

    // Fetch the results from the server after form submission
    const response = await fetch('/submit', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    const resultDiv = document.getElementById('result');
    resultDiv.innerText = 'Total Score: ' + result.total_score + ', Role: ' + result.role;
    resultDiv.style.display = 'block'; // Show the result section
});
