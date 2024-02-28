function predict() {
    const inputX = parseFloat(document.getElementById('inputX').value);

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `input_x=${inputX}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Predicted Y: ${data.predicted_y.toFixed(2)}`;
    })
    .catch(error => console.error('Error:', error));
}
