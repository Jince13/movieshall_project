//Swiper
var swiper = new Swiper(".popular-content", {
      slidesPerView:1,
      spaceBetween: 10,
      autoplay: {
        delay: 5500,
        disableOnInteraction: false,
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      breakpoints:{
        280:{
            slidesPerView:1,
            spaceBetween: 10,
        },
        320:{
            slidesPerView:2,
            spaceBetween: 10,
        },
        510:{
            slidesPerView:2,
            spaceBetween: 10,
        },
        758:{
            slidesPerView:3,
            spaceBetween: 15,
        },
        900:{
            slidesPerView:4,
            spaceBetween: 20,
        },
      },
    });
// user
let user_img_box = document.querySelector('.user_img_box');
let navigation = document.querySelector('.navigation');
user_img_box.onclick = function(){
    navigation.classList.toggle('active')
}
// Rating & Review
//var stars = document.getElementsByClassName("fa-solid fa-star");
//var emoji = document.getElementById("emoji");
//
//stars[0].onclick = function(){
//    stars[0].style.color = "#f7c705";
//    stars[1].style.color = "#e4e4e4";
//    stars[2].style.color = "#e4e4e4";
//    stars[3].style.color = "#e4e4e4";
//    stars[4].style.color = "#e4e4e4";
//    emoji.style.transform = "translateX(0)";
//}
//stars[1].onclick = function(){
//    stars[0].style.color = "#f7c705";
//    stars[1].style.color = "#f7c705";
//    stars[2].style.color = "#e4e4e4";
//    stars[3].style.color = "#e4e4e4";
//    stars[4].style.color = "#e4e4e4";
//    emoji.style.transform = "translateX(-100px)";
//}
//stars[2].onclick = function(){
//    stars[0].style.color = "#f7c705";
//    stars[1].style.color = "#f7c705";
//    stars[2].style.color = "#f7c705";
//    stars[3].style.color = "#e4e4e4";
//    stars[4].style.color = "#e4e4e4";
//    emoji.style.transform = "translateX(-200px)";
//}
//stars[3].onclick = function(){
//    stars[0].style.color = "#f7c705";
//    stars[1].style.color = "#f7c705";
//    stars[2].style.color = "#f7c705";
//    stars[3].style.color = "#f7c705";
//    stars[4].style.color = "#e4e4e4";
//    emoji.style.transform = "translateX(-300px)";
//}
//stars[4].onclick = function(){
//    stars[0].style.color = "#f7c705";
//    stars[1].style.color = "#f7c705";
//    stars[2].style.color = "#f7c705";
//    stars[3].style.color = "#f7c705";
//    stars[4].style.color = "#f7c705";
//    emoji.style.transform = "translateX(-400px)";
//}

// rating form open & close
function OpenRatingForm(){
    document.getElementById("my_rating").style.display = "block";
    document.getElementById("play_img").style.filter ="blur(2px)";
    document.getElementById("play_text").style.filter ="blur(2px)";
    document.getElementById("play_rating").style.filter ="blur(2px)";
    document.getElementById("play_tags").style.filter ="blur(2px)";
    document.getElementById("play_watch_btn").style.filter ="blur(2px)";
    document.getElementById("play_feedback").style.filter ="blur(2px)";
}
function OpenThankYou(){
    document.getElementById("thank_you_form").style.display = "block";
//    document.getElementById("my_rating").style.display = "none";
    // document.getElementById("play_img").style.filter ="blur(2px)";
    // document.getElementById("play_text").style.filter ="blur(2px)";
    // document.getElementById("play_rating").style.filter ="blur(2px)";
    // document.getElementById("play_tags").style.filter ="blur(2px)";
    // document.getElementById("play_watch_btn").style.filter ="blur(2px)";
    // document.getElementById("play_feedback").style.filter ="blur(2px)";
}
function CloseThankYou(){
    document.getElementById("thank_you_form").style.display = "none";
}

//view reviews
function OpenSeeReviewForm(){
    document.getElementById("see_reviews").style.display = "block";
}
function CloseSeeReviewForm(){
    document.getElementById("see_reviews").style.display = "none";
}

//my profile edit
function toggleEdit(fieldId) {
            var field = document.getElementById(fieldId);
            var button = field.nextElementSibling;
            var isDisabled = field.disabled;

            field.disabled = !isDisabled;
            field.focus();

            if (isDisabled) {
                button.innerText = 'Cancel';
            } else {
                button.innerText = 'Update';
            }
        }

//Welcome message
//function OpenWelcome(){
//    document.getElementById("welcome_form").style.display = "block";
//}
//function CloseWelcome(){
//    document.getElementById("welcome_form").style.display = "none";
//}