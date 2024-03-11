const navItems = document.querySelectorAll(".nav-link");

navItems.forEach((item) => {
  item.addEventListener("click", () => {
    navItems.forEach((item) => item.classList.remove("active"));
    item.classList.add("active");
  });
});

document.getElementById("contactForm").addEventListener("submit", function (e) {
  e.preventDefault();

  // Send email function here

  document.getElementById("responseMessage").innerText =
    "Message sent successfully!";
});