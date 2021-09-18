/** ------------------------------
 *  Functionality related with sidebar when user is not logged in
 *  ----------------------------- */
const applicationStuff = document.querySelector('.navigation__application__stuffs');
const aboutBtn = document.querySelector('.navigation__about__btn');
console.log(applicationStuff, aboutBtn);

if(aboutBtn) {
    aboutBtn.addEventListener('click', () => {
        applicationStuff.classList.toggle('navigation__application__show__stuffs');
    })
}


/** ------------------------------
 *  Functionality related with sidebar when user is logged in
 *  ----------------------------- */
const navigationProfileWrapper = document.querySelector('.navigation__user__profile__wrapper');

if (navigationProfileWrapper) {
    navigationProfileWrapper.addEventListener('click', () => {
        applicationStuff.classList.toggle('navigation__application__show__stuffs');
    })
}