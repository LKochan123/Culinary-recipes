const infoButton = document.querySelector('body .container .icons .info')
const closeButton = document.querySelector('body .modal-shadow .close')
const modalShadow = document.querySelector('body .modal-shadow')

const showModal = () => {
    if (!(modalShadow.style.display === 'block')) {
        modalShadow.style.display = 'block'
    } else {
        modalShadow.style.display = 'none'
    }
    modalShadow.classList.toggle('modal-animation')
}

infoButton.addEventListener('click', showModal)
closeButton.addEventListener('click', showModal)
window.addEventListener('click', e => {
    if (e.target === modalShadow) showModal()
})