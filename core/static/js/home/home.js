function updateBolaV(index) {
  const bolas = document.querySelectorAll('.bolaV');
  bolas.forEach((bola, i) => {
      if (i === index) {
          bola.style.backgroundColor = '#262626';
      } else {
          bola.style.backgroundColor = '#E1E5EE';
      }
  });
}

document.addEventListener("DOMContentLoaded", function() {
  const slides = document.querySelectorAll('.nossaHistoriaImg');
  let currentIndex = 0;
  let intervalo = 3000;

  function showSlide(index) {
    slides.forEach((slide, i) => {
      if (i === index) {
        slide.style.transform = 'translateX(0)';
      } else if (i < index) {
        slide.style.transform = 'translateX(-100%)';
      } else {
        slide.style.transform = 'translateX(100%)';
      }
    });
    updateBolaV(index);
  }

  function nextSlide() {
      currentIndex = (currentIndex + 1) % slides.length;
      showSlide(currentIndex);
  }

  setInterval(nextSlide, intervalo); // Altere o intervalo conforme necessário (em milissegundos)

  showSlide(currentIndex);    
});

document.addEventListener("DOMContentLoaded", function() {
  const container = document.querySelector('.cards');
  const cardWidth = 415; // Largura de cada cartão;
  let scrollAmount = 0; // Quantidade de rolagem atual

    document.getElementById('setaCarrosselEsquerda').addEventListener('click', () => {
        // Calcula a nova quantidade de rolagem
        scrollAmount = Math.max(scrollAmount - cardWidth, 0);
        container.scrollLeft = scrollAmount;
    });

    document.getElementById('setaCarrosselDireita').addEventListener('click', () => {
        // Calcula a nova quantidade de rolagem
        scrollAmount = Math.min(scrollAmount + cardWidth, container.scrollWidth - container.clientWidth);
        container.scrollLeft = scrollAmount;
    });
});