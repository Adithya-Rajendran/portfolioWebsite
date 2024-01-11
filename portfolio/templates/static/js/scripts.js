/*!
* Start Bootstrap - Personal v1.0.1 (https://startbootstrap.com/template-overviews/personal)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-personal/blob/master/LICENSE)
*/

// Function to initialize the typing effect
function initTypingEffect() {
  const words = $("#typed").data("typed-items").split(",");
  let currentWordIndex = 0;

  function typeWords() {
    const currentWord = words[currentWordIndex];
    let charIndex = 0;
    const typingInterval = setInterval(() => {
      $("#typed").text(currentWord.substring(0, charIndex));
      charIndex++;

      if (charIndex > currentWord.length) {
        clearInterval(typingInterval);

        // Wait for a short time before typing the next word
        setTimeout(() => {
          $("#typed").text('');
          currentWordIndex = (currentWordIndex + 1) % words.length;
          typeWords();
        }, 3000);
      }
    }, 100);
  }

  typeWords();
}

// Call the function to initialize the typing effect
$(document).ready(function () {
  initTypingEffect();
});
