/** ------------------------------
 *  Functionality related with sidebar when user is not logged in
 *  ----------------------------- */
const applicationStuff = document.querySelector('.navigation__application__stuffs');
const aboutBtn = document.querySelector('.navigation__about__btn');

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


/*--------------------------------
* Functionality related with hiding messages
* -------------------------------- */ 
const msgHideBtns = document.querySelectorAll('.msg__hide__btn');
const msgContainers = document.querySelectorAll('.msg--container');

if (msgContainers) {
    msgHideBtns.forEach((btn, index) => {
        btn.addEventListener('click', () => {
            msgContainers[index].style.display = 'none';
        });
    });
}



/*------------------------------
Follow button related functionality
---------------------------------*/
const followBtns = document.querySelectorAll('.follow__btn');

followBtns.forEach(followBtn => {

    followBtn.addEventListener('click',function(e) {
        e.preventDefault();
    
        fetch('/follow_action', {
            headers : {
                'Content-Type' : 'application/json'
            },
            method : 'POST',
            body : JSON.stringify( {
                'user_id': Number(this.dataset.userid)
            })
        })
        .then(res => res.json()).then(res =>{
            this.textContent = (res['follow'] ? res['follow'] : res['unfollow']);
        })
    }); 
})
