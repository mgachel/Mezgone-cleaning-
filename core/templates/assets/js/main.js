// Initialize Lucide icons if available
window.addEventListener('DOMContentLoaded', () => {
  if (window.lucide && typeof window.lucide.createIcons === 'function') {
    window.lucide.createIcons();
  }

  // Mobile menu toggle
  const burger = document.querySelector('[data-open-mobile]');
  const close = document.querySelector('[data-close-mobile]');
  const menu = document.querySelector('#mobile-menu');
  const overlay = document.querySelector('#mobile-overlay');

  function openMenu(){
    menu?.classList.add('open');
    overlay?.classList.remove('hidden');
  }
  function closeMenu(){
    menu?.classList.remove('open');
    overlay?.classList.add('hidden');
  }

  burger?.addEventListener('click', openMenu);
  close?.addEventListener('click', closeMenu);
  overlay?.addEventListener('click', closeMenu);

  // Simple testimonial rotator if present
  const slides = document.querySelectorAll('[data-testimonial]');
  const dots = document.querySelectorAll('[data-testimonial-dot]');
  if (slides.length > 1) {
    let idx = 0;
    function show(i){
      slides.forEach((el, k)=>{
        el.classList.toggle('hidden', k !== i);
      });
      dots.forEach((d, k)=>{
        d.classList.toggle('bg-primary', k === i);
        d.classList.toggle('bg-gray-300', k !== i);
      });
      if (window.lucide) window.lucide.createIcons();
    }
    show(0);
    setInterval(()=>{
      idx = (idx + 1) % slides.length;
      show(idx);
    }, 5000);
    dots.forEach((d, k)=> d.addEventListener('click', ()=>{ idx = k; show(idx); }));
  }
});
