const profileBtn=document.querySelector(".profile__btn"),profileNavigation=document.querySelector(".profile__navigation");profileBtn.addEventListener("click",(()=>{profileNavigation.classList.toggle("profile__navigation__hidden")}));const sideNavShowBtns=document.querySelectorAll(".sideNavShowBtn"),sideNavHideBtns=document.querySelectorAll(".sideNavHideBtn"),sideNavs=document.querySelectorAll(".post__related__btn__links");sideNavShowBtns.forEach(((e,t)=>{e.addEventListener("click",(()=>{sideNavs[t].style.display="block"}))})),sideNavHideBtns.forEach(((e,t)=>{e.addEventListener("click",(()=>{sideNavs[t].style.display="none"}))}));const heartBtns=document.querySelectorAll(".heart__btn"),totalHearts=document.querySelectorAll(".heart__btn span"),heartIcons=document.querySelectorAll(".heart__btn i");heartBtns&&heartBtns.forEach(((e,t)=>{e.addEventListener("click",(n=>{n.preventDefault();const o=Number(e.dataset.postid);fetch("/like_action",{headers:{"Content-Type":"application/json"},method:"POST",body:JSON.stringify({post_id:o})}).then((e=>e.json())).then((n=>{e.classList.toggle("heart__btn__active"),totalHearts[t].textContent=n.totalLikes,heartIcons[t].classList.toggle("far"),heartIcons[t].classList.toggle("fas")}))}))}));