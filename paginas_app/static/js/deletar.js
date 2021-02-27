
function deletar() {
    
if (confirm("Deseja apagar ?")) {
    alert('Deletado com sucesso !')
    window.location = "{% url 'post_delete' pk=pk %}";
    } else {
    alert('Cancelado com sucesso !')
    window.location = "{% url 'lista_post' %}"
    }
}

