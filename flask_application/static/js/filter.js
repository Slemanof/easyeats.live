const searchButton = document.querySelector('.main__filter__body-search-btn');
const inputArr = document.querySelectorAll('.main__filter__body-input');
const viewElement = document.querySelector('.main__header');
const searchAddress = document.querySelector('#searchAddress');
const searchRadius = document.querySelector('#searchRadius');
let coordinates;
let queryStr = '';

for (let inputItem of inputArr) {
  inputItem.addEventListener('change', () => checkboxFilter(event));
}

function checkboxFilter(event) {
  if (event.target.checked == true) {
    localStorage.setItem(event.target.id, JSON.stringify(event.target.checked));
  } else if (event.target.checked == false) {
    localStorage.removeItem(event.target.id);
  }
}

searchAddress.addEventListener('input', () => {
  if (searchAddress.value) {
    localStorage.setItem(searchAddress.id, JSON.stringify(searchAddress.value));
  } else if (!searchAddress.value) {
    localStorage.removeItem(searchAddress.id);
  }
});

async function geocode() {
  try {
    let location = '';
    const address = JSON.parse(localStorage.getItem(searchAddress.id));

    location = `${address}, Prague`;
    const res = await axios.get(
      'https://maps.googleapis.com/maps/api/geocode/json',
      {
        params: {
          address: location,
          key: 'AIzaSyCmhfn0Ki3ZJxNQmIr8kMHurmcCebsZ68k',
        },
      }
    );
    coordinates = `lat=${res.data.results[0].geometry.location.lat}&lon=${res.data.results[0].geometry.location.lng}`;
  } catch (err) {
    console.log('Invalid data');
  }
}

for (let key of Object.keys(localStorage)) {
  if (key == searchAddress.id) {
    document.getElementById(key).value = JSON.parse(localStorage.getItem(key));
  }

  document.getElementById(key).checked = JSON.parse(localStorage.getItem(key));
}


for (let item of inputArr) {
  if (
    !window.location.href.includes(item.name) ||
    !window.location.href.includes(item.value)
  ) {
    localStorage.removeItem(item.id);
    item.checked = false;
  } else if (window.location.href.includes(item.value)) {
    item.checked = true;
    localStorage.setItem(item.id, JSON.stringify(item.checked));
  }
}

if (!window.location.href.includes(searchAddress.name)) {
  localStorage.removeItem(searchAddress.id);
  searchAddress.value = '';
}

//document.querySelector('.btn-logout').addEventListener('click', () => {
//  localStorage.clear();
//});


document
  .querySelector('.main__filter__body-refresh-btn')
  .addEventListener('click', () => {
    localStorage.clear();
    history.pushState(null, null, '/home');
    viewElement.scrollIntoView({
      behavior: 'smooth',
      block: 'start',
    });
    setTimeout(() => {
      location.reload(true);
    }, 1000);
  });


const formQuery = () => {
  queryStr = '?';
  let values = [];
  let nameSet = new Set();

  for (let key of Object.keys(localStorage)) {
    nameSet.add(document.getElementById(key).name);
    console.log(nameSet);
    values.push(document.getElementById(key));
    console.log(values);
  }
  for (let name of nameSet) {
    queryStr += `${name}=`;
    for (let value of values) {
      if (value.name == name) {
        if (value.name === 'address') {
          queryStr = queryStr.replace(value.name, coordinates);
        } else {
          queryStr += `${value.value}/`;
        }
      }
    }
    queryStr = queryStr.substring(0, queryStr.length - 1) + '&';
  }
  queryStr = queryStr.substring(0, queryStr.length - 1) + '';
};


searchButton.addEventListener('click', async () => {
  await geocode();
  formQuery();

  if (localStorage.length == 0) {
    queryStr = '/home';
  }

  history.pushState(null, null, queryStr);

  viewElement.scrollIntoView({
    behavior: 'smooth',
    block: 'start',
  });

  setTimeout(() => {
    location.reload(true);
  }, 1000);
});
