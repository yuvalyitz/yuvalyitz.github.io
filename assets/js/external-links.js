/* Open links that leave the site in a new tab, so the site stays open.
   Counts as leaving: another host, the Scheduling Zoo app (served from this
   host but a separate app), and PDFs. Mail links and in-page anchors are left
   alone. */
(function () {
  var APPS = ["/lean-scheduling-zoo/", "/parameterized-scheduling-zoo/"];
  document.querySelectorAll("a[href]").forEach(function (a) {
    if (a.hasAttribute("target")) return;
    var href = a.getAttribute("href");
    if (!href || href.charAt(0) === "#") return;
    var url;
    try { url = new URL(a.href, location.href); } catch (e) { return; }
    if (url.protocol !== "http:" && url.protocol !== "https:") return;
    var leaves = url.host !== location.host ||
      APPS.some(function (p) { return url.pathname.indexOf(p) === 0; }) ||
      /\.pdf$/i.test(url.pathname);
    if (leaves) {
      a.target = "_blank";
      a.rel = ((a.rel || "") + " noopener noreferrer").trim();
    }
  });
})();
