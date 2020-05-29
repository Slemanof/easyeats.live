const logout = async () => {
  try {
    const res = await axios({
      method: 'GET',
      url: 'http://127.0.0.1:5000/logout',

    });


    if ((res.data.logout === true)) {
      window.setTimeout(() => {
        location.assign('/login');
      }, 500);

    }
  } catch (err) {
    console.log(err.response);
  }
};

document.querySelector('.btn-logout').addEventListener('click', logout);
