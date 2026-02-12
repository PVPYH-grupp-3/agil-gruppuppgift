let currentBox = 0;

document.addEventListener("keydown", function (event) {
  const boxes = document.querySelectorAll(".wordle-row.active .box");

  if (event.key === "Enter") {
    if (currentBox === 5) {
      console.log("Kollar gissning...");
      let userGuess = [];
      for (i = 0; i < boxes.length; i++) {
        userGuess.push(boxes[i].textContent);
      }
    }
  } else if (event.key === "Backspace") {
    if (currentBox > 0) {
      currentBox--;
      boxes[currentBox].textContent = "";
      console.log("Raderade, nu på ruta:", currentBox);
    }
  } else if (event.key.length === 1 && event.key.match(/[a-z]/i)) {
    if (currentBox < 5) {
      console.log(event.key);
      boxes[currentBox].textContent = event.key.toUpperCase();
      currentBox++;
      console.log("Lade till:", event.key, "Nu på ruta:", currentBox);
    }
  }
}); 
