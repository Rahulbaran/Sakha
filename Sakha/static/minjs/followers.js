const followBtns=document.querySelectorAll(".follow__btn");followBtns.forEach((t=>{t.addEventListener("click",(function(t){t.preventDefault(),fetch("/follow_action",{headers:{"Content-Type":"application/json"},method:"POST",body:JSON.stringify({user_id:Number(this.dataset.userid)})}).then((t=>t.json())).then((t=>{this.textContent=t.follow?t.follow:t.unfollow}))}))}));