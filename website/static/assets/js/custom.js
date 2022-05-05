// (function ($){
//     "use strict";
//     function fractionPagination (carousel, number){

//         var currentItem = number+1 ;
//         carousel.find(".fraction-current").html(currentItem);
//         var totalItems = carousel.find(".carousel-item").length;
//         carousel.find(".fraction-total").html(totalItems);

//     }

//     if($(".carousel").length){
//         $(".carousel").each(function(){
//             var thisCarousel = $(this);

//             fractionPagination(thisCarousel,0);

//             thisCarousel.on("slide.bs.carousel",function (e){
//                 fractionPagination($(this),$(e.relatedTarget).index());
//             });
//         });
//     }
// })(jQuery);
