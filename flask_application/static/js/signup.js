const signup = async (name, email, password, confirm) => {
  try {
    const pass = document.querySelector('#password-signup').value;
    console.log(pass)
    if (pass.length < 8) {
      showAlert('error', 'Password length must be not less than 8 symbols');
      return 'short_pass';
    } else if (pass.search(/[a-z]/) == -1) {
      showAlert(
        'error',
        'You need to have at least one small letter in password'
      );
      return 'no_small_letter';
    } else if (pass.search(/[A-Z]/) == -1) {
      showAlert(
        'error',
        'You need to have at least one capital letter in password'
      );
      return 'no_capital_letter';
    } else if (pass.search(/[0-9]/) == -1) {
      showAlert('error', 'You need to have at least one digit in password');
      return 'no_digit';
    } else if (pass.search(/[!\@\#\$\%\^\&\_\+\.\,\;\:]/) == -1) {
      showAlert(
        'error',
        'You need to have at least one special character in password: !@#$%^&_+.,;:'
      );
      return 'no_special_charachter';
    }
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
