
$(".option").click(function(){
    if ($(this).hasClass("active")){
        $(this).removeClass('active');
    } else {
        $(".option").removeClass("active");
        $(this).addClass("active");
    }
});

var slide_index = [0, 1, 2, 3, 4];
var new_index = 5;
show_slides(slide_index);


showDivs(slideIndex);

function slide_image(n) {
    shift_images(current_images, )
  showDivs(slideIndex += n);
}

function shift_images(current_images, new_index, total_images) {
    current_images.shift();
    if (new_index > total_images ) {new_index = 0} 
       
    if (new_index < 0 ) {new_index = 0} 

    current_images.push(new_index);
    new_index++;

}
function show_slides() {
    var i;
    var slides = document.getElementsByClassName("option");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    
    // for (i = slide_index; i < slide_index+5; i++) {
    //     slides[i].style.display = "block";  
    // }
    console.log(slide_index);

    slide_index.forEach(function (item, index) {
        slides[item].style.display = "inline";
    });
    slide_index.shift();
    if (new_index > slides.length / 2 ) {new_index = 0}    
 
    slide_index.push(new_index);
    new_index++;
    // slides[slide_index-1].style.display = "block";  
    // setTimeout(show_slides, 1000); 
}