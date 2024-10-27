// Description: This file contains the JavaScript code for the base.html file.
function updateClock() {
  const now = new Date();
  document.getElementById("clock").innerText = now.toLocaleTimeString();
}
setInterval(updateClock, 1000);
updateClock(); // Initial call to set the clock immediately

function toggleMessage() {
  const message = document.getElementById("welcome-message");
  if (message.style.display === "none") {
    message.style.display = "block";
  } else {
    message.style.display = "none";
  }
}
