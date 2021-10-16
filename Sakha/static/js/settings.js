/*--------------------------------
* Functionality related with hiding flashed message
____________________________________*/
const msgContainer = document.querySelector('.message--container');
const msgHideBtn = document.querySelector('.message__hide__btn');

if(msgContainer) {
    
    msgHideBtn.addEventListener('click', () => {
        msgContainer.classList.add('message--hide');
    })
}



/*-------------------------------
 * Functionality related with sending json for names fields
---------------------------- */
const firstname = document.querySelector('.firstname__field');
const lastname = document.querySelector('.lastname__field');
const nameForm = document.querySelector('.nameForm');
const firstnameError = document.querySelector('.firstname__error');
const lastnameError = document.querySelector('.lastname__error');


nameForm.addEventListener('submit', e => {
    e.preventDefault();
    
    if(firstname.value.length > 30 && lastname.value.length > 30) {
        firstnameError.textContent = 'firstname should contain maximum 30 characters';
        lastnameError.textContent = 'lastname should contain maximum 30 characters';
    }
    else if(firstname.value.length > 30) {
        firstnameError.textContent = 'firstname should contain maximum 30 characters';
    }

    else  if(lastname.value.length > 30) {
        lastnameError.textContent = 'lastname should contain maximum 30 characters';
    }

    else {
        fetch('/updateName', {
            headers : {
                'Content-Type':'application/json'
            },
            method : 'POST',
            body : JSON.stringify({
                'firstname':firstname.value,
                'lastname':lastname.value
            })
        })
        .then(res => res.text()).then(res => res)
        .catch(res => console.log(res.text()))
    
        msgContainer.classList.remove('message--hide');
    }
})



/*-------------------------------
 * Functionality related with sending json for about_user field
---------------------------- */
const aboutUser = document.querySelector('.about_user');
const address = document.querySelector('.address')
const aboutForm = document.querySelector('.aboutForm');
const addressError = document.querySelector('.address__error');
const aboutError = document.querySelector('.about__error');


aboutForm.addEventListener('submit', e => {
    e.preventDefault();

    if(address.value.length > 200 && aboutUser.value.length > 5000) {
        addressError.textContent = "address should be maximum 200 characters long";
        aboutError.textContent = 'upto 5000 characters are allowed';
    }
    else if(address.value.length > 200) {
        addressError.textContent = "address should be maximum 200 characters long"; 
    } 
    else if(aboutUser.value.length > 5000) {
        aboutError.textContent = 'upto 5000 characters are allowed';
    }
    else {
        
        addressError.textContent = "";
        aboutError.textContent = "";

        fetch('/updateAboutUser', {
            headers : {
                'Content-Type':'application/json'
            },
            method : 'POST',
            body : JSON.stringify( {
                'about_user':aboutUser.value,
                'address':address.value
            })
        })
        .then(res => res.text()).then(res => res)
        .catch(res => console.log(res.text()))
    }
    
    msgContainer.classList.remove('message--hide');
});