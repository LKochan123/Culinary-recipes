const body = document.querySelector('body')
const nav = document.querySelector('.navbar')
const colorBtn = document.querySelector('nav .navbar-nav .color-btn')
let theme = localStorage.getItem('theme')

const addShadow = () => {
    window.scrollY > 1 ? nav.classList.add('shadow-bg') : nav.classList.remove('shadow-bg')
}

const darkTheme = () => {
    theme = 'dark'
    body.classList.add('dark')
    body.classList.remove('light')
    colorBtn.innerHTML = '<i class="fa-regular fa-lightbulb"></i>'
}

const lightTheme = () => {
    theme = 'light'
    body.classList.remove('dark')
    body.classList.add('light')
    colorBtn.innerHTML = '<i class="fa-regular fa-moon"></i>'
}

const checkColorMode = () => {
    theme === 'light' ? darkTheme() : lightTheme()
    localStorage.setItem('theme', theme)
}

const checkUserColorPreference = () => {
    if (theme === 'dark') body.classList.add('dark')
    if (theme === 'light') body.classList.add('light')
}

checkUserColorPreference()
colorBtn.addEventListener('click', checkColorMode)
window.addEventListener('scroll', addShadow)