const searchButton = document.querySelector('.main__filter__body-search-btn');
const inputArr = document.querySelectorAll('.main__filter__body-input');

for (let inputItem of inputArr) {
  inputItem.addEventListener('change', () => checkboxFilter(event));
}

function checkboxFilter(event) {
  if (event.target.checked == true && searchButton.href.includes('?')) {
    searchButton.href += '&' + `${event.target.name}=${event.target.value}`;
  } else if (event.target.checked == true && !searchButton.href.includes('?')) {
    searchButton.href += '?' + `${event.target.name}=${event.target.value}`;
  } else if (event.target.checked == false) {
    if (
      searchButton.href.includes(`?${event.target.name}=${event.target.value}&`)
    ) {
      searchButton.href = searchButton.href.replace(
        `?${event.target.name}=${event.target.value}&`,
        '?'
      );
    } else if (
      searchButton.href.includes(`&${event.target.name}=${event.target.value}`)
    ) {
      searchButton.href = searchButton.href.replace(
        `&${event.target.name}=${event.target.value}`,
        ''
      );
    } else if (
      searchButton.href.includes(`?${event.target.name}=${event.target.value}`)
    ) {
      searchButton.href = searchButton.href.replace(
        `?${event.target.name}=${event.target.value}`,
        ''
      );
    }
    console.log(searchButton.href);
  }
}

searchButton.addEventListener('mouseover', goecode);

function goecode() {
  try {
    let location = '';
    if (document.querySelector('.main__address-input').value) {
      location = `${
        document.querySelector('.main__address-input').value
      }, Praha`;
    } else {
      throw new Error();
    }
    axios
      .get('https://maps.googleapis.com/maps/api/geocode/json', {
        params: {
          address: location,
          key: 'AIzaSyCmhfn0Ki3ZJxNQmIr8kMHurmcCebsZ68k',
        },
      })
      .then((res) => {
        const lat = `lat=${res.data.results[0].geometry.location.lat}`;
        const lon = `lon=${res.data.results[0].geometry.location.lng}`;
        const latlon = `${lat}&${lon}`;

        if (searchButton.href.includes('?')) {
          searchButton.href += '&' + latlon;
        } else {
          searchButton.href += '?' + latlon;
        }
        searchButton.addEventListener('mouseout', () => {
          if (searchButton.href.includes(`?${latlon}&`)) {
            searchButton.href = searchButton.href.replace(`?${latlon}&`, '?');
          } else if (searchButton.href.includes(`&${latlon}`)) {
            searchButton.href = searchButton.href.replace(`&${latlon}`, '');
          } else if (searchButton.href.includes(`?${latlon}`)) {
            searchButton.href = searchButton.href.replace(`?${latlon}`, '');
          }
        });
        console.log(searchButton.href);
      });
  } catch (err) {
    console.log('Invalid data');
  }
}
