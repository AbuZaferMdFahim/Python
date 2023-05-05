//get searchform and page links
let searchForm = document.getElementById('searchForm')
let pageLink = document.getElementsByClassName('page-link')

//Ensure Search Form Exists
if(searchForm){
    for(let i=0;pageLink.length >i;i++){
        pageLink[i].addEventListener('click', function(e) {
            e.preventDefault()
            
            //get data attribute
            let page = this.dataset.page

            //add hidden search input to form
            searchForm.innerHTML += `<input value=${page} name = "page" hidden/>`

            //Submit Form
            searchForm.submit() 
        })
    }
}