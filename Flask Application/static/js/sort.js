const sortOptions = document.querySelector('#sortOptions');
sortOptions.addEventListener('change', () => {
  switch (sortOptions.value) {
    case 'rating-sort-desc':
      mySortDesc('data-rating');
      break;
    case 'rating-sort-asc':
      mySort('data-rating');
      break;
    case 'price-sort-asc':
      mySort('data-price');
      break;
    case 'price-sort-desc':
      mySortDesc('data-price');
      break;
  }
});

function mySort(attribute) {
  const restaurantsOutput = document.querySelector('.restaurant-view');
  for (let i = 0; i < restaurantsOutput.children.length; i++) {
    for (let j = i; j < restaurantsOutput.children.length; j++) {
      if (
        Number(restaurantsOutput.children[i].getAttribute(attribute)) >
        Number(restaurantsOutput.children[j].getAttribute(attribute))
      ) {
        replaceNode = restaurantsOutput.replaceChild(
          restaurantsOutput.children[j],
          restaurantsOutput.children[i]
        );
        insertAfter(replaceNode, restaurantsOutput.children[i]);
      }
    }
  }
}

function mySortDesc(attribute) {
  const restaurantsOutput = document.querySelector('.restaurant-view');
  for (let i = 0; i < restaurantsOutput.children.length; i++) {
    for (let j = i; j < restaurantsOutput.children.length; j++) {
      if (
        Number(restaurantsOutput.children[i].getAttribute(attribute)) <
        Number(restaurantsOutput.children[j].getAttribute(attribute))
      ) {
        replaceNode = restaurantsOutput.replaceChild(
          restaurantsOutput.children[j],
          restaurantsOutput.children[i]
        );
        insertAfter(replaceNode, restaurantsOutput.children[i]);
      }
    }
  }
}

function insertAfter(elem, refElem) {
  return refElem.parentNode.insertBefore(elem, refElem.nextElementSibling);
}
