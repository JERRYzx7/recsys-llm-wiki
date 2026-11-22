// 主題切換、wiki 側欄搜尋、簡報 iframe 焦點
(function () {
  var root = document.documentElement;
  var btn = document.querySelector('.theme-btn');
  function isDark() {
    return root.dataset.theme === 'dark' ||
      (!root.dataset.theme && window.matchMedia('(prefers-color-scheme: dark)').matches);
  }
  function syncDeck() {
    var deck = document.getElementById('deck');
    try { if (deck && deck.contentDocument) deck.contentDocument.documentElement.dataset.theme = isDark() ? 'dark' : 'light'; } catch (e) {}
  }
  function label() { if (btn) btn.textContent = isDark() ? '白紙' : '黑板'; }
  label();
  if (btn) btn.addEventListener('click', function () {
    root.dataset.theme = isDark() ? 'light' : 'dark';
    try { localStorage.setItem('theme', root.dataset.theme); } catch (e) {}
    label(); syncDeck();
  });

  // 側欄搜尋
  var q = document.querySelector('.side-search');
  if (q) q.addEventListener('input', function () {
    var v = q.value.trim().toLowerCase();
    document.querySelectorAll('.wiki-side li').forEach(function (li) {
      li.style.display = !v || li.textContent.toLowerCase().indexOf(v) !== -1 ? '' : 'none';
    });
  });
  // 手機版預設收合側欄
  var det = document.querySelector('.side-details');
  if (det && window.matchMedia('(max-width: 860px)').matches) det.open = false;

  // 簡報：載入後把焦點交給 iframe，方向鍵可直接翻頁；主題跟著網站
  var deck = document.getElementById('deck');
  if (deck) deck.addEventListener('load', function () {
    if (localStorage && (function(){try{return localStorage.getItem('theme')}catch(e){return null}})()) syncDeck();
    try { deck.contentWindow.focus(); } catch (e) {}
  });
})();
