// ************************ Drag and drop ***************** //
let dropArea = document.getElementById("drop-area")

// Prevent default drag behaviors
;['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false)
    document.body.addEventListener(eventName, preventDefaults, false)
})

// Highlight drop area when item is dragged over it
;['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false)
})

;['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false)
})

// Handle dropped files
dropArea.addEventListener('drop', handleDrop, false)

function preventDefaults(e) {
    e.preventDefault()
    e.stopPropagation()
}

function highlight(e) {
    var dropArea = document.getElementById("drop-area")
    dropArea.classList.add('highlight')
}

function unhighlight(e) {
    var dropArea = document.getElementById("drop-area")
    dropArea.classList.remove('highlight')
}

function handleDrop(e) {
    var dt = e.dataTransfer
    var files = dt.files
    handleFiles(files)
}

function handleFiles(files) {
    var fileElem = document.querySelector('#fileElem')
    fileElem.files = files
    console.log(document.querySelector('#fileElem').files)
    console.log(files)
    file = [...files]
    var file_name_field = document.querySelector('.fileview')
    var status = validation(file[0].name)
    if (status == false){
        file_name_field.innerHTML = "Невозможно загрузить данный файл"
        var button = document.querySelector('.submit_button')
        button.style.display = 'none'
        var dropArea = document.getElementById("drop-area")
        dropArea.style.borderColor = 'rgb(255, 0, 0)'
        
    }else{
        file_name_field.innerHTML = file[0].name
        var button = document.querySelector('.submit_button')
        button.style.display = 'block'
        var dropArea = document.getElementById("drop-area")
        dropArea.style.borderColor = 'rgb(94, 209, 0)'
    }
}

function validation(filename){
    if (filename.endsWith('xlsx') || filename.endsWith('xls')){
        return true
    }else{ return false }
}


function waiting_upload(button){
    button.style.pointerEvents = 'none'
    button.innerText = "Данные загружаются"
    button.style.background = 'rgb(255, 250, 0)'

}

