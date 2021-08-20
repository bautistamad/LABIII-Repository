window.sr = ScrollReveal();
sr.reveal(".navbar", {
  duration: 2000,
  origin: "bottom",
});
window.sr = ScrollReveal();
sr.reveal(".header-content-left ", {
  duration: 2000,
  origin: "top",
  distance: "300px",
});
window.sr = ScrollReveal();
sr.reveal(".header-content-right", {
  duration: 2000,
  origin: "right",
  distance: "300px",
});

window.sr = ScrollReveal();
sr.reveal(".header-btn", {
  duration: 2000,
  origin: "bottom",
  delay: 1000,
});
window.sr = ScrollReveal();
sr.reveal("#testimonial", {
  duration: 2000,
  origin: "left",
  distance: "300px",
  viewFactpr: 0.2,
});
sr.reveal(".info-left ", {
  duration: 2000,
  origin: "left",
  distance: "300px",
});
sr.reveal(".info-right", {
  duration: 2000,
  origin: "right",
  distance: "300px",
});
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();

    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth",
    });
  });
});