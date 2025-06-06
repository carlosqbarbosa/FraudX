$(document).ready(function(){

    $('.currency').numeric();
    $('.currency').maskMoney({
        showSymbol: true,
        symbol: "$",
        decimal: ".",
        thousands: ",",
    });
        
    function checkForm() {
        let allFilled = true;

        $('.currency, #transaction-type').each(function(){
            let value = $(this).val().trim();
            if (value === '' || value === '0.00') {
                allFilled = false;
            }
        });

        if (allFilled) {
            $('#submit-button').prop('disabled', false).css('opacity', '1'); // Botão ativo
        } else {
            $('#submit-button').prop('disabled', true).css('opacity', '0.5'); // Botão opaco
        }
    }

    $('.currency, #transaction-type').on('input change', checkForm);

    $('#submit-button').prop('disabled', true).css('opacity', '0.5');
});