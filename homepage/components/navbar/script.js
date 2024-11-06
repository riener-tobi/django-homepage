const burgerMenu = document.querySelector('span.burger-menu');
const navLinks = document.querySelector('div.nav-links');

burgerMenu.addEventListener('click', function(event){
    if(navLinks.style.visibility == "hidden"){
        navLinks.style.visibility = "visible";
        navLinks.style.opacity = "1";
    }
    else{
        navLinks.style.visibility = "hidden";
        navLinks.style.opacity = "0";
    }
});

window.onresize = (event) =>{
    if(document.body.clientWidth >= 850){
        navLinks.style.visibility = "";
        navLinks.style.opacity = "";
    }
};