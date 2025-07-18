// reusable form validation and spinner functionality
// This script handles form submission with a spinner and validation
document.addEventListener("DOMContentLoaded", function () {
  const forms = document.querySelectorAll(".spinner-form");

  forms.forEach((form) => {
    form.addEventListener("submit", function (e) {
      e.preventDefault(); // prevent default submit first

      const button = form.querySelector(".spinner-button");
      const text = button.querySelector(".btn-text");
      const spinner = button.querySelector(".btn-spinner");

      // Show spinner, hide text, disable button
      text.style.display = "none";
      spinner.style.display = "inline-block";
      button.disabled = true;

      // Submit after showing spinner
      form.submit();
    });
  });
});
