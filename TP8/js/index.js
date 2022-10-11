const d = document;
const btnMenu = d.querySelector(".panel-btn");

btnMenu.addEventListener("click", (e) => {
    if (e.target.matches(".panel-btn") || e.target.matches(".panel-btn *")){
        d.querySelector(".menu").classList.toggle("is-active")
        d.querySelector(".panel-btn").classList.toggle("is-active")
    }
})
