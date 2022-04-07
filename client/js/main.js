console.log('He')

const BASE_URL = 'http://127.0.0.1:8000';

const form_name = document.getElementById("form_name")?.value;
const form_phone = document.getElementById("form_phone")?.value;
const form_email = document.getElementById("form_email")?.value;

function handleSubmit(event) {
  event.preventDefault();
  const paramsString = new URLSearchParams({
    name: form_name,
    phone: form_phone,
    email: form_email
  });
  const url = `${BASE_URL}/client_form?${paramsString}`;

  window.fetch(url).then(response.json)
  .then(function(data) {
    console.log(data);
  });

  return false;
}