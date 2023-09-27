// Script para carregar o calendário
$(document).ready(function(){
                      
           $(function(){
               $("#conteudo-pagina-lida").load("/calendario"); 
           });
       
});



   
// Script para o botão flutuante voltar ao topo
function toggleFAB(fab){
      if(document.querySelector(fab).classList.contains('show')){
        document.querySelector(fab).classList.remove('show');
      }else{
        document.querySelector(fab).classList.add('show');
      }
}

document.querySelector('.fab .main').addEventListener('click', function(){
      toggleFAB('.fab');
});

document.querySelectorAll('.fab ul li button').forEach((item)=>{
      item.addEventListener('click', function(){
        toggleFAB('.fab');
      });
});
    
 