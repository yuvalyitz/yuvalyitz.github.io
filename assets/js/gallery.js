document.addEventListener('DOMContentLoaded', function () {
  const gallery = document.getElementById('gallery');
  if (!gallery) return;

  // The grid remains usable if the external justified-gallery plugin is unavailable.
  if (window.jQuery && jQuery.fn.justifiedGallery) {
    jQuery(gallery).justifiedGallery({ rowHeight: 260, lastRow: 'nojustify', margins: 8 });
  }
  if (!window.PhotoSwipeLightbox || !window.PhotoSwipe) return;
  const lightbox = new PhotoSwipeLightbox({
    gallery: '#gallery',
    children: 'a',
    pswpModule: PhotoSwipe,
    paddingFn: () => ({ top: 30, bottom: 30, left: 20, right: 20 })
  });
  lightbox.init();
});
