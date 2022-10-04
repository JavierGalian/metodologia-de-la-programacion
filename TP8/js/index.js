var nombreGrupo = 'NOMBRE_TEAM  ';
nombreDelGrupo = () => document.write(nombreGrupo);


integrantesGrupo = ['name1','name2','name3'];
function mostrarLista(){
    for (let i = 0; i <= 2; i++) {
        document.querySelector("#lista").innerHTML += "<li>"+ integrantesGrupo[i]+"</li>";
    }
}
integrantesGrupo.forEach(function(element){
    document.querySelector("#lista").innerHTML += "<li>"+ integrantesGrupo[i]+"</li>";
});