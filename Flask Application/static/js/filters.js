function checkboxFilter() {
  let str = '?';
  const inputArr = document.querySelectorAll('.main__filter__body-elem');
  let searchButton = document.querySelector('.main__filter__body-search-btn');

  for (let inputItem of inputArr) {
    inputItem.addEventListener('change', () => {
      if (inputItem.firstElementChild.checked == true) {
        str += `${inputItem.firstElementChild.name}=${inputItem.firstElementChild.value}`;
        searchButton.href += str;
        str = '&';
      } else if (inputItem.firstElementChild.checked == false) {
        if (
          searchButton.href.includes(
            `?${inputItem.firstElementChild.name}=${inputItem.firstElementChild.value}&`
          )
        ) {
          searchButton.href = searchButton.href.replace(
            `?${inputItem.firstElementChild.name}=${inputItem.firstElementChild.value}&`,
            '?'
          );
        } else if (
          searchButton.href.includes(
            `&${inputItem.firstElementChild.name}=${inputItem.firstElementChild.value}`
          )
        ) {
          searchButton.href = searchButton.href.replace(
            `&${inputItem.firstElementChild.name}=${inputItem.firstElementChild.value}`,
            ''
          );
        } else if (
          searchButton.href.includes(
            `?${inputItem.firstElementChild.name}=${inputItem.firstElementChild.value}`
          )
        ) {
          searchButton.href = searchButton.href.replace(
            `?${inputItem.firstElementChild.name}=${inputItem.firstElementChild.value}`,
            ''
          );
        }
        console.log(searchButton.href);

        str = '?';
      }
    });
  }
}
checkboxFilter();
