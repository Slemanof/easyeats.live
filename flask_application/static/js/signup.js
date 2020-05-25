const passwordFiled = document.querySelector('#password-signup');
    const tooltip = document.querySelector('.tooltip-content');

    passwordFiled.addEventListener('focusin', () => {
    tooltip.classList.remove('tooltip-toggle');
    });

    passwordFiled.addEventListener('focusout', () => {
    tooltip.classList.add('tooltip-toggle');
    });

const signup = async (name, email, password, confirm) => {
  try {
    const res = await axios({
      method: 'POST',
      url: 'http://127.0.0.1:5000/signup',
      data: {
        name,
        email,
        password,
        confirm,
      },
    });
    if (res.data.signup === true) {
      showAlert('success', 'Signed up successfully!');
      window.setTimeout(() => {
        location.assign('/login');
      }, 1500);
    }
  } catch (err) {
        showAlert('error', err.response.data.msg);
  }
};

document.querySelector('.form').addEventListener('submit', (e) => {
  e.preventDefault();
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('password-signup').value;
  const confirm = document.getElementById('password-confirm').value;
  signup(name, email, password, confirm);
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
