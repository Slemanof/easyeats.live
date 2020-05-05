const Restaurantshow = {
  toggleClass(element, elementClass) {
    element.classList.toggle(elementClass);
  },

  showMore(element, exccerpt) {
    element.addEventListener('click', (event) => {
      const linkText = event.target.textContent;
      event.preventDefault();
      if (linkText == 'Show more') {
        element.textContent = 'Show less';
        this.toggleClass(
          document.querySelector('.restaurant-view__bottom-block'),
          'restaurant-view__bottom-block-visable'
        );
      } else {
        element.textContent = 'Show more';
        this.toggleClass(
          document.querySelector('.restaurant-view__bottom-block '),
          'restaurant-view__bottom-block-visable'
        );
      }
    });
  },
};
Restaurantshow.showMore(document.querySelector('.restaurant-view__show-more'));
