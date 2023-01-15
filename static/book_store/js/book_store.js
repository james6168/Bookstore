$(document).ready(function () {
    var bookList = []
    var bookContainer = $('.book_container')

    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/api/v1/book/book-list/',
        success: function (response) {
            bookList = response
            for (i = 0; i < bookList.length; i++) {
                bookName = bookList[i].name
                bookDescription = bookList[i].description
                bookImage = bookList[i].images[0].book_image
                bookContainer.append(`<div class="card" style="width: 18rem;">
                <img src="${bookImage}" class="card-img-top" alt="..." />
                <div class="card-body">
                    <h5 class="card-title">${bookName}</h5>
                    <p class="card-text">
                        ${bookDescription}
                    </p>
                    <a href="#" class="btn btn-primary">To book details</a>
                </div>
            </div>`)
            }
        }
    })
})









