
function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}


function typeWrite(text, element_id) {

  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  var i = 0;
  async function typeWriter() {
    await sleep(getRandomArbitrary(10, 20));
    if (i < text.length) {
      document.getElementById(element_id).innerHTML += text.charAt(i);
      i++;
      setTimeout(typeWriter, 0);
    }
  }
  typeWriter();
}


document.addEventListener("DOMContentLoaded", () => {
    fetch('/cinematics', {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then((response) => response.json())
    .then((result) => {
      let code = result[0];
      console.log(code);
      typeWrite(code, 'cine');
    });

});
