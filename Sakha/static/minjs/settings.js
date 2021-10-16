const msgContainer=document.querySelector(".message--container"),msgHideBtn=document.querySelector(".message__hide__btn");msgContainer&&msgHideBtn.addEventListener("click",(()=>{msgContainer.classList.add("message--hide")}));const firstname=document.querySelector(".firstname__field"),lastname=document.querySelector(".lastname__field"),nameForm=document.querySelector(".nameForm"),firstnameError=document.querySelector(".firstname__error"),lastnameError=document.querySelector(".lastname__error");nameForm.addEventListener("submit",(e=>{e.preventDefault(),firstname.value.length>30&&lastname.value.length>30?(firstnameError.textContent="firstname should contain maximum 30 characters",lastnameError.textContent="lastname should contain maximum 30 characters"):firstname.value.length>30?firstnameError.textContent="firstname should contain maximum 30 characters":lastname.value.length>30?lastnameError.textContent="lastname should contain maximum 30 characters":(fetch("/updateName",{headers:{"Content-Type":"application/json"},method:"POST",body:JSON.stringify({firstname:firstname.value,lastname:lastname.value})}).then((e=>e.text())).then((e=>e)).catch((e=>console.log(e.text()))),msgContainer.classList.remove("message--hide"))}));const aboutUser=document.querySelector(".about_user"),address=document.querySelector(".address"),aboutForm=document.querySelector(".aboutForm"),addressError=document.querySelector(".address__error"),aboutError=document.querySelector(".about__error");aboutForm.addEventListener("submit",(e=>{e.preventDefault(),address.value.length>200&&aboutUser.value.length>5e3?(addressError.textContent="address should be maximum 200 characters long",aboutError.textContent="upto 5000 characters are allowed"):address.value.length>200?addressError.textContent="address should be maximum 200 characters long":aboutUser.value.length>5e3?aboutError.textContent="upto 5000 characters are allowed":(addressError.textContent="",aboutError.textContent="",fetch("/updateAboutUser",{headers:{"Content-Type":"application/json"},method:"POST",body:JSON.stringify({about_user:aboutUser.value,address:address.value})}).then((e=>e.text())).then((e=>e)).catch((e=>console.log(e.text())))),msgContainer.classList.remove("message--hide")}));