const date = new Date();
document.querySelector('.year').innerHTML = date.getFullMonthName()

setTimeout(function () {
    $('#message').fadeOut('slow');
}, 3000);