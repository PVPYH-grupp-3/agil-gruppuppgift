let currentBox = 0;

document.addEventListener("keydown", function (event) {
  const activeRow = document.querySelector(".wordle-row.active");
  if (!activeRow) return;
  const boxes = activeRow.querySelectorAll(".box");

  if (event.key === "Enter") {
    if (currentBox === 5) {
      let userGuess = "";
      for (let i = 0; i < boxes.length; i++) {
        userGuess += boxes[i].textContent;
      }

      fetch("/guess", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ guess: userGuess.toLowerCase() }),
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.error) {
            console.log("Ogiltig gissning");
            return;
          }

          // Colors
          for (let i = 0; i < boxes.length; i++) {
            setTimeout(() => {
              boxes[i].classList.add("flip");
              setTimeout(() => {
                if (data.result[i] === "1") boxes[i].classList.add("correct");
                else if (data.result[i] === "2")
                  boxes[i].classList.add("present");
                else boxes[i].classList.add("absent");
              }, 250);
            }, i * 150);
          }

          setTimeout(
            () => {
              if (data.won) {
                alert("Du vann!");
                return;
              }

              const nextRow = activeRow.nextElementSibling;
              if (nextRow) {
                activeRow.classList.remove("active");
                nextRow.classList.add("active");
                currentBox = 0;
              } else {
                const word = document.getElementById("game").dataset.word;
                alert(`Game over! Det rätta ordet var: ${word.toUpperCase()}`);
              }
            },
            5 * 150 + 500,
          );
        });
    }
  } else if (event.key === "Backspace") {
    if (currentBox > 0) {
      currentBox--;
      boxes[currentBox].textContent = "";
    }
  } else if (event.key.length === 1 && event.key.match(/[a-z]/i)) {
    if (currentBox < 5) {
      boxes[currentBox].textContent = event.key.toUpperCase();
      currentBox++;
    }
  }
});
