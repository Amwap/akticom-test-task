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
    dropArea.classList.add('highlight')
}

function unhighlight(e) {
    dropArea.classList.remove('active')
}

function handleDrop(e) {
    var dt = e.dataTransfer
    var files = dt.files
    handleFiles(files)
}

function handleFiles(files) {
    files = [...files]
    var file_name_field = document.querySelector('.fileview')
    var text = document.createElement('p');
    text.innerText = files[0].name
    console.log(text)
    file_name_field.innerHTML = files[0].name
    var button = document.querySelector('.submit_button')
    button.style.display = 'block'

}

// let uploadProgress = []
// let progressBar = document.getElementById('warning')

// function initializeProgress(numFiles) {
//     var progrbar = document.querySelector('#warning')
//     progrbar.style.display = 'block'
//     progressBar.value = 0
//     uploadProgress = []

//     for (let i = numFiles; i > 0; i--) {
//         uploadProgress.push(0)
//     }
// }

// function updateProgress(fileNumber, percent) {
//     uploadProgress[fileNumber] = percent
//     let total = uploadProgress.reduce((tot, curr) => tot + curr, 0) / uploadProgress.length
//     console.debug('update', fileNumber, percent, total)
//     progressBar.value = total
// }



// function previewFile(file) {
//     let reader = new FileReader()
//     reader.readAsDataURL(file)
//     reader.onloadend = function () {
//         let text = document.createElement('p')
//         text.text = file
//         document.getElementById('warning').appendChild(text)
//     }
// }

// function uploadFile(file, i) {
    // var url = 'http://127.0.0.1:8000/'
    // var xhr = new XMLHttpRequest()
    // xhr.open('POST', url, true)
    // // xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
    // var token = document.getElementsByName('csrfmiddlewaretoken')
    // xhr.setRequestHeader("x-csrf-token", token[0].value); 

    // // Update progress (can be used to show progress indicator)
    // xhr.upload.addEventListener("progress", function (e) {
    //     updateProgress(i, (e.loaded * 100.0 / e.total) || 100)
    // })

    // xhr.addEventListener('readystatechange', function (e) {
    //     if (xhr.readyState == 4 && xhr.status == 200) {
    //         updateProgress(i, 100) // <- Add this
    //     }
    //     else if (xhr.readyState == 4 && xhr.status != 200) {
    //         // Error. Inform the user
    //     }
    // })

    // var formData = new FormData()
    // formData.append('file', file)
    // xhr.send(formData)
// }

// var options = {
//     url: '/upload/',
//     type: "POST",
//      error: function(response) {
//              alert('Something went Wrong. Try Again');
//       },
//       success: function(response) {
//           if ( response.status == 'success' ) {
//             alert('success');
//            }
//       }
// };

// $('#my-form').ajaxSubmit(options);

// $('#my-form').submit(function(){
//     var formData = new FormData($(this)[0]);
//     $.ajax({
//             url: '/upload/',
//             type: 'POST',
//             data: formData,
//             async: false,
//             success: function (data) {
//                 alert(data)
//             },
//             cache: false,
//             contentType: false,
//             processData: false
//     });
//     return false;
// });














// function main(){
//     // функция отправляющая Васю копать огород
//     var home = new Home()
//     var jobs = new Jobs()
//     var vasya = home.users.get('Вася')
//     var job = jobs.get('Копать огород')
//     vasya.doJob(job.id)
//     vasya.start()
// }