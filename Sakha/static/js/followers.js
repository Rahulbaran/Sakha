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