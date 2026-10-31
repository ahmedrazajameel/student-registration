document.addEventListener("DOMContentLoaded", function () {
    var email = document.getElementById("email");
    var hint = document.getElementById("email_hint");

    if (email && hint) {
        email.addEventListener("input", function () {
            var value = email.value;
            if (value === "") {
                hint.textContent = "";
                hint.style.color = "";
                return;
            }
            // Simple check: must contain @ and a dot after the @
            var looksValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
            if (looksValid) {
                hint.textContent = "✓ Email format looks good";
                hint.style.color = "green";
            } else {
                hint.textContent = "✗ Email needs to look like name@example.com";
                hint.style.color = "red";
            }
        });
    }
});