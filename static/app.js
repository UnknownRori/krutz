/**
 * Helper function send out post request.
 * 
 * @param {string} url 
 * @param {object} body 
 * @return {response} response
 */
const post = async (url, body) => {
    const request = {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
    };

    return await fetch(url, request);
}


/**
 * Add Event Listener to form
 */
const formElement = document.getElementById('form');
const resultSection = document.getElementById('result-section');
const resultDisplay = document.getElementById('result-display');
formElement.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent form to performing full page refresh.

    // get the input element in the form.
    const inputElement = event.target.firstElementChild.firstElementChild

    // get value from input element.
    const uri = inputElement.value;

    // Post the value to api
    // post('endpoint', {uri:  uri.value}).then((res) => res.json()).then((data) => {
    // Display the result
    // resultSection.classList.remove('hidden');
    // resultDisplay.textContent = uri;
    // }).catch((err) => {
    // Catch Error
    // });
})