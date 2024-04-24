let publicidad = document.getElementById("publicidad");

setTimeout(() => {
    publicidad.setAttribute("class", "visible");
}, 5000)

let ok = document.getElementById("ok");

ok.addEventListener("click", () => {
    publicidad.setAttribute("class", "invisible");
})