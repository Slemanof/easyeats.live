const login = async (email, password) => {

  try {
    const res = await axios({
      method: 'POST',
      url: 'http://127.0.0.1:5000/login',
      data: {
        email,
        password,
      },
    });

    if (res.data.login === true) {
      showAlert('success', 'Logged in successfully!');
      window.setTimeout(() => {
        location.assign('/home');
      }, 1500);
    }
  } catch (err) {
    showAlert('error', err.response.data.msg);
  }
};

document.querySelector('.form').addEventListener('submit', (e) => {
  e.preventDefault();
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  login(email, password);
});


const hideAlert = () => {
  const el = document.querySelector('.alert');
  if (el) el.parentElement.removeChild(el);
};

const showAlert = (type, msg) => {
  hideAlert();
  const markup = `<div class="alert alert--${type}">${msg}</div>`;
  document.querySelector('body').insertAdjacentHTML('afterbegin', markup);
  window.setTimeout(hideAlert, 3000);
};

