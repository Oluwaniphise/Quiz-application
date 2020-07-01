//smooth scroll from stack overflow thru brad traversy
$(function() {
  // Smooth Scrolling
  $('a[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});




//scrollreveal animation
window.sr = ScrollReveal();
sr.reveal('.img_overlay_heading',{
  duration:2000,
  origin:'top',
  distance:"200px"});

sr.reveal('.img_overlay_par',{
  duration:2000,
  origin:'bottom',
  distance:"200px",
  delay:500
});
 
sr.reveal('.welcome',{
  duration:2500,
  delay:500,
  origin:'right',
  distance:"200px"

});

sr.reveal('.Sunday_worship,.Monday_bible,.Thursday_revival',{
  duration:2000,
  origin:'left',
  viewFactor:0.2,
  distance:"200px"

});


sr.reveal('.container-fluid .mission',{
  duration:2000,
  origin:'bottom',
  viewFactor:0.2,
  distance:"200px"
});

