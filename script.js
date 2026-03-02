const lines = document.querySelectorAll("#lyrics div");
let index = 0;

function highlightLine() {
  lines.forEach(line => line.classList.remove("highlight"));
  if (index < lines.length) {
    lines[index].classList.add("highlight");
    index++;
  } else {
    // Trigger ARMS animation at the end
    const ending = document.getElementById("ending");
    ending.classList.add("grow-text");
    clearInterval(interval);
  }
}

const interval = setInterval(highlightLine, 4250);
highlightLine();