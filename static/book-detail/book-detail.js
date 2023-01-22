$(document).ready(function () {
    var currentPage = parseInt($(location).attr('pathname').substring(13, 15))
    var bookName = null
    var bookDescription = null
    var bookCreatedAt = null
    var bookImages = []
    var bookPrice = null
    var bookNameRender = $('#bookName')
    var bookDescriptionRender = $('#bookDescription')
    var bookCreatedAtRender = $('#bookCreatedAt')
    var bookPriceRender = $('#bookPrice')

    $.ajax({
        url: `http://127.0.0.1:8000/api/v1/book/?id=${currentPage}`,
        type: 'GET',
        async: false,
        success: function (response) {
            bookName = response.name
            bookDescription = response.description
            bookCreatedAt = response.created_at
            console.log(bookCreatedAt)
            bookPrice = response.price
            for (i = 0; i < response.images.length; i++) {
                bookImages.push(response.images[i].book_image)
            }
            bookNameRender.append(bookName)
            bookDescriptionRender.append(bookDescription)
            bookCreatedAtRender.append(bookCreatedAt)
            bookPriceRender.append(bookPrice)
            $('#bookImage1').attr('src', bookImages[0])
            $('#bookImage2').attr('src', bookImages[1])
            $('#bookImage3').attr('src', bookImages[2])
        }  
    })



})