$(function(){
    $("#id_marca").change(function(){
        $("#id_modelo").empty()

        fetch('http://127.0.0.1:8000/modelos/')
        .then(result => {
            return result.json();
        })
        .then(result => {
            marca = $("#id_marca").val()

            for(let i = 0; i < result.length; i++){
                if(result[i].marca == marca)
                {
                    $("#id_modelo").append(`<option value=${result[i].id}>${result[i].nombre}</value>`)
                }
            }
        })
        .catch(error => {
            console.log(error)
        })
    })
})