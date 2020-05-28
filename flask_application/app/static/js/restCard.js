const showBtn = document.querySelectorAll(".restaurant-view__show-more");

for (let item of showBtn) {
  item.addEventListener("click", () => showMore(event));

  function showMore(event) {
    event.preventDefault();
    if (event.target.firstElementChild.textContent == "Show more") {
      event.target.firstElementChild.textContent = "Show less";
      toggleClass(
        event.target.previousElementSibling,
        "restaurant-view__bottom-block-visable"
      );
    } else {
      event.target.firstElementChild.textContent = "Show more";
      toggleClass(
        event.target.previousElementSibling,
        "restaurant-view__bottom-block-visable"
      );
      event.target.previousElementSibling.previousElementSibling.scrollIntoView(
        {
          behavior: "smooth",
          block: "start",
        }
      );
    }
  }
}

function toggleClass(element, elementClass) {
  element.classList.toggle(elementClass);
}
