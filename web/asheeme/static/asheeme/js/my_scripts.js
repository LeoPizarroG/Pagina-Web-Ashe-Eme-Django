$(document).ready(function() {
    $('#id_idProducto').attr('readonly','readonly');   
    
    $('#texto_buscado').on('keyup', function() {
        var texto = $(this).val().toLowerCase();
        $('#tabla_productos tr').filter (function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(texto) > -1)
        });
    });
});