function abrirFormulario(params) {
  let obj = document.querySelector("#form-cadastro");
  obj.removeAttribute("style")
}

function fecharFormulario(params) {
  params.closest("#form-cadastro").setAttribute("style", "display: none;")
}

function cancelar(params) {
  console.log("oi")
  params.closest("#alert").setAttribute("style", "display: none;")
}