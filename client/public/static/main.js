const form = document.querySelector('.url-form');
const result = document.querySelector('.result-section');
form.addEventListener('submit', event => {
  event.preventDefault();

  const input = document.querySelector('.original-url-input');
  fetch('https://shorty.mikemiller.tech/u/create', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      original_url: input.value,
    })
  })
    .then(response => {
      if (!response.ok) {
        throw Error(response.statusText);
      }
      //console.log(response);
      return response.json();
    })
    .then(data => {
      while (result.hasChildNodes()) {
        result.removeChild(result.lastChild);
      }

      result.insertAdjacentHTML('afterbegin', `
        <div class="result">
          <a target="_blank" class="short-url" rel="noopener" href="${data.short_url}">
            ${data.short_url}
          </a>
        </div>
      `)
    })
    .catch(console.error)
});