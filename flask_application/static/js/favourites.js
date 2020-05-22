const addTofavourites = async (restId) => {
  try {
    const res = await axios({
      method: 'POST',
      url: 'http://127.0.0.1:5000/home',
      data: {
        restId,
      },
    });
  } catch (err) {
    showAlert('error', 'Failed to add to favourites');
  }
};
const likeSvg = document.querySelectorAll('.restaurant-view__like-svg');

for (let item of likeSvg) {
  item.addEventListener('click', () => extractId(event));
}


const extractId = (event) => {
  const svgBtn = event.target;
  const restId = svgBtn.parentElement.getAttribute('data-rest-id');
  addTofavourites(restId);
  setTimeout(() => {
        location.reload(true);
      }, 1000);
};



const hideAlert = () => {
  const el = document.querySelector('.alert');
  if (el) el.parentElement.removeChild(el);
};

const showAlert = (type, msg) => {
  hideAlert();
  const markup = `<div class="alert alert--${type}">${msg}</div>`;
  document.querySelector('body').insertAdjacentHTML('afterbegin', markup);
  window.setTimeout(hideAlert, 1000);
};
