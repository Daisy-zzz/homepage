(() => {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('#site-nav');
  if (toggle && nav) {
    toggle.hidden = false;
    document.documentElement.classList.add('nav-enhanced');
    const close = () => { nav.classList.remove('is-open'); toggle.setAttribute('aria-expanded', 'false'); };
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('is-open', open);
    });
    nav.addEventListener('click', event => { if (event.target.closest('a')) close(); });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && nav.classList.contains('is-open')) { close(); toggle.focus(); }
    });
  }
  const input = document.querySelector('#publication-search');
  if (!input) return;
  const papers = [...document.querySelectorAll('[data-publication]')];
  const count = document.querySelector('#result-count');
  const empty = document.querySelector('#empty-state');
  document.querySelector('[data-search-tools]').hidden = false;
  const filter = () => {
    const words = input.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
    let visible = 0;
    papers.forEach(paper => {
      const matches = words.every(word => paper.dataset.search.toLowerCase().includes(word));
      paper.hidden = !matches;
      if (matches) visible += 1;
    });
    count.textContent = `${visible} / ${papers.length} papers`;
    empty.hidden = visible > 0;
  };
  input.addEventListener('input', filter);
  filter();
})();
