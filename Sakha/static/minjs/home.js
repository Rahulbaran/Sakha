const sideNavShowBtns=document.querySelectorAll(".sideNavShowBtn"),sideNavHideBtns=document.querySelectorAll(".sideNavHideBtn"),sideNavs=document.querySelectorAll(".post__related__btn__links");sideNavShowBtns.forEach(((e,t)=>{e.addEventListener("click",(()=>{sideNavs[t].style.display="block"}))})),sideNavHideBtns.forEach(((e,t)=>{e.addEventListener("click",(()=>{sideNavs[t].style.display="none"}))}));const heartBtns=document.querySelectorAll(".heart__btn"),totalHearts=document.querySelectorAll(".heart__btn span"),heartIcons=document.querySelectorAll(".heart__btn i");heartBtns&&heartBtns.forEach(((e,t)=>{e.addEventListener("click",(s=>{s.preventDefault();const n=Number(e.dataset.postid);fetch("/like_action",{headers:{"Content-Type":"application/json"},method:"POST",body:JSON.stringify({post_id:n})}).then((e=>e.json())).then((s=>{e.classList.toggle("heart__btn__active"),totalHearts[t].textContent=s.totalLikes,heartIcons[t].classList.toggle("far"),heartIcons[t].classList.toggle("fas")}))}))}));