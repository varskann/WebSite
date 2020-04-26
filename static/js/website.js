var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  console.log(slides.length);
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  slides[slideIndex-1].style.display = "block";  
  setTimeout(showSlides, 1000); // Change image every 2 seconds
}



var dance = {
  
  init: function() {
    this.dance();
  },
  
  config: {
    newSize: 40,
  },
  
  dance: function(config) {
    var newText = '',
        h1 = $('.dance'),
        text = $('.dance').text(),
        oldSize = h1.css('font-size'),
        length = text.length,
        i;
  
    console.log("Hola");
    console.log(h1.html);
    for( i = 0; i < length; i++ ) {
      
      newText += '<span>' + text.charAt(i) + '</span>';    
    }


    
    h1.html(newText);
    
    h1.on('mouseenter mouseleave', 'span', function(e) {
      var span = $(this);
      
      if( e.type == 'mouseenter') {
         
        span.stop(true,false).animate({fontSize: dance.config.newSize + 'px'});
        
      } else if( e.type == "mouseleave" ) {
        
        span.animate({fontSize: oldSize});
      }  
    });
  }
};

$(function() {
  dance.init();
});