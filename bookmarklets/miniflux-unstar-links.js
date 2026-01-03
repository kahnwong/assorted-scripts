javascript: (function () {
  const buttons = document.querySelectorAll("li.item-meta-icons-star button");
  buttons.forEach((button) => button.click());
  console.log(`Clicked ${buttons.length} buttons.`);
})();
