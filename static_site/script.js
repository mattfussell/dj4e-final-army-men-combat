const ui_year = document.querySelector('#ui_current-year')

const setYear = function() {
    ui_year.innerText = new Date().getFullYear()
}

setYear()