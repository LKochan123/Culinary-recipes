document.addEventListener('DOMContentLoaded', function() {
    const nav = document.querySelector('.navbar')
    const navLinks = document.querySelectorAll('.nav-link')
    const navList = document.querySelector('.navbar-collapse')

    function addBackground() {
        if (window.scrollY > 0) {
            nav.classList.add('shadow-bg')
        } else {
            nav.classList.remove('shadow-bg')
        }
    }

    window.addEventListener('scroll', addBackground)
    navLinks.forEach(link => link.addEventListener('click', () => navList.classList.remove('show')))
})