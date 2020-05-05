const Filtershow = {
  toggleClass(element, elementClass) {
    element.classList.toggle(elementClass);
  },
  addClass(element, elementClass) {
    element.classList.toggle(elementClass);
  },
  removeClass(element, elementClass) {
    element.classList.toggle(elementClass);
  },

  showMore(element, exccerpt) {
    element.addEventListener('click', (event) => {
      const linkText = event.target.textContent;
      event.preventDefault();
      if (linkText == 'Show more') {
        element.textContent = 'Show less';
        this.toggleClass(
          document.querySelector('.main__filter__body-hidden'),
          'main__filter__body-hidden--visable'
        );
      } else {
        element.textContent = 'Show more';
        this.toggleClass(
          document.querySelector('.main__filter__body-hidden '),
          'main__filter__body-hidden--visable'
        );
      }
    });
  },
};
Filtershow.showMore(
  document.querySelector('.main__filter__body-show-more-btn')
);
