const showMoreFilter = document.querySelector(
  '.main__filter__body-show-more-btn'
);

function toggleClass(element, elementClass) {
  element.classList.toggle(elementClass);
}

showMoreFilter.addEventListener('click', showMore);

function showMore() {
  if (showMoreFilter.textContent == 'Show more') {
    showMoreFilter.textContent = 'Show less';
    toggleClass(
      document.querySelector('.main__filter__body-hidden'),
      'main__filter__body-hidden--visable'
    );
  } else {
    showMoreFilter.textContent = 'Show more';
    toggleClass(
      document.querySelector('.main__filter__body-hidden '),
      'main__filter__body-hidden--visable'
    );
  }
}
