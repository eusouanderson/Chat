const messageInput = document.getElementById("message-input");
const submitButton = document.getElementById("submit-button");
const messageContainer = document.getElementById("message-container");

function exibirNotificacao() {
  if (Notification.permission === "granted") {
    var notification = new Notification("Nova mensagem recebida!");
  } else if (Notification.permission !== "denied") {
    Notification.requestPermission().then(function (permission) {
      if (permission === "granted") {
        var notification = new Notification("Nova mensagem recebida!");
      }
    });
  }
}
exibirNotificacao()