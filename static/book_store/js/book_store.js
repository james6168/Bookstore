$(document).ready(function () {
    var bookList = []
    var bookContainer = $('.book_container')
    var paginationBar = $('.pagination')
    var currentPage = $(location).attr('pathname')
    if (currentPage == '/') {
        currentPage = '/1/'
    }
    var currentPageInt = parseInt(currentPage.substring(1, 2))
    var nextPageInt = currentPageInt + 1
    if ($(location).attr('pathname') == '/') {
        var nextPage = $(location).attr('href') + `${nextPageInt}/`
    } else {
        var nextPage = $(location).attr('href').replace(currentPage, `/${nextPageInt}/`)
    }
    // var nextPage = $(location).attr('href').replace(currentPage, `/${nextPageInt}/`)
    var previousPageInt = parseInt(currentPage.substring(1, 2)) - 1
    var previousPage = $(location).attr('href').replace(currentPage, `/${previousPageInt}/`)

    $.ajax(
        {
            type: 'GET',
            url: `http://127.0.0.1:8000/api/v1/book/book-list/?page=${currentPageInt}`,
            success: function (response) {
                if (response.next != null) {
                    paginationBar.append(`<li class="page-item"><a class="page-link" href="${nextPage}">Next</a></li>`)
                }

                if (response.previous != null) {
                    paginationBar.append(`<li class="page-item"><a class="page-link" href="${previousPage}">Previous</a></li>`)
                }

                bookList = response.results

                for (i = 0; i < bookList.length; i++) {
                    bookName = bookList[i].name
                    bookDescription = bookList[i].description.substring(0, 100) + "..."
                    bookImage = bookList[i].images[0].book_image

                    bookContainer.append(`
                        <div class="card" style="width: 18rem;">
                            <img src="${bookImage}" class="card-img-top" alt="..." />
                            <div class="card-body">
                                <h5 class="card-title">${bookName}</h5>
                                <p class="card-text">
                                    ${bookDescription}
                                </p>
                                <a href="#" class="btn btn-primary">To book details</a>
                            </div>
                        </div>`
                    )
                }

            },
        }
    )

})









